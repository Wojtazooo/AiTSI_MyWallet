import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def ConfigureDatabase(): 
    basedir = os.path.abspath(os.path.dirname(__file__))
    App.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return SQLAlchemy(App)

def FormatDecimal(value):
    if(value == None): 
        return value;
    return "%.2f" % value

App = Flask(__name__)
Database = ConfigureDatabase()

from src.pages.home import HomeBlueprint
from src.pages.transactions import TransactionsBlueprint
from src.pages.userProfile import UserProfileBlueprint
from src.pages.walletDetails import WalletDetailsBlueprint
from src.pages.assetValue import assetValueBlueprint

App.register_blueprint(HomeBlueprint);
App.register_blueprint(TransactionsBlueprint)
App.register_blueprint(WalletDetailsBlueprint)
App.register_blueprint(UserProfileBlueprint)
App.register_blueprint(assetValueBlueprint)
App.jinja_env.globals.update(FormatDecimal=FormatDecimal)
