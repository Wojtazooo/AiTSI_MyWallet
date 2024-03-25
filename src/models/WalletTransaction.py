from src import Database

class WalletTransaction(Database.Model):
  id = Database.Column(Database.Integer, primary_key=True)
  assetId = Database.Column(Database.Integer, Database.ForeignKey('asset.id'))
  asset = Database.relationship("Asset", backref=Database.backref("asset", uselist=False))
  count = Database.Column(Database.Integer, nullable=False)
  timestamp = Database.Column(Database.DateTime, nullable=False)
  price = Database.Column(Database.Numeric(precision=10, scale=2), nullable=False)
  fees = Database.Column(Database.Numeric(precision=10, scale=2), nullable=True)

  def __repr__(self):
    return f'<WalletTransaction id={self.id}, timestamp={self.timestamp}, assetId={self.assetId}, count={self.count}>'