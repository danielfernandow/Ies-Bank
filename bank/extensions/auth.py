from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from bank.extensions.database import db
from bank.models import Pessoa


def verify_login(user):
    """Valida o usuario e senha para efetuar o login"""
    nome = user.get('nome')
    password = user.get('password')
    if not nome or not password:
        return False
    existing_user = Pessoa.query.filter_by(nome=nome).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False


def create_user(nome, password):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if Pessoa.query.filter_by(nome=nome).first():
        raise RuntimeError(f'{nome} ja esta cadastrado')
    user = Pessoa(nome=nome, password=generate_password_hash(password))
    db.session.add(Pessoa)
    db.session.commit()
    return user


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
