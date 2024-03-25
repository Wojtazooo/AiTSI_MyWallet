
from flask import Blueprint, render_template
from src.consts import TEMPLATE_FOLDER

WalletDetailsBlueprint = Blueprint('walletDetails', __name__, template_folder=TEMPLATE_FOLDER)

@WalletDetailsBlueprint.route("/wallet-details")
def WalletSummaryPage():
    return render_template('pages/wallet-details.html')
