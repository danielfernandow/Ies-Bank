from bank.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Person(db.Model, SerializerMixin):
    person_id = db.Column(db.Integer, primary_key=True)
    adress_id = db.Column(db.Integer)
    account_id = db.Column(db.Integer)
    name = db.Column(db.String(256))
    password = db.Column(db.String(512))
    cpf = db.Column(db.String(14))
    birthdate = db.Column(db.DateTime)
    email = db.Column(db.String(128))


class Account(db.Model, SerializerMixin):
    account_id = db.Column(db.Integer, primary_key=True)
    account_status_id = db.Column(db.Integer)
    agency = db.Column(db.Integer)
    balance = db.Column(db.Float)


class AccountStatus(db.Model, SerializerMixin):
    account_status_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))


class Transaction(db.Model, SerializerMixin):
    transaction_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer)
    transaction_type_id = db.Column(db.Integer)
    transaction_status_id = db.Column(db.Integer)
    transactionDate = db.Column(db.DateTime)
    amount = db.Column(db.Float)


class TransactionStatus(db.Model, SerializerMixin):
    transaction_status_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))


class TransactionTipo(db.Model, SerializerMixin):
    transaction_type_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))


class Adress(db.Model, SerializerMixin):
    adress_id = db.Column(db.Integer, primary_key=True)
    telephone_id = db.Column(db.Integer)
    state_id = db.Column(db.Integer)
    city = db.Column(db.String(64))
    adress = db.Column(db.String(256))
    number = db.Column(db.String(32))
    district = db.Column(db.String(64))
    zipCode = db.Column(db.String(9))


class Telephone(db.Model, SerializerMixin):
    telephone_id = db.Column(db.Integer, primary_key=True)
    ddd = db.Column(db.String(3))
    number = db.Column(db.String(10))


class State(db.Model, SerializerMixin):
    state_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    initials = db.Column(db.String(2))
