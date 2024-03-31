
import datetime
from flask import Blueprint, render_template, request
from src import Database
from src.consts import TEMPLATE_FOLDER
from src.models.database.Asset import Asset
from src.models.database.WalletTransaction import WalletTransaction

TransactionsBlueprint = Blueprint('transactions', __name__, template_folder=TEMPLATE_FOLDER)

@TransactionsBlueprint.route('/transactions', methods = ['POST', 'GET', 'PUT'])
def TranactionsPage():
    if request.method == 'POST':
        json = request.get_json();

        print(f"[transactions/add] json: {json}");

        timestampValue = datetime.datetime.strptime(json['timestamp'], '%Y-%m-%d')
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
    elif request.method == 'PUT':
        json = request.get_json();

        print(f"[transactions/edit] json: {json}");

        transactionToUpdate = WalletTransaction.query.get_or_404(json['id'])


        timestampValue = datetime.datetime.strptime(json['timestamp'], '%Y-%m-%d')

        transactionToUpdate.assetId = json['assetId']
        transactionToUpdate.count = json['count']
        transactionToUpdate.timestamp = timestampValue
        transactionToUpdate.price = json['price']
        transactionToUpdate.fees = json['fees']

        Database.session.commit()

        return {}
    elif request.method == 'GET':
        transactionsToDisplay = WalletTransaction.query.order_by(WalletTransaction.timestamp.desc()).all()

        return render_template('pages/transactions.html', transactions = transactionsToDisplay)
    

@TransactionsBlueprint.route('/transaction-add')
def TransactionAddPage():
    return render_template('pages/transaction-add.html', assets=Asset.query.all())

@TransactionsBlueprint.route('/transaction-edit/<transactionId>')
def TransactionEditPage(transactionId):
    transactionToEdit = WalletTransaction.query.get(transactionId)
    print(transactionToEdit)

    return render_template('pages/transaction-edit.html', assets=Asset.query.all(), transactionToEdit = transactionToEdit)

