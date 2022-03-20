

from operator import truediv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://localhost:13306/eldorado-mecanica?allowPublicKeyRetrieval=true&useSSL=false'