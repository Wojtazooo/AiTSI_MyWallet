from src import App, Database

with App.app_context():
    Database.create_all();