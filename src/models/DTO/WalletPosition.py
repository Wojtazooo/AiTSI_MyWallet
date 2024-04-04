from sqlalchemy import text
from src import Database
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
  walletPositions =  Database.session.execute(text(sql_query)).fetchall()

  return walletPositions

