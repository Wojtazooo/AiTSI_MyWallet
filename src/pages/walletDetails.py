
from flask import Blueprint, render_template
from sqlalchemy import  text
from src import Database
from src.consts import TEMPLATE_FOLDER
from src.models.DTO.WalletPosition import GetWalletPositions

WalletDetailsBlueprint = Blueprint('walletDetails', __name__, template_folder=TEMPLATE_FOLDER)

@WalletDetailsBlueprint.route("/wallet-details")
def WalletDetails():
    walletPositions = GetWalletPositions()
    print(walletPositions);
    return render_template('pages/wallet-details.html', walletPositions=walletPositions)