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
    return render_template('signup.html')

@app.route('/ok', methods=['GET'])
def show_details():
    return 'tela detalhamento'

@app.route('/ok/<user_id>', methods=['GET'])
def show_details_id(user_id):
    return 'tela detalhamento'

@app.route('/transfer', methods=['GET'])
def transfer():
    return 'transferir dinheiro/sacar da origem'

@app.route('/transfer/<id_user>', methods=['POST'])
def transfer_id(id_user1):
    return 'transferir dinheiro/sacar da origem'

@app.route('/balance', methods=['GET'])
def balance():
    return 'saldo da usuario'

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