from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Introduction
        yield Decisions
        if self.player.role() == C.TRUSTOR_ROLE:
            yield AssignmentA
            yield Send, dict(sent_amount=10)
        else:
            yield AssignmentB
            yield SendBack, dict(sent_back_amount=10)
        yield Results
        yield Task2Conclusion
