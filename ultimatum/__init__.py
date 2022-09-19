from otree.api import *

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'ultimatum'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    PROPOSER_ROLE = 'Player A'
    RECEIVER_ROLE = 'Player B'
    ENDOWMENT_A = 10
    ENDOWMENT_B = 0


class Subsession(BaseSubsession):
    pass


def creating_subsession(subsession: Subsession):
    subsession.group_randomly()

    # assign is_genpop based on label
    for player in subsession.get_players():
        player.is_genpop = player.participant.label.lower()[0].to == "g"


class Group(BaseGroup):
    decision_a = models.IntegerField(max=10, min=0)
    decision_b = models.BooleanField(choices=[[True, 'Accept'], [False, 'Reject']])
    proposed_amount = models.IntegerField()


def compute_proposed_amount(group: Group):
    session = group.session
    subsession = group.subsession
    group.proposed_amount = C.ENDOWMENT_A - group.decision_a


class Player(BasePlayer):
    is_genpop = models.BooleanField(initial=False)

    def calculate_game_payoff(self):
        player = self
        participant = player.participant
        participant.payoff_ultimatum = sum([p.payoff for p in player.in_all_rounds()])
        group = player.group
        if group.decision_b:
            player.payoff = C.ENDOWMENT_A - group.decision_a if player.role == C.PROPOSER_ROLE else group.decision_a
        else:
            player.payoff = 0


class Instructions(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(exchange_rate_ult=cu(2.50) if player.is_genpop else cu(1))


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


class Conclusion(Page):
    form_model = 'player'


page_sequence = [Instructions, AssignmentU, Adecision, MyWaitPageAdecision, Bdecision, MyWaitPageBdecision, Conclusion]
