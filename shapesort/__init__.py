from otree.api import *


doc = """
Shape Sort tasks the participant to organize shapes into colored bins until advanced. When all shapes are sorted in their respective bin the game restarts. This app can be used as a starting point and amended with timer behavior, or can be used as-is and manually advanced to proceed.
"""


class C(BaseConstants):
    NAME_IN_URL = 'shapesort'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    shapes_sorted = models.IntegerField(initial=0)
    rounds_completed = models.IntegerField(initial=0)


# PAGES
class ShapeSort(Page):
    def live_method(player: Player, data):
        print("Received live method", data)

        if data == "sorted":
            player.shapes_sorted += 1
        elif data == "completed":
            player.rounds_completed += 1


class EG(Page):
    pass


class Done(WaitPage):
    form_model = 'player'

    wait_for_all_groups = True

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        return player.session.task_order[0] + '0'


page_sequence = [EG, ShapeSort, Done]
