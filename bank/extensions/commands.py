import click
from bank.extensions.database import db
from bank.extensions.auth import create_user


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--adress_id', '-a')
    @click.option('--account_id', '-ac')
    @click.option('--name', '-u')
    @click.option('--password', '-p')
    @click.option('--cpf', '-c')
    @click.option('--birthdate', '-b')
    @click.option('--email', '-e')
    def add_user(adress_id, account_id, name, password, cpf, birthdate, email):
        """Adds a new user to the database"""
        return create_user(adress_id, account_id, name, password, cpf, birthdate, email)
