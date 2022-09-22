from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield Instructions1
            yield PrivateAccountDescription
            yield PublicAccountDescription
            yield Instructions2
        yield Contribute, dict(private=3, contribution=7)
        yield Results
        if self.round_number == C.NUM_ROUNDS:
            yield Conclusion
