import os
from dotenv import load_dotenv
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))


class Config():

    """
    Set Config variables for our flask app.
    Using Environment variables where available otherwise
    Create config variables.
    """

    FLASK_APP = os.environ.get('FLASK_APP') #looking for the key of Flask_APP in our .env file 
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = True 
    SECRET_KEY = os.environ.get('SECRET_KEY') or "don't be suspicious" #just needs to be present 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #hide update messages 
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)