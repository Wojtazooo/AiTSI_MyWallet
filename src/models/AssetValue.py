from src import Database

class AssetValue(Database.Model):
  assetId = Database.Column(Database.Integer, Database.ForeignKey('asset.id'), primary_key=True)
  asset = Database.relationship("Asset", backref=Database.backref("asset_assetValue", uselist=False))
  timestamp = Database.Column(Database.DateTime, primary_key=True)
  openValue = Database.Column(Database.Numeric(precision=10, scale=2), nullable=False)
  closeValue = Database.Column(Database.Numeric(precision=10, scale=2), nullable=False)

  def __repr__(self):
    return f'<Asset Value timestamp={self.timestamp}, assetId={self.assetId}, open={self.openValue}, close={self.closeValue}>'
  
