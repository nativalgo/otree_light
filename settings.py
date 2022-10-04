from os import environ

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=15, dark=True)
SESSION_CONFIGS = [
    dict(name='Eric_is_da_best',
         num_demo_participants=None,
         app_sequence=['Intro',
                       # Will choose a random order and ignore games in-between
                       'ultimatum0', 'trust0', 'pg_et0', 'ge0',
                       'ultimatum1', 'trust1', 'pg_et1', 'ge1',
                       'ultimatum2', 'trust2', 'pg_et2', 'ge2',
                       'ultimatum3', 'trust3', 'pg_et3', 'ge3',
                       'exit_survey'],
         ),
    dict(name='ROBO_Eric_is_cranky',
         num_demo_participants=None,
         app_sequence=['Intro',
                       # Will choose a random order and ignore games in-between
                       'ultimatum0', 'trust0', 'pg_et0', 'ge0',
                       'ultimatum1', 'trust1', 'pg_et1', 'ge1',
                       'ultimatum2', 'trust2', 'pg_et2', 'ge2',
                       'ultimatum3', 'trust3', 'pg_et3', 'ge3',
                       'exit_survey'],
         use_browser_bots=True,
         ),
    dict(name='Escape',
         num_demo_participants=None,
         app_sequence=['exit_survey'],
         use_browser_bots=True,),
    dict(name='trust',
         num_demo_participants=None,
         app_sequence=['trusttest'])
]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['is_genpop', 'payoff_ultimatum',
                      'payoff_trust', 'payoff_pg_et', 'payoff_ge']
SESSION_FIELDS = ['task_order', 'random_pay_app']
ROOMS = [dict(name='my_room', display_name='my_room',
              participant_label_file='_rooms/test.txt')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
