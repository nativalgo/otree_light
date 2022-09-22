from otree.api import *

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'ultimatum_0'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    PROPOSER_ROLE = 'Player A'
    RECEIVER_ROLE = 'Player B'
    ENDOWMENT_A = 10
    ENDOWMENT_B = 0


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    subsession.group_randomly()


class Group(BaseGroup):
    decision_a = models.IntegerField(max=10, min=0)
    decision_b = models.BooleanField(
        choices=[[True, 'Accept'], [False, 'Reject']])


class Player(BasePlayer):

    def calculate_game_payoff(self):
        player = self
        group = player.group
        if group.decision_b:
            player.payoff = C.ENDOWMENT_A - \
                group.decision_a if player.role == C.PROPOSER_ROLE else group.decision_a
        else:
            player.payoff = 0

        participant = player.participant
        participant.payoff_ultimatum = sum(
            [p.payoff for p in player.in_all_rounds()])


class Instructions(Page):

    @staticmethod
    def vars_for_template(player: Player):
        idx_current_task = player.session.task_order.index('ultimatum')
        return dict(
            exchange_rate_ult=cu(2.50) if player.participant.is_genpop
            else cu(1),
            task_number=idx_current_task + 1
        )


class AssignmentU(Page):
    form_model = 'player'


class Adecision(Page):
    form_model = 'group'
    form_fields = ['decision_a']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.PROPOSER_ROLE


class MyWaitPageAdecision(WaitPage):
    pass


class Bdecision(Page):
    form_model = 'group'
    form_fields = ['decision_b']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.RECEIVER_ROLE

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return {"proposed_amount": C.ENDOWMENT_A - group.decision_a}


class MyWaitPageBdecision(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        players = group.get_players()
        for p in players:
            p.calculate_game_payoff()


class Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        decision = 'accepted' if group.decision_b else 'rejected'
        return dict(payoff=int(player.payoff), decision=decision)


class Conclusion(Page):
    form_model = 'player'


class Done(WaitPage):

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        task_order = player.session.task_order
        idx_current_app = task_order.index('ultimatum')
        if idx_current_app == 3:
            return upcoming_apps[-1]
        return f'{task_order[idx_current_app + 1]}{idx_current_app + 1}'


page_sequence = [Instructions, AssignmentU, Adecision,
                 MyWaitPageAdecision, Bdecision, MyWaitPageBdecision, Results, Conclusion, Done]
