
import base64
import io
from flask import Blueprint, render_template
from matplotlib import pyplot as plt
import numpy as np
from src import Database
from src.consts import TEMPLATE_FOLDER
from src.models.database.Asset import Asset
from src.models.database.AssetValue import AssetValue

assetValueBlueprint = Blueprint('assetValue', __name__, template_folder=TEMPLATE_FOLDER)

@assetValueBlueprint.route("/asset-value/<assetId>")
def UserProfilePage(assetId):
    print(assetId)
    
    asset = Asset.query.get_or_404(assetId)
    
    assetValues = Database.session.query(AssetValue).filter(AssetValue.assetId==assetId).limit(100).all();

    print(f'found {len(assetValues)}')

    timestamps = [value.timestamp for value in assetValues]
    values = [value.openValue for value in assetValues]


    return render_template('pages/asset-value.html', timestamps=timestamps, values=values, asset=asset)
