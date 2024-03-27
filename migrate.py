from datetime import datetime
from src.models.Asset import Asset
from src import App, Database
from src.models.AssetValue import AssetValue
import csv

def parse_csv_and_add_to_db(csv_file, assetId):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            asset_value = AssetValue(
                assetId = assetId,
                timestamp=datetime.strptime(row['Data'], '%Y-%m-%d').date(),
                openValue=float(row['Otwarcie']),
                closeValue=float(row['Zamkniecie'])
            )
            Database.session.add(asset_value)
        Database.session.commit()

with App.app_context():
    Database.drop_all();
    Database.create_all();

    assets = [
        Asset(id=1, name='JSW', tickerSymbol='JSW'),
        Asset(id=2, name='CD Projekt', tickerSymbol='CDR'),
        Asset(id=3, name='PKO BP', tickerSymbol='PKOBP'),
        Asset(id=4, name='PZU', tickerSymbol='PZU'),
        Asset(id=5, name='Alior', tickerSymbol='ALR'),
        Asset(id=6, name='PKN ORLEN', tickerSymbol='PKN')
    ]

    for asset in assets:
        Database.session.add(asset)

    Database.session.commit()

    for asset in assets:
        try:
            parse_csv_and_add_to_db(f'assetValuesData/{asset.tickerSymbol}.csv', asset.id)
            print(f'Succesfully added asset values for: {asset}')
        except:
            print(f'Could not add asset values for: {asset}')