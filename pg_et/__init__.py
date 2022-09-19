from otree.api import *

c = cu

doc = 'Public Goods game set up for eye-tracking data collection'


class C(BaseConstants):
    NAME_IN_URL = 'pg_et'
    PLAYERS_PER_GROUP = 4
    MULTIPLIER = 2
    PRACTICE_ROUNDS = 2
    ENDOWMENT = 10
    NUM_REAL_ROUNDS = 10
    NUM_ROUNDS = PRACTICE_ROUNDS + NUM_REAL_ROUNDS
    EXCHANGE_RATE_S = 0.1


class Subsession(BaseSubsession):

    def creating_subsession(self):
        subsession = self
        subsession.is_practice_round = (
                subsession.round_number <= C.NUM_PRACTICE_ROUNDS
        )
        if not subsession.is_practice_round:
            subsession.real_round_number = (
                    subsession.round_number - C.NUM_PRACTICE_ROUNDS
            )

        # assign is_genpop based on label
        for player in subsession.get_players():
            player.is_genpop = player.participant.label.lower()[0].to == "g"

    def is_practice_round(self):
        return self.round_number <= C.PRACTICE_ROUNDS


class Group(BaseGroup):
    total_contribution = models.IntegerField()
    individual_share = models.FloatField()

    def compute_payoffs(self):
        group = self
        subsession = group.subsession
        players = group.get_players()
        group.total_contribution = sum(p.contribution for p in players)
        group.individual_share = (
                group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
        )

        for p in players:
            p.payoff = C.ENDOWMENT - p.contribution + group.individual_share
            if group.round_number == C.NUM_ROUNDS:
                p.calculate_game_payoff()


class Player(BasePlayer):
    is_genpop = models.BooleanField(initial=False)
    contribution = models.IntegerField(label='Your contribution in the public account:', max=C.ENDOWMENT, min=0)
    private = models.IntegerField(label='Your contribution in the private account:', max=C.ENDOWMENT, min=0)

    def calculate_game_payoff(self):
        participant = self.participant
        participant.payoff_pg_et = (sum([p.payoff for p in self.in_rounds(C.PRACTICE_ROUNDS + 1, C.NUM_ROUNDS)]))*C.EXCHANGE_RATE_S


class Instructions1(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        subsession = player.subsession
        return subsession.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return dict(exchange_rate_pg=cu(0.25) if player.is_genpop else cu(0.10))


class PrivateAccountDescription(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        subsession = player.subsession
        return subsession.round_number == 1


class PublicAccountDescription(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        subsession = player.subsession
        return subsession.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        individual_share_multiplier = C.MULTIPLIER / C.PLAYERS_PER_GROUP
        return dict(individual_share_multiplier=individual_share_multiplier)


class Instructions2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        subsession = player.subsession
        return subsession.round_number == 1


class Contribute(Page):
    form_model = 'player'
    form_fields = ['private', 'contribution']

    @staticmethod
    def vars_for_template(player: Player):
        subsession = player.subsession
        group = player.group
        title = f"Practice Round {subsession.round_number}" if group.round_number <= C.PRACTICE_ROUNDS else f"Round {group.round_number - C.PRACTICE_ROUNDS}"
        has_prev_info = (1 < group.round_number and group.round_number < C.PRACTICE_ROUNDS + 1) or (
                group.round_number > C.PRACTICE_ROUNDS + 1)
        previous_round_public = player.in_round(subsession.round_number - 1).contribution if has_prev_info else ""
        previous_round_private = C.ENDOWMENT - previous_round_public if has_prev_info else ""
        previous_total = group.in_round(group.round_number - 1).total_contribution if has_prev_info else ""
        previous_individual = C.ENDOWMENT - previous_round_public + group.in_round(
            group.round_number - 1).individual_share if has_prev_info else ""

        return dict(round_title=title, has_prev_info=has_prev_info, previous_round_public=previous_round_public,
                    previous_round_private=previous_round_private, previous_total=previous_total,
                    previous_individual=previous_individual)

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values['contribution'] + values['private'] != C.ENDOWMENT:
            return F'The numbers must add up to {C.ENDOWMENT}'


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        group.compute_payoffs()


class Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        session = player.session
        subsession = player.subsession
        pagetitle = f"Your Results, Practice Round {subsession.round_number}" if subsession.round_number <= C.PRACTICE_ROUNDS else f"Your Results, Round {subsession.round_number - C.PRACTICE_ROUNDS}"
        return dict(page_title=pagetitle, payoff=int(player.payoff))


class Conclusion(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Instructions1, PrivateAccountDescription, PublicAccountDescription, Instructions2, Contribute,
                 ResultsWaitPage, Results, Conclusion]
