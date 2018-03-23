#Debug Statement
DEBUG = True   #development environment
import os
import configparser

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 

config = configparser.ConfigParser()  
config.read('readonly.cfg')

SQLALCHEMY_DATABASE_URI = 'mysql://' + config.get('DB', 'user') + ':' + config.get('DB', 'password') + '@' + config.get('DB', 'host') + '/' + config.get('DB', 'db')

DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True

THREADS_PER_PAGE = 2

CSRF_ENABLED     = True
CSRF_SESSION_KEY = "rg4*bl2*l1(3t$s!n#kke2k8sz8-29xc)z-n4h_)(c3"

SECRET_KEY = "pk953l2*52a(3t$s!n#kke2k8sz8-29xc))z-n4h_(b4x"