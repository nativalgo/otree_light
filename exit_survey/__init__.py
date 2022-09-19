from otree.api import *
import random

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'exit_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    session.random_pay_app = random.randint(0, 3)
    print('random app selection', session.random_pay_app)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    hours_slept = models.FloatField(
        label='How many hours did you sleep last night?')
    feeling_best1 = models.StringField(choices=[['1', 'Between 5 am - 6:30 am'], ['2', 'Between 6:30 am - 7:45 am'],
                                                ['3', 'Between 7:45 am - 9:45 am'], ['4',
                                                                                     'Between 9:45 am - 11 am'],
                                                ['5', 'Between 11 am - 12 pm']],
                                       label='Considering your own "feeling best" rhythm, what time would you get up if you were entirely free to plan your day?')
    tired2 = models.StringField(
        choices=[['1', 'Very tired'], ['2', 'Fairly tired'], [
            '3', 'Fairly refreshed'], ['4', 'Very refreshed']],
        label='During the first half-hour after waking up in the morning, how tired do you feel?')
    sleep3 = models.StringField(
        choices=[['1', 'Between 8 pm - 9 pm'], ['2', 'Betwen 9 pm - 10:15 pm'], ['3', 'Between 10:15 pm - 12:45 am'],
                 ['4', 'Between 12:45 am - 2 am'], ['5', 'Between 2 am - 3 am']],
        label='At what time in the evening do you feel tired, and as a result in need of sleep?')
    peak4 = models.StringField(choices=[['1', 'Between 12 am - 4:30 am'], ['2', 'Between 4:30 am - 7:30 am'],
                                        ['3', 'Between 7:30 am - 8:45 am'], ['4',
                                                                             'Between 8:45 am - 4:30 pm '],
                                        ['5', 'Between 4:30 pm - 11 pm'], ['6', 'Between 11 pm - 12 am']],
                               label='At what time of the day do you think you reach your “feeling best” peak?')
    female = models.StringField(choices=[['0', 'Male'], ['1', 'Female'], ['2', 'Other'], ['3', 'Prefer not to answer']],
                                label='Please indicate your gender')
    race = models.StringField(
        choices=[['1', 'Asian/Pacific Islander'], ['2', 'African American'], ['3', 'Caucasian/White'],
                 ['4', 'Native American/Indigenous'], ['5', 'Other']], label='Please indicate your race')
    hispanic = models.StringField(
        choices=[['0', 'No'], ['1', 'Yes']], label='Are you Hispanic?')
    age_genpop = models.StringField(
        choices=[['1', '18-25'], ['2', '26-35'],
                 ['3', '36-45'], ['4', '45-59'], ['5', '60+']],
        label='Please indicate your age range')
    age_student = models.IntegerField(label='Please indicate your age range')
    year_school = models.StringField(
        choices=[['1', '1st year undergraduate'], ['2', '2nd year undergraduate'], ['3', '3rd year undergraduate'],
                 ['4', '4th year undergraduate'], [
                     '5', '5th+ year undergraduate'], ['6', 'Graduate student'],
                 ['7', 'Non-student']], label='Please indicate your year in school')
    income = models.StringField(
        choices=[['1', 'Less than $30,000'], ['2', '$30,000 - $49,999'], ['3', '$50,000 - $74,999'],
                 ['4', '$75,000 - $99,999'], ['5', '$100,000 - $124,999'], ['6', '$125,000 +']],
        label='Please indicate your gross annual household income (if undergraduate student, you may consider your parent’s income as your household income)')
    hh_size = models.IntegerField(
        label='How many people in your household? Note: if you used your parent’s income in the previous question, please indicate the number of that household, not your current living arrangement ')
    comments = models.StringField(blank=True,
                                  label='Please provide any comments that you would like to share with the research team at this time.')


class Survey1(Page):
    form_model = 'player'
    form_fields = ['hours_slept', 'feeling_best1']

    # Calculate the payoff early to give chance to prepare if monitoring admin page
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        session = player.session
        selected_task = session.task_order[session.random_pay_app]
        participant.payoff = participant[selected_task + '_payoff']

        print(dict(participant=player.id_in_group, payoff=participant.payoff))


class Survey2(Page):
    form_model = 'player'
    form_fields = ['tired2']


class Survey3(Page):
    form_model = 'player'
    form_fields = ['sleep3']


class Survey4(Page):
    form_model = 'player'
    form_fields = ['peak4']


class Survey5(Page):
    form_model = 'player'
    form_fields = ['female']


class Survey6(Page):
    form_model = 'player'
    form_fields = ['race', 'hispanic']


class Survey7(Page):
    form_model = 'player'
    form_fields = ['age_genpop', 'age_student', 'year_school']

    @staticmethod
    def get_form_fields(player):
        if player.participant.is_genpop:
            return ['age_genpop']
        else:
            return ['age_student', 'year_school']


class Survey8(Page):
    form_model = 'player'
    form_fields = ['income', 'hh_size']


class Comments(Page):
    form_model = 'player'
    form_fields = ['comments']


class Final(Page):

    def vars_for_template(player: Player):
        return dict(
            selected_task=player.session.random_pay_app + 1
        )


page_sequence = [Survey1, Survey2, Survey3, Survey4,
                 Survey5, Survey6, Survey7, Survey8, Comments, Final]
