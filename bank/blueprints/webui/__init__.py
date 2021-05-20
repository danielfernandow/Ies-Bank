from bank.models import Person
from flask import Blueprint

from .views import person, person_id, signin, signup

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=person)
bp.add_url_rule("/person/<person_id>", view_func=person_id, endpoint="personview")
bp.add_url_rule("/signin/", view_func=signin)
bp.add_url_rule("/signup/", view_func=signup)

def init_app(app):
    app.register_blueprint(bp)