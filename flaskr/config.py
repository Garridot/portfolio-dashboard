class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Otros parámetros de configuración comunes


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 4  # Para hacer más rápidas las pruebas
    JWT_SECRET_KEY = 'your-secret-key-for-tests'
    # Otros parámetros específicos para pruebas
