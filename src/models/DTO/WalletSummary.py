import decimal
from src.models.database.WalletTransaction import GetWalletPositions

class WalletSummary:
    def __init__(self, totalGain: decimal, totalWalletValue: decimal) -> None:
        self.totalGain = totalGain
        self.totalWalletValue = totalWalletValue
    def __str__(self) -> str:
       return f"{self.totalGain}, {self.totalWalletValue}"

def GetWalletSummary() -> WalletSummary:
  walletPositions = GetWalletPositions()
  totalGain = sum(position.assetGain for position in walletPositions)
  totalWalletValue = sum(position.currentAssetWorth for position in walletPositions)

  return WalletSummary(totalGain=totalGain, totalWalletValue=totalWalletValue)
