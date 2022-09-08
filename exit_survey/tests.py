from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Survey1, dict(hours_slept=0,feeling_best1=1)
        yield Survey2, dict(tired2=1)
        yield Survey3, dict(sleep3=1)
        yield Survey4, dict(peak4=1)
        yield Survey5, dict(female=1)
        yield Survey6, dict(race=1, hispanic=1)
        yield Survey7, dict(age_student=1, year_school=1)
        yield Survey8, dict(income=1, hh_size=1)
        yield Comments
        yield Final