
from flask import Blueprint, render_template
from src.consts import TEMPLATE_FOLDER

HomeBlueprint = Blueprint('home', __name__, template_folder=TEMPLATE_FOLDER)

@HomeBlueprint.route("/")
def IndexPage():
    return render_template('pages/home.html')