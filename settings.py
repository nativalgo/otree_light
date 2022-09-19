from os import environ

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=10)
SESSION_CONFIGS = [
    dict(name='UTPG', num_demo_participants=None, app_sequence=['Intro', 'ultimatum', 'trust', 'pg_et', 'ge', 'exit_survey'],
         use_browser_bots=True),
    dict(name='UTGP', num_demo_participants=None, app_sequence=['Intro', 'ultimatum', 'trust', 'ge','pg_et',  'exit_survey'],
         use_browser_bots=True),
    dict(name='UPGT', num_demo_participants=None, app_sequence=['Intro', 'ultimatum', 'pg_et', 'ge', 'trust', 'exit_survey'],
         use_browser_bots=True),
    dict(name='UPTG', num_demo_participants=None, app_sequence=['Intro', 'ultimatum',  'pg_et', 'trust','ge', 'exit_survey'],
         use_browser_bots=True),
    dict(name='UGPT', num_demo_participants=None, app_sequence=['Intro', 'ultimatum', 'ge', 'pg_et', 'trust', 'exit_survey'],
         use_browser_bots=True),
    dict(name='UGTP', num_demo_participants=None, app_sequence=['Intro', 'ultimatum', 'ge', 'trust', 'pg_et', 'exit_survey'],
         use_browser_bots=True),
    dict(name='TUPG', num_demo_participants=None, app_sequence=['Intro', 'trust', 'ultimatum', 'pg_et', 'ge', 'exit_survey'],
         use_browser_bots=True),
    dict(name='TUGP', num_demo_participants=None, app_sequence=['Intro', 'trust', 'ultimatum', 'ge','pg_et',  'exit_survey'],
         use_browser_bots=True),
    dict(name='TGUP', num_demo_participants=None, app_sequence=['Intro', 'trust', 'ge', 'ultimatum', 'pg_et', 'exit_survey'],
         use_browser_bots=True),
    dict(name='TGPU', num_demo_participants=None, app_sequence=['Intro', 'trust', 'ge', 'pg_et', 'ultimatum', 'exit_survey'],
         use_browser_bots=True),
    dict(name='TPGU', num_demo_participants=None, app_sequence=['Intro', 'trust', 'pg_et', 'ge', 'ultimatum', 'exit_survey'],
         use_browser_bots=True),
    dict(name='TPUG', num_demo_participants=None, app_sequence=['Intro', 'trust', 'pg_et', 'ultimatum', 'ge', 'exit_survey'],
         use_browser_bots=True),
    dict(name='PUTG', num_demo_participants=None, app_sequence=['Intro', 'pg_et', 'ultimatum', 'trust', 'ge', 'exit_survey'],
         use_browser_bots=True),
    dict(name='PUGT', num_demo_participants=None, app_sequence=['Intro', 'pg_et', 'ultimatum', 'ge', 'trust', 'exit_survey'],
         use_browser_bots=True),
    dict(name='PGUT', num_demo_participants=None, app_sequence=['Intro', 'pg_et', 'ge', 'ultimatum', 'trust', 'exit_survey'],
         use_browser_bots=True),
    dict(name='PGTU', num_demo_participants=None, app_sequence=['Intro', 'pg_et', 'ge', 'trust', 'ultimatum', 'exit_survey'],
         use_browser_bots=True),
    dict(name='PTGU', num_demo_participants=None, app_sequence=['Intro', 'pg_et', 'trust', 'ge', 'ultimatum', 'exit_survey'],
         use_browser_bots=True),
    dict(name='PTUG', num_demo_participants=None, app_sequence=['Intro', 'pg_et', 'trust', 'ultimatum', 'ge', 'exit_survey'],
         use_browser_bots=True),
    dict(name='GUTP', num_demo_participants=None, app_sequence=['Intro', 'ge', 'ultimatum', 'trust', 'pg_et', 'exit_survey'],
         use_browser_bots=True),
    dict(name='GUPT', num_demo_participants=None, app_sequence=['Intro', 'ge', 'ultimatum', 'pg_et', 'trust', 'exit_survey'],
         use_browser_bots=True),
    dict(name='GPTU', num_demo_participants=None, app_sequence=['Intro', 'ge', 'pg_et', 'trust', 'ultimatum', 'exit_survey'],
         use_browser_bots=True),
    dict(name='GPUT', num_demo_participants=None, app_sequence=['Intro', 'ge', 'pg_et', 'ultimatum', 'trust', 'exit_survey'],
         use_browser_bots=True),
    dict(name='GTUP', num_demo_participants=None, app_sequence=['Intro', 'ge', 'trust', 'ultimatum', 'pg_et', 'exit_survey'],
         use_browser_bots=True),
    dict(name='GTPU', num_demo_participants=None, app_sequence=['Intro', 'ge', 'trust', 'pg_et', 'ultimatum', 'exit_survey'],
         use_browser_bots=True),
    dict(name='Escape', num_demo_participants=None, app_sequence=['exit_survey'],
         use_browser_bots=True,),
    dict(name ='trust', num_demo_participants=None, app_sequence=['trust'])
]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['payoff_ultimatum', 'payoff_trust', 'payoff_pg_et', 'payoff_ge']
SESSION_FIELDS = ['random_pay_app']
ROOMS = [dict(name='my_room', display_name='my_room')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
