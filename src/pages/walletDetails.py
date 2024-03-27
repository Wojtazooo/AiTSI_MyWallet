
from flask import Blueprint, render_template
from sqlalchemy import func, text
from src import Database
from src.consts import TEMPLATE_FOLDER
from src.models.WalletTransaction import WalletTransaction

WalletDetailsBlueprint = Blueprint('walletDetails', __name__, template_folder=TEMPLATE_FOLDER)

@WalletDetailsBlueprint.route("/wallet-details")
def WalletSummaryPage():
    sql_query = """
    SELECT
        A.name as assetName,
        SUM(WT.count) as currentAssetCount,
        SUM(WT.count * WT.price + WT.fees) as transactionTotalCost
    FROM
        wallet_transaction WT
    JOIN
        asset A ON WT.assetId = A.id
    GROUP BY
        A.id, A.name;
    """

    walletPositions = Database.session.execute(text(sql_query)).fetchall()

    print(walletPositions);

    return render_template('pages/wallet-details.html', walletPositions=walletPositions)
