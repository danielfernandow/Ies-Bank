from bank.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Transacao_Status(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))


class Transacao_Tipo(db.Model, SerializerMixin):
    tipo = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))


class Transacao(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    conta_id = db.Column(db.Integer)
    tipo = db.Column(db.Integer)
    status = db.Column(db.Integer)
    data = db.Column(db.DateTime)
    valor = db.Column(db.Float)


class Pessoa(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    endereco_id = db.Column(db.Integer)
    conta_id = db.Column(db.Integer)
    nome = db.Column(db.String(30))
    cpf = db.Column(db.String(14))
    dataNascimento = db.Column(db.DateTime)
    email = db.Column(db.String(40))
    password = db.Column(db.String(80))


class Conta(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    agencia = db.Column(db.Integer)
    saldo = db.Column(db.Float)


class Endereco(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    telefone_id = db.Column(db.Integer)
    estado_id = db.Column(db.Integer)
    municipio = db.Column(db.String(25))
    endereco = db.Column(db.String(50))
    numero = db.Column(db.String(5))
    complemento = db.Column(db.String(30))
    bairro = db.Column(db.String(20))
    cep = db.Column(db.String(9))


class Conta_Status(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))


class telefone(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    ddd = db.Column(db.String(5))
    numero = db.Column(db.String(10))


class estado(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    sigla = db.Column(db.String(2))
