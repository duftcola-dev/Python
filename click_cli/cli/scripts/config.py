import click

@click.command()
def config():
    click.echo("Show config")

@click.command()
def load_config():
    click.echo("Load configuration")
    
@click.command()
def reset_config():
    click.echo("Set a new project configuration")