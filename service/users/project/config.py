import os

class BaseConfig:
    """Configurationd de base"""
    TESTING = False
    SQLALCHEMY_TRACK8MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """ Configuration de developpement"""
    SQLAALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
    """ Test de la configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('')

class TestingConfig(BaseConfig):
    """ Configuration de la production"""
    pass