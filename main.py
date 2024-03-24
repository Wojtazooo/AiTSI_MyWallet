import os
import random
from flask import Flask, render_template
from models.walletPosition import WalletPosition

sijaxPath = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

app = Flask(__name__)
app.config['SIJAX_STATIC_PATH'] = sijaxPath
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'


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
