
import datetime
from flask import Blueprint, render_template, request
from src import Database
from src.consts import TEMPLATE_FOLDER
from src.models.database.Asset import Asset
from src.models.database.WalletTransaction import WalletTransaction
from datetime import datetime

TransactionsBlueprint = Blueprint('transactions', __name__, template_folder=TEMPLATE_FOLDER)

@TransactionsBlueprint.route('/transactions', methods = ['POST', 'GET', 'PUT'])
def TranactionsPage():
    if request.method == 'POST':
        json = request.get_json();

        print(f"[transactions/add] json: {json}");

        timestampValue = datetime.strptime(json['timestamp'], '%Y-%m-%d')
        print(timestampValue)

        transaction = WalletTransaction(
            assetId=json['assetId'], 
            count=json['count'],
            timestamp=timestampValue, 
            price=json['price'], 
            fees=json['fees']);
        Database.session.add(transaction)
        Database.session.commit()

        return {}
    
    elif request.method == 'GET':
        transactionsToDisplay = WalletTransaction.query.order_by(WalletTransaction.timestamp.desc()).all()

        return render_template('pages/transactions.html', transactions = transactionsToDisplay)
    

@TransactionsBlueprint.route('/transactions/<transactionId>', methods = ['PUT', 'DELETE'])
def EditTransaction(transactionId):
  if request.method == 'PUT':
    json = request.get_json();

    transactionToUpdate = WalletTransaction.query.get_or_404(transactionId)

    timestampValue = datetime.strptime(json['timestamp'], '%Y-%m-%d')

    transactionToUpdate.assetId = json['assetId']
    transactionToUpdate.count = json['count']
    transactionToUpdate.timestamp = timestampValue
    transactionToUpdate.price = json['price']
    transactionToUpdate.fees = json['fees']
    Database.session.commit()
    return {}
  elif request.method == 'DELETE':
    transaction = WalletTransaction.query.get_or_404(transactionId)
    Database.session.delete(transaction)
    Database.session.commit()
    return {}

@TransactionsBlueprint.route('/transaction-add')
def TransactionAddPage():
    return render_template('pages/transaction-add.html', assets=Asset.query.all(), todayDate = datetime.now().strftime("%Y-%m-%d"))

@TransactionsBlueprint.route('/transaction-edit/<transactionId>')
def TransactionEditPage(transactionId):
    transactionToEdit = WalletTransaction.query.get(transactionId)
    print(transactionToEdit)

    return render_template('pages/transaction-edit.html', assets=Asset.query.all(), transactionToEdit = transactionToEdit)

