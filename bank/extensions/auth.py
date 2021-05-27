from flask.json import jsonify
from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from bank.extensions.database import db
from bank.models import Person

def verify_login(user):
    """Valida o cpf e senha para efetuar o login"""
    cpf = user.get('cpf')
    password = user.get('password')
    if not cpf or not password:
        return False
    existing_user = Person.query.filter_by(cpf=cpf).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False


def create_user(data):
    #data = json.loads(data)
    if Person.query.filter_by(cpf=data.get('cpf')).first():
       raise RuntimeError(f"{data.get('cpf')} always registred")
    user1 = Person(adress_id=3, account_id=1, name=data.get('name'), password=generate_password_hash(data.get('password')), cpf=data.get('cpf'), birthdate=data.get('birthdate'), email=data.get('email'))
    db.session.add(user1)
    db.session.commit()
    return jsonify({
        "Created": data
    })

def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
