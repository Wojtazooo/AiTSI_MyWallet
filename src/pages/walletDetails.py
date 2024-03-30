
from flask import Blueprint, render_template
from sqlalchemy import  text
from src import Database
from src.consts import TEMPLATE_FOLDER

WalletDetailsBlueprint = Blueprint('walletDetails', __name__, template_folder=TEMPLATE_FOLDER)

@WalletDetailsBlueprint.route("/wallet-details")
def WalletSummaryPage():
    sql_query = """
SELECT
    *,
    currentAssetWorth - transactionTotalCost as assetGain,
    (currentAssetWorth - transactionTotalCost) / transactionTotalCost as assetPercentageReturn,
    transactionTotalCost / currentAssetCount as assetAverageBuyPrice
FROM
    (
        SELECT
            A.name as assetName,
            AV.lastAssetCloseValue as lastAssetCloseValue,
            SUM(WT.count) as currentAssetCount,
            SUM(WT.count * WT.price + WT.fees) as transactionTotalCost,
            SUM(WT.count * AV.lastAssetCloseValue) as currentAssetWorth
        FROM
            wallet_transaction WT
            JOIN asset A ON WT.assetId = A.id
            JOIN (
                SELECT
                    assetId,
                    closeValue as lastAssetCloseValue
                FROM
                    asset_value
                ORDER BY
                    timestamp DESC
                LIMIT
                    1
            ) AV ON AV.assetId = A.id
        GROUP BY
            A.id,
            A.name
    );

    """

    walletPositions = Database.session.execute(text(sql_query)).fetchall()

    print(walletPositions);

    return render_template('pages/wallet-details.html', walletPositions=walletPositions)
