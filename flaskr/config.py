import os

class Config:
    # General Configurations
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Default Logging Configuration
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')
    LOG_FILE_PATH = os.environ.get('LOG_FILE_PATH', 'logs/app.log')

    CSP = "default-src 'self'; img-src 'self' https://frontend.com https://emailapi.com; media-src 'self'; script-src 'self' https://frontend.com https://emailapi.com; style-src 'self' https://frontend.com; connect-src 'self' https://frontend.com https://emailapi.com;"

    # More General Configurations can go here

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
    JWT_SECRET_KEY = os.environ.get('DEV_JWT_SECRET_KEY')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
    BCRYPT_LOG_ROUNDS = 4  # For faster tests
    JWT_SECRET_KEY = os.environ.get('TEST_JWT_SECRET_KEY')
    # Other test-specific configurations
