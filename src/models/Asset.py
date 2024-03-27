from src import Database

class Asset(Database.Model):
  id = Database.Column(Database.Integer, primary_key=True)
  name = Database.Column(Database.String, primary_key=False)
  tickerSymbol = Database.Column(Database.String, primary_key=False) 

  def __repr__(self):
    return f'<Asset - {self.id}, {self.name} ({self.tickerSymbol})>'
  
def GetAssets():
  Database.Asset.Query()