import os
import random
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.walletPosition import WalletPosition

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class WalletPositionDbModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  assetId = db.Column(db.Integer, nullable=False)
  count = db.Column(db.Integer, nullable=False)
  currentValue = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

@app.route("/")
def IndexPage():
    return render_template('index.html')

@app.route("/home")
def Welcome():
    return render_template('home-page/home.html')

@app.route('/transactions')
def TranactionsPage():
    return render_template('transactions-page/transactions.html')

@app.route('/transactions/add')
def AddTransaction():
    return render_template('transactions-page/transactions.html')

@app.route("/wallet-details")
def WalletSummaryPage():
    walletPositions = [
        WalletPosition(7, 2, 10.4),
        WalletPosition(2, 3, 20.1),
        WalletPosition(random.randint(1, 10), 1, random.random()),
    ]

    walletSum = 0;

    for position in walletPositions:
        walletSum += position.count * position.currentPrice;

    return render_template('wallet-details-page/wallet-details.html', walletPositions = walletPositions, walletSum = walletSum)

@app.route("/user-profile")
def UserProfilePage():
    return render_template('user-profile-page/user-profile.html')
