from flask import Flask, request, jsonify, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
#import jwt
import datetime
from functools import wraps
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SKEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://bhaskara:danield5@localhost/aps'

db = SQLAlchemy(app)

@app.route('/')
def main():
    return 'aqui uma tela de entrada, talvez de login?'


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    data={
        'name': request.form.get('name'),
       'email' : request.form.get('email'),
        'password' : request.form.get('password'),
        'cpf' : request.form.get('cpf'),
        'birth' : request.form.get('birth')
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
        #['password'] = user.password
        'birth_date' : user.dataNascimento,
        'email': user.email
    }
    return 'tela detalhamento'


@app.route('/conta/<conta_id>', methods=['GET'])
def transfer():
    user = conta.query.filter_by(id=user.conta_id).first()
    balance_data={

    }
    
    return 'retorna saldo'

#funcao de banco
@app.route('/transfer/<id_user>', methods=['POST'])
def transfer_id(id_user):
    return 'transferir dinheiro/sacar da origem'

@app.route('/balance/<user_id>', methods=['GET'])
def balance_id(id_user):
    return 'saldo da usuario'

@app.route('/personal_data', methods=['GET'])
def personal_data():
    return 'template'

@app.route('/personal_data/<user_id>',  methods=['GET'])
def personal_data_id(user_id):
    return 'dados do usuario'


@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')


if __name__ == "__main__":
    app.run(port=8080, debug=True)