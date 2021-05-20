from flask import abort, json, jsonify, request
from flask_restful import Resource
import json 

from bank.extensions.auth import create_user
from bank.models import Person

class PersonResource(Resource):
    def get(self):
        users = Person.query.all() or abort(204)
        return jsonify(
            {"Person": [user.to_dict() for user in users]}
        )


class PersonIdResource(Resource):
    def get(self, person_id):
        user = Person.query.filter_by(person_id=person_id).first() or abort(404)
        return jsonify(user.to_dict())

class PostUserResource(Resource):
    def post(self):
        user = request.get_json() #or abort(404)
        return create_user(user)

