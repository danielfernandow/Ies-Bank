from bank.models import Person
from flask import Blueprint

from .views import person, person_id, hello, accounts, account_id

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=person)
bp.add_url_rule("/person/", view_func=person)
bp.add_url_rule("/person/<person_id>", view_func=person_id, endpoint="personview")
bp.add_url_rule("/account/", view_func=accounts)
bp.add_url_rule("/account/<account_id>", view_func=account_id, endpoint="accountView")



def init_app(app):
    app.register_blueprint(bp)