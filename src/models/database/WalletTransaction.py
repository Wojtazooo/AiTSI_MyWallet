from sqlalchemy import text
from src import Database

class WalletTransaction(Database.Model):
  id = Database.Column(Database.Integer, primary_key=True)
  assetId = Database.Column(Database.Integer, Database.ForeignKey('asset.id'))
  asset = Database.relationship("Asset", backref=Database.backref("asset_walletTransaction", uselist=False))
  count = Database.Column(Database.Integer, nullable=False)
  timestamp = Database.Column(Database.DateTime, nullable=False)
  price = Database.Column(Database.Numeric(precision=10, scale=2), nullable=False)
  fees = Database.Column(Database.Numeric(precision=10, scale=2), nullable=True)

  def __repr__(self):
    return f'<WalletTransaction id={self.id}, timestamp={self.timestamp}, assetId={self.assetId}, count={self.count}>'

def GetWalletPositions():
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
                      MAX(timestamp),
                      closeValue as lastAssetCloseValue
                  FROM
                      asset_value
                  GROUP BY
                      assetId
              ) AV ON AV.assetId = A.id
          GROUP BY
              A.id,
              A.name
      );
      """
  print('fetching new walletPositions')

  walletPositions =  Database.session.execute(text(sql_query)).fetchall()

  return walletPositions




     
