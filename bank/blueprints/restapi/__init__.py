from flask import Blueprint
from flask_restful import Api

from .resources import PersonResource, PersonIdResource, PostUserResource

bp = Blueprint("restapi", __name__, url_prefix="/api")
api = Api(bp)


def init_app(app):
    api.add_resource(PersonResource, "/person/")
    api.add_resource(PersonIdResource, "/person/<person_id>")
    api.add_resource(PostUserResource, "/person/signup/")

    app.register_blueprint(bp)
