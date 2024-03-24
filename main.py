import datetime
import os
import random
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from models.walletPosition import WalletPosition

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class WalletTransaction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  assetId = db.Column(db.Integer, nullable=False)
  count = db.Column(db.Integer, nullable=False)
  timestamp = db.Column(db.Date, nullable=False)
  price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
  fees = db.Column(db.Numeric(precision=10, scale=2), nullable=True)

  def __repr__(self):
    return f'<WalletTransaction id={self.id}, timestamp={self.timestamp}, assetId={self.assetId}, count={self.count}>'

@app.route("/")
def IndexPage():
    return render_template('index.html')

@app.route("/home")
def Welcome():
    return render_template('pages/home.html')

@app.route('/transactions', methods = ['POST', 'GET'])
def TranactionsPage():
    if request.method == 'POST':
        json = request.get_json();

        print("transactions/add")
        print(f"json: {json}");

        # TODO: add calendar to select it
        timestampValue = datetime.datetime.utcnow()

        transaction = WalletTransaction(assetId=123, count=json['count'],timestamp=timestampValue, price=json['price'], fees=json['fee']);
        db.session.add(transaction)
        db.session.commit()

        return {}
    else:
        walletTransactions = WalletTransaction.query.all()
        print(walletTransactions)
        return render_template('pages/transactions.html', transactions = walletTransactions)

@app.route('/transaction-add')
def TransactionAddPage():
    return render_template('pages/transaction-add.html')

@app.route("/wallet-details")
def WalletSummaryPage():
    return render_template('pages/wallet-details.html')

@app.route("/user-profile")
def UserProfilePage():
    return render_template('pages/user-profile.html')
