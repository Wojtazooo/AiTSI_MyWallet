
import base64
import io
from flask import Blueprint, render_template
from matplotlib import pyplot as plt
import numpy as np
from src import Database
from src.consts import TEMPLATE_FOLDER
from src.models.database.AssetValue import AssetValue

assetValueBlueprint = Blueprint('assetValue', __name__, template_folder=TEMPLATE_FOLDER)

@assetValueBlueprint.route("/asset-value/<assetId>")
def UserProfilePage(assetId):
    print(assetId)
    assetValues = Database.session.query(AssetValue).filter(AssetValue.assetId==assetId).all();

    timestamps = [value.timestamp for value in assetValues]
    values = [value.openValue for value in assetValues]

    x_values = np.arange(len(timestamps))

    # Create a Matplotlib plot
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, values, marker=',')
    plt.xticks(x_values, timestamps)  # Set the tick labels to the dates
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price Chart')
    plt.grid(True)

    # Convert the plot to a PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('pages/asset-value.html', plot_url=plot_url)
