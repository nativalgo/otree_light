
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
class Subsession(BaseSubsession):
    pass
def creating_subsession(subsession: Subsession):
    session = subsession.session
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
    group.proposed_amount = subsession.endowmentA-group.decision_a
def compute_payoffs(group: Group):
    p1 = group.get_player_by_role(C.PROPOSER_ROLE)
    p2 = group.get_player_by_role(C.RECEIVER_ROLE)
    
    if group.decisionB:
        p1.payoff = C.ENDOWMENT_A - group.decision_a
        p2.payoff = group.decision_a
    else:
        p1.payoff = 0
        p2.payoff = 0
    
    p1.calculate_game_payoff()
    p2.calculate_game_payoff()
class Player(BasePlayer):
    is_genpop = models.BooleanField()
def calculate_game_payoff(player: Player):
    participant = player.participant
    participant.payoff_ultimatum = sum([p.payoff for p in player.in_all_rounds()])
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
class MyWaitPageBdecision(WaitPage):
    after_all_players_arrive = compute_payoffs
class Conclusion(Page):
    form_model = 'player'
page_sequence = [Instructions, AssignmentU, Adecision, MyWaitPageAdecision, Bdecision, MyWaitPageBdecision, Conclusion]