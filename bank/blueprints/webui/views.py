from flask import abort, render_template
from bank.models import Pessoa


def pessoa():
    pessoas = Pessoa.query.all()
    return render_template("pessoa.html", pessoas=pessoas)


def pessoa_id(pessoa_id):
    pessoa = Pessoa.query.filter_by(id=pessoa_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("pessoa_id.html", pessoa=pessoa)
