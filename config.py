import os, random, string

class Config(object):
    CSRF_ENABLE = True
    SECRET_KEY = 'CC9CDFEA96DA97FAE0162D6DC1CDF41FAADFB5366AB682377C241F0333D8F8D0'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    
class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST) # http://localhost:8000
    
app_config = {
    'development': DevelopmentConfig(),
    'testing': None,
    'production': None
}

app_active = os.getenv('FLASK_ENV') # para setar, no terminal: export FLASK_ENV=development

if app_config is None:
    app_config = 'development'

#app_config[app_active]