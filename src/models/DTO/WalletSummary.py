import decimal

from src.models.DTO.WalletPosition import GetWalletPositions

class WalletSummary:
    def __init__(self, totalGain: decimal, totalWalletValue: decimal, totalGainPercentage: decimal) -> None:
        self.totalGain = totalGain
        self.totalWalletValue = totalWalletValue
        self.totalGainPercentage = totalGainPercentage
    def __str__(self) -> str:
       return f"{self.totalGain}, {self.totalWalletValue}"

def GetWalletSummary() -> WalletSummary:
  walletPositions = GetWalletPositions()
  totalGain = sum(position.assetGain for position in walletPositions)
  totalWalletValue = sum(position.currentAssetWorth for position in walletPositions)

  totalGainPercentage = 0

  if(totalWalletValue != 0):
    totalGainPercentage = totalGain * 100 / totalWalletValue

  return WalletSummary(totalGain=totalGain, totalWalletValue=totalWalletValue, totalGainPercentage=totalGainPercentage)
