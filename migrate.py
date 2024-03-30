from datetime import datetime

import requests
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

def AddAssetValuesFromCsv(assets):
    for asset in assets:
        try:
            parse_csv_and_add_to_db(f'assetValuesData/{asset.tickerSymbol}.csv', asset.id)
            print(f'Succesfully added asset values for: {asset}')
        except:
            print(f'Could not add asset values for: {asset}')

def AddAssetValuesDirectlyFromStooq(assets):
    for asset in assets:
        try:
            url = f'https://stooq.pl/q/d/l/?s={asset.tickerSymbol}&i=d'
            response = requests.get(url)
            
            print(f'Sent request to = {url}, result = {response.status_code}');

            if(response.status_code >= 300 or response.status_code < 200):
                raise

            content = response.text.splitlines();

            for row in content[1:]:
                rowValues = row.split(',')
                asset_value = AssetValue(
                    assetId = asset.id,
                    timestamp=datetime.strptime(rowValues[0], '%Y-%m-%d').date(),
                    openValue=float(rowValues[1]),
                    closeValue=float(rowValues[4])
                )
                Database.session.add(asset_value)
            Database.session.commit()
            print(f'Succesfully added {len(content[1:])} asset values for: {asset}')
        except:
            print(f'Could not get asset values for: {asset}')
            raise

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

    #AddAssetValuesFromCsv(assets)
    AddAssetValuesDirectlyFromStooq(assets);
   