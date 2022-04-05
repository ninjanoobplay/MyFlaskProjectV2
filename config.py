

class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S'


class DevelopmentConfig(Config):
    DEBUG = True
    # Essa Config Abaixo é para Flask-SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Use isso como Exemplo SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'
    # Para Mais Informações Leia a Documentação do Flask-SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_login'
    #print(SQLALCHEMY_TRACK_MODIFICATIONS,"HOST: ",SQLALCHEMY_DATABASE_URI)
    # Essa Config Abaixo é para Flask-MySQLdb
    #MYSQL_HOST = 'localhost'
    #MYSQL_USER = 'root'
    #MYSQL_PASSWORD = ''
    #MYSQL_DB = 'flask_login'


config ={
    'development':DevelopmentConfig
}