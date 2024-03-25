
import datetime
from flask import Blueprint, render_template, request
from src import Database
from src.consts import TEMPLATE_FOLDER
from src.models.Asset import Asset
from src.models.WalletTransaction import WalletTransaction

TransactionsBlueprint = Blueprint('transactions', __name__, template_folder=TEMPLATE_FOLDER)

@TransactionsBlueprint.route('/transactions', methods = ['POST', 'GET'])
def TranactionsPage():
    if request.method == 'POST':
        json = request.get_json();

        print("transactions/add")
        print(f"json: {json}");

        # TODO: add calendar to select it
        timestampValue = datetime.datetime.utcnow()

        transaction = WalletTransaction(assetId=json['assetId'], count=json['count'],timestamp=timestampValue, price=json['price'], fees=json['fee']);
        Database.session.add(transaction)
        Database.session.commit()

        return {}
    else:
        transactionsToDisplay = WalletTransaction.query.order_by(WalletTransaction.timestamp.desc()).all()

        return render_template('pages/transactions.html', transactions = transactionsToDisplay)

@TransactionsBlueprint.route('/transaction-add')
def TransactionAddPage():
    return render_template('pages/transaction-add.html', assets=Asset.query.all())
