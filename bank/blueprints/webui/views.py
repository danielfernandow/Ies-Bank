from re import template

from flask.helpers import url_for
from bank.extensions.database import db
from flask import abort, render_template, request
from bank.models import Person


def person():
    users = Person.query.all()
    return render_template("person.html", users=users)


def person_id(person_id):
    user = Person.query.filter_by(person_id=person_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("person_id.html", user=user)

def signin():
    return render_template("signin.html")

def signup():
    return render_template("signup.html")
