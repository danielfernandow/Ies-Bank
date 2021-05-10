from flask import Flask, request, jsonify, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
# import jwt
import datetime
from functools import wraps
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SKEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://bhaskara:danield5@localhost/aps'

db = SQLAlchemy(app)


class Transacao_Status(db.Model):
    id = db.Column(db.Integer)
    descricao = db.Column(db.String(50))


class Transacao_Tipo(db.Model):
    tipo = db.Column(db.Integer)
    descricao = db.Column(db.String(50))


class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conta_id = db.Column(db.Integer)
    tipo = db.Column(db.Integer)
    status = db.Column(db.Integer)
    data = db.Column(db.DateTime)
    valor = db.Column(db.Float)


class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endereco_id = db.Column(db.Integer)
    conta_id = db.Column(db.Integer)
    nome = db.Column(db.String(30))
    cpf = db.Column(db.String(14))
    dataNascimento = db.Column(db.DateTime)
    email = db.Column(db.String(40))


class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    agencia = db.Column(db.Integer)
    saldo = db.Column(db.Float)


class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telefone_id = db.Column(db.Integer)
    estado_id = db.Column(db.Integer)
    municipio = db.Column(db.String(25))
    endereco = db.Column(db.String(50))
    numero = db.Column(db.String(5))
    complemento = db.Column(db.String(30))
    bairro = db.Column(db.String(20))
    cep = db.Column(db.String(9))


class Conta_Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))


class telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ddd = db.Column(db.String(5))
    numero = db.Column(db.String(10))


class estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    sigla = db.Column(db.string(2))


@app.route('/')
def main():
    return 'aqui uma tela de entrada, talvez de login?'


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    data = {
        'name': request.form.get('name'),
<<<<<<< HEAD
       'email' : request.form.get('email'),
        'password' : request.form.get('password'),
        'cpf' : request.form.get('cpf'),
        'birth' : request.form.get('birth')
=======
        'email': request.form.get('email'),
        'password': request.form.get('password'),
        'cpf': request.form.get('cpf'),
        'birth': request.form.get('birth')

>>>>>>> 0874d48633f71b70e281f7b736be80aa1b9cfbc6
    }
    #post in /conta
    
    return render_template('signup.html')


@app.route('/user/<pessoa_id>', methods=['GET'])
def show_details_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({'message': 'no user found.'})
    pass

    user_data = {
        'id': user.id,
        'name': user.nome,
        'cpf': user.cpf,
        # ['password'] = user.password
        'birth_date': user.dataNascimento,
        'email': user.email
    }
    return 'tela detalhamento'


@app.route('/conta/<conta_id>', methods=['GET'])
def transfer():
<<<<<<< HEAD
    user = conta.query.filter_by(id=user.conta_id).first()
    balance_data={
=======
    user = conta.query.filter_by(id=user_id).first()
    balance_data = {
>>>>>>> 0874d48633f71b70e281f7b736be80aa1b9cfbc6

    }

    return 'retorna saldo'


# funcao de banco
@app.route('/transfer/<id_user>', methods=['POST'])
def transfer_id(id_user):
    return 'transferir dinheiro/sacar da origem'


@app.route('/balance/<user_id>', methods=['GET'])
def balance_id(id_user):
    return 'saldo da usuario'


@app.route('/personal_data', methods=['GET'])
def personal_data():
    return 'template'


@app.route('/personal_data/<user_id>', methods=['GET'])
def personal_data_id(user_id):
    return 'dados do usuario'


@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')


if __name__ == "__main__":
    app.run(port=8080, debug=True)
