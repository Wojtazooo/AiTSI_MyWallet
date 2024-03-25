
from flask import Blueprint, render_template
from src.consts import TEMPLATE_FOLDER

UserProfileBlueprint = Blueprint('userProfile', __name__, template_folder=TEMPLATE_FOLDER)

@UserProfileBlueprint.route("/user-profile")
def UserProfilePage():
    return render_template('pages/user-profile.html')
