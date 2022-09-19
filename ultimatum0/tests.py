from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Instructions
        yield AssignmentU
        if self.player.id_in_group == 1:
            yield Adecision, dict(decision_a=7)
        else:
            yield Bdecision, dict(decision_b=True)
        yield Conclusion