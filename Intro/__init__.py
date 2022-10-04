
from random import random, shuffle
from otree.api import *
c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'Intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    # TODO: Determine order of the apps to run
    task_order = ['ultimatum', 'trust', 'pg_et', 'ge']
    shuffle(task_order)
    subsession.session.task_order = task_order
    print('Task order', task_order)

    # assign is_genpop based on label
    for player in subsession.get_players():
        participant = player.participant
        label = participant.label
        participant.is_genpop = label != None and label.lower()[0].to == "g"


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Instructions(Page):
    form_model = 'player'


class PFTask(Page):
    pass





page_sequence = [Instructions, PFTask]
