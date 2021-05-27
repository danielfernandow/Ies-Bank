from flask import Blueprint
from flask_restful import Api

from .resources import PersonResource, PersonIdResource, PostUserResource, PostAccountResource, GetAccountResource, GetAccountIdResource

bp = Blueprint("restapi", __name__, url_prefix="/api")
api = Api(bp)


def init_app(app):
    api.add_resource(PersonResource, "/person/")
    api.add_resource(PersonIdResource, "/person/<person_id>")
    api.add_resource(PostUserResource, "/person/post/")
    api.add_resource(GetAccountResource, "/account/get/")
    api.add_resource(PostAccountResource, "/account/post/")
    api.add_resource(GetAccountIdResource, "/account/get/<account_id>")



    app.register_blueprint(bp)
