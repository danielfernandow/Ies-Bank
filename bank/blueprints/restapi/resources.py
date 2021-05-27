from flask import abort, json, jsonify, request
from flask_restful import Resource
from bank.extensions.database import db

from bank.extensions.auth import create_user
from bank.models import Account, Person

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
        data = request.get_json()
        return create_user(data)


class GetAccountResource(Resource):
    def get(self):
        accounts = Account.query.all() or abort(404)
        return jsonify(
            {"Account": [account.to_dict() for account in accounts]}
        )

class PostAccountResource(Resource):
    def post(self):
        data = request.get_json()
        account = Account(account_status_id=data.get('account_status_id'), agency=data.get('agency'), balance=data.get('balance'))
        db.session.add(account)
        db.session.commit()
        return jsonify({"Created":
            data})


class GetAccountIdResource(Resource):
    def get(self):
        data = request.get_json()
        account = Account.query.filter_by(account_id=data.get('account_id')).first() or abort(404)
        return jsonify(account.to_dict())

