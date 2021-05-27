from bank.extensions.auth import verify_login
from re import template

from flask.helpers import url_for
from bank.extensions.database import db
from flask import abort, render_template
from bank.models import Account, Person


def hello():
    return render_template('maintenance.html')


def person():
    users = Person.query.all()
    return render_template("person.html", users=users)


def person_id(person_id):
    user = Person.query.filter_by(person_id=person_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("person_id.html", user=user)


def accounts():
    accounts = Account.query.all()
    return render_template("accounts.html", accounts=accounts)


def account_id(account_id):
    account = Account.query.filter_by(account_id=account_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("account_id.html", account=account)


def maintenance():
    return render_template('maintenance.html')