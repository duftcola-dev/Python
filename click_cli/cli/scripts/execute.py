import click

@click.command()
def execute():
    result = click.echo("executing command")
    print(result)

