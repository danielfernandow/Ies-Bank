from flask import Blueprint

from .views import pessoa, pessoa_id

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=pessoa)
bp.add_url_rule(
    "/pessoa/<pessoa_id>", view_func=pessoa_id, endpoint="pessoaview")


def init_app(app):
    app.register_blueprint(bp)