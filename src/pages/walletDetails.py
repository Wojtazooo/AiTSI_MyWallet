
from flask import Blueprint, render_template
from src.consts import TEMPLATE_FOLDER
from src.models.DTO.WalletPosition import GetWalletPositions

from src.models.DTO.WalletSummary import GetWalletSummary

WalletDetailsBlueprint = Blueprint('walletDetails', __name__, template_folder=TEMPLATE_FOLDER)

@WalletDetailsBlueprint.route("/wallet-details")
def WalletDetails():
    walletPositions = GetWalletPositions()
    walletSummary = GetWalletSummary()

    pieChartLabels = [position.assetName for position in walletPositions]
    pieChartValues = [position.currentAssetWorth * 100 / walletSummary.totalWalletValue for position in walletPositions]

    return render_template('pages/wallet-details.html', walletPositions=walletPositions, pieChartLabels=pieChartLabels, pieChartValues=pieChartValues)