
from flask import Blueprint, jsonify, render_template
from src import Database
from src.consts import TEMPLATE_FOLDER
from src.models.database.Asset import Asset
from src.models.database.AssetValue import AssetValue

assetValueBlueprint = Blueprint('assetValue', __name__, template_folder=TEMPLATE_FOLDER)

@assetValueBlueprint.route("/asset-value/<assetId>")
def assetValuePage(assetId):
    
    asset = Asset.query.get_or_404(assetId)
    
    assetValues = Database.session.query(AssetValue).filter(AssetValue.assetId==assetId).limit(100).all();

    timestamps = [value.timestamp for value in assetValues]
    values = [value.openValue for value in assetValues]

    return render_template('pages/asset-value.html', timestamps=timestamps, values=values, asset=asset)

@assetValueBlueprint.route("/asset-value/<assetId>/<timestamp>")
def getLastPrice(assetId, timestamp):
  assetValue = AssetValue.query.filter(AssetValue.assetId == assetId, AssetValue.timestamp >= timestamp).first()
  
  if(assetValue is None):
    assetValue = AssetValue.query.filter(AssetValue.assetId == assetId).order_by(AssetValue.timestamp.desc()).first()
  
  if(assetValue is None):
    raise
  
  return jsonify({'value': assetValue.closeValue})