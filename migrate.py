import datetime
from src.models.Asset import Asset
from src import App, Database
from src.models.WalletTransaction import WalletTransaction

with App.app_context():
    Database.drop_all();
    Database.create_all();

    Database.session.add(Asset(id=1, name='JSW'))
    Database.session.add(Asset(id=2, name='CD Projekt'))
    Database.session.add(Asset(id=3, name='PKO BP'))
    Database.session.add(Asset(id=4, name='PZU'))
    Database.session.add(Asset(id=5, name='Alior'))
    Database.session.add(Asset(id=6, name='PKN ORLEN'))

    Database.session.add(WalletTransaction(assetId=3, count=10,timestamp=datetime.datetime(2022, 9, 10, 11, 39, 00), price=12.32, fees=1.3))
    Database.session.add(WalletTransaction(assetId=3, count=8,timestamp=datetime.datetime(2022, 10, 13, 9, 10, 00), price=14.86, fees=1.3))
    Database.session.add(WalletTransaction(assetId=4, count=5,timestamp=datetime.datetime(2022, 10, 13, 9, 10, 00), price=67.12, fees=0.9))

    Database.session.commit()