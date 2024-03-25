from src import Database

class Asset(Database.Model):
  id = Database.Column(Database.Integer, primary_key=True)
  name = Database.Column(Database.String, primary_key=False)

  def __repr__(self):
    return f'<Asset id={self.id} name={self.name}>'
  
def GetAssets():
  Database.Asset.Query()