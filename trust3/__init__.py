from otree.api import *

c = cu

doc = '\nThis is a standard 2-player trust game where the amount sent by player 1 gets\ntripled. The trust game was first proposed by\n<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">\n    Berg, Dickhaut, and McCabe (1995)\n</a>.\n'


class C(BaseConstants):
    NAME_IN_URL = 'trust_3'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    MULTIPLIER = 3
    ENDOWMENT = 10
    TRUSTOR_ROLE = 'Player A'
    TRUSTEE_ROLE = 'Player B'


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    subsession.group_randomly()


class Group(BaseGroup):
    sent_amount = models.IntegerField(
        doc='Amount sent by P1', label='Please enter an amount from 0 to 10', min=0, max=10)
    sent_back_amount = models.IntegerField(doc='Amount sent back by P2', min=0)

    def compute_payoffs(self):
        group = self
        p1 = group.get_player_by_role(C.TRUSTOR_ROLE)
        p2 = group.get_player_by_role(C.TRUSTEE_ROLE)

        p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
        p2.payoff = C.ENDOWMENT + \
            (group.sent_amount * C.MULTIPLIER) - group.sent_back_amount

        p1.calculate_game_payoff()
        p2.calculate_game_payoff()


def sent_back_amount_max(group: Group):
    return group.sent_amount * C.MULTIPLIER


class Player(BasePlayer):

    def calculate_game_payoff(self):
        participant = self.participant
        participant.payoff_trust = sum(
            [p.payoff for p in self.in_all_rounds()])


class Introduction(Page):
    form_model = 'player'

    def vars_for_template(player: Player):
        idx_current_task = player.session.task_order.index('trust')
        return dict(
            exchange_rate_trust=cu(2.50) if player.participant.is_genpop
            else cu(1),
            task_number=idx_current_task + 1
        )


class Decisions(Page):
    form_model = 'player'


class AssignmentA(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.TRUSTOR_ROLE


class AssignmentB(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.TRUSTEE_ROLE


class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.TRUSTOR_ROLE


class SendWaitPage(WaitPage):
    pass


class SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.TRUSTEE_ROLE

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        tripled_amount = sent_back_amount_max(group)
        total_amount = C.ENDOWMENT + tripled_amount
        return dict(tripled_amount=tripled_amount, total_amount=total_amount)


class SendBackWaitPage(WaitPage):
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        group.compute_payoffs()


class Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER, payoff=int(player.payoff))


class Task2Conclusion(Page):
    form_model = 'player'


class Conclusion(WaitPage):
    form_model = 'player'


class Done(WaitPage):

    wait_for_all_groups = True

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        task_order = player.session.task_order
        idx_current_app = task_order.index('trust')
        if idx_current_app == 3:
            return upcoming_apps[-1]
        return f'{task_order[idx_current_app + 1]}{idx_current_app + 1}'


page_sequence = [Introduction, Decisions, AssignmentA, Send, AssignmentB, SendWaitPage, SendBack, SendBackWaitPage,
                 ResultsWaitPage, Results, Task2Conclusion, Done]
