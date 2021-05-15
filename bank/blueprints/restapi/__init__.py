from flask import Blueprint
from flask_restful import Api

from .resources import PessoatResource, PessoaIdResource

bp = Blueprint("restapi", __name__, url_prefix="/api/")
api = Api(bp)


def init_app(app):
    api.add_resource(PessoatResource, "/pessoa/")
    api.add_resource(PessoaIdResource, "/pessoa/<pessoa_id>")
    app.register_blueprint(bp)
