import click
from flask import Flask, current_app
from app.db.db import get_db 
from flask.cli import with_appcontext

@click.command("init-db")
@with_appcontext
def init_db_command():

    db = get_db()
    click.echo("Initializing database")
    with current_app.open_resource(current_app.config["DATABASE_INIT"]) as f:
        db.executescript(f.read().decode("utf-8"))
    click.echo("Database initialized")


@click.command("create-db")
@with_appcontext
def create_db_command():

    click.echo("Creating database")
    path = current_app.config["DATABASE_URI"]
    click.echo(f"--> {path}")
    file = open(path,"w")
    file.close()
    click.echo("Database created")


def init_app(app:Flask):
    app.cli.add_command(init_db_command)
    app.cli.add_command(create_db_command)
    return app
