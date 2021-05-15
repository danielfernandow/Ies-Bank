from flask import abort, jsonify
from flask_restful import Resource

from bank.models import Pessoa


class PessoatResource(Resource):
    def get(self):
        pessoa = Pessoa.query.all() or abort(204)
        return jsonify(
            {"products": [pessoa.to_dict() for pessoa in Pessoa]}
        )


class PessoaIdResource(Resource):
    def get(self, pessoa_id):
        pessoa = Pessoa.query.filter_by(id=pessoa_id).first() or abort(404)
        return jsonify(pessoa.to_dict())
