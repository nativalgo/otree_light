from otree.api import *

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'ge_2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    EMPLOYER_ROLE = 'employer'
    EMPLOYEE_ROLE = 'employee'
    MIN_WAGE = 20
    MAX_WAGE = 120
    EXCHANGE_RATE_S = 0.20
    # Effort * 1/10 (Principal return)
    EFFORT_TO_RETURN = {
        0.1: 0.1,
        0.2: 0.2,
        0.3: 0.3,
        0.4: 0.4,
        0.5: 0.5,
        0.6: 0.6,
        0.7: 0.7,
        0.8: 0.8,
        0.9: 0.9,
        1: 1, }

    # Cost of Effort (Agent's looses)
    EFFORT_TO_COST = {
        0.1: 0,
        0.2: 1,
        0.3: 2,
        0.4: 4,
        0.5: 6,
        0.6: 8,
        0.7: 10,
        0.8: 12,
        0.9: 15,
        1: 18, }


def cost_from_effort(effort: float):
    return c(C.EFFORT_TO_COST[effort])


def return_from_effort(effort: float):
    return c(C.EFFORT_TO_RETURN[effort])


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    subsession.group_randomly()


class Group(BaseGroup):
    # --- set round results and player's payoff
    # --------------------------------------------------------------------

    pay_this_round = models.BooleanField()
    round_result = models.CurrencyField()

    total_return = models.CurrencyField(
        # doc="""Total return from agent's effort = [Return for single unit of
        # agent's work effort] * [Agent's work effort]"""
    )

    employer_wage_offer = models.PositiveIntegerField(
        #doc="""Amount offered as fixed pay to agent""",
        min=C.MIN_WAGE, max=C.MAX_WAGE,
        label='What wage would you like to offer?',
    )

    desired_employee_work_effort = models.FloatField(
        choices=[C.EFFORT_TO_RETURN[x] for x in C.EFFORT_TO_RETURN],
        widget=widgets.RadioSelectHorizontal(),
        label='What effort do you expect from your employee?',
    )

    employee_work_effort = models.FloatField(
        choices=[C.EFFORT_TO_RETURN[x] for x in C.EFFORT_TO_RETURN],
        widget=widgets.RadioSelectHorizontal(),
        label='Which effort level would you like to choose?'
    )

    employee_work_cost = models.CurrencyField(
        #        doc="""Agent's cost of work effort"""
    )

    def set_payoffs(self):
        employer = self.get_player_by_role('employer')
        employee = self.get_player_by_role('employee')

        #       if not self.contract_accepted:
        #          principal.payoff = Constants.reject_principal_payoff
        #          agent.payoff = Constants.reject_agent_payoff
        #       else:
        self.employee_work_cost = cost_from_effort(self.employee_work_effort)
        self.total_return = return_from_effort(self.employee_work_effort)

        money_to_employee = self.employer_wage_offer

        employee.payoff = money_to_employee - self.employee_work_cost - 20
        employer.payoff = self.employee_work_effort * (120 - money_to_employee)

        employee.participant.payoff_ge = employee.payoff * C.EXCHANGE_RATE_S
        employer.participant.payoff_ge = employer.payoff * C.EXCHANGE_RATE_S


class Player(BasePlayer):
    employer_answer = models.IntegerField(label="Employer's payoff (tokens)")
    employee_answer = models.IntegerField(label="Employee's payoff (tokens)")

    def role(self):
        if self.id_in_group == 1:
            return 'employer'
        if self.id_in_group == 2:
            return 'employee'


def employer_answer_error_message(player, value):
    if value != 6:
        return 'Employer payoff function: (120 - w) * e'


def employee_answer_error_message(player, value):
    if value != 78:
        return 'Employee payoff function: w - c(e) - 20'


class Intro(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        task_order = player.session.task_order
        idx_current_task = task_order.index('ge')

        return dict(
            exchange_rate_ge=cu(0.50) if player.participant.is_genpop
            else cu(0.20),
            task_number=idx_current_task + 1
        )


class Instructions(Page):
    form_model = 'player'


class Explanation(Page):
    form_model = 'player'


class Quiz(Page):
    form_model = 'player'
    form_fields = ['employee_answer', 'employer_answer']


class AssignmentA(Page):

    @staticmethod
    def is_displayed(player):
        return player.role() == C.EMPLOYER_ROLE


class AssignmentB(Page):
    @staticmethod
    def is_displayed(player):
        return player.role() == C.EMPLOYEE_ROLE


class Adecision(Page):
    form_model = 'group'
    form_fields = ['desired_employee_work_effort', 'employer_wage_offer']

    @staticmethod
    def is_displayed(player):
        return player.role() == C.EMPLOYER_ROLE


class MyWaitPageAdecision(WaitPage):
    @staticmethod
    def is_displayed(player):
        return player.role() == C.EMPLOYEE_ROLE


class Bdecision(Page):
    form_model = 'group'
    form_fields = ['employee_work_effort']

    @staticmethod
    def is_displayed(player):
        return player.role() == C.EMPLOYEE_ROLE


class MyWaitPageBdecision(WaitPage):

    @staticmethod
    def is_displayed(player):
        return player.role() == C.EMPLOYER_ROLE

    def after_all_players_arrive(group: Group):
        group.set_payoffs()


class Results(Page):

    def vars_for_template(player: Player):
        group = player.group
        employer = group.get_player_by_role(C.EMPLOYER_ROLE)
        employee = group.get_player_by_role(C.EMPLOYEE_ROLE)

        return dict(employer_payoff=int(employer.payoff), employee_payoff=int(employee.payoff))


class Done(WaitPage):

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):

        task_order = player.session.task_order
        idx_current_app = task_order.index('ge')
        if idx_current_app == 3:
            return upcoming_apps[-1]
        return f'{task_order[idx_current_app+1]}{idx_current_app+1}'


page_sequence = [Intro, Instructions, Explanation, Quiz, AssignmentA, AssignmentB,
                 Adecision, MyWaitPageAdecision, Bdecision, MyWaitPageBdecision, Results, Done]
