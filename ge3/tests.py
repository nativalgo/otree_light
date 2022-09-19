from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Intro
        yield Instructions
        yield Explanation
        yield Quiz, dict(employee_answer=78, employer_answer=6)
        if self.player.role() == C.EMPLOYER_ROLE:
            yield AssignmentA
            yield Adecision, dict(desired_employee_work_effort=0.5, employer_wage_offer=50)
        else:
            yield AssignmentB
            yield Bdecision, dict(employee_work_effort=0.5)
        yield Results
