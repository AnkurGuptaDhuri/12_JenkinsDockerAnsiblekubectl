from flask import Flask
import os
application = Flask(__name__, template_folder='templates')
application.config['DEBUG'] = True

app=application

from mypackage import db
from mypackage import routes
from mypackage import database

if not os.path.exists("./database.db"):
    print("no database. Hence creating a sqlite database.db and tables e.g. user table")
    database.create_database()
else:
    print("database already exist")




