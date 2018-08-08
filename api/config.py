import os

class BaseConfig(object):
    TESTING = False
    DEBUG = False


class Development(BaseConfig):
    DEBUG = True

class Testing(BaseConfig):
    TESTING = False
    
app_config ={
    'development': Development,
    'testing': Testing
}

