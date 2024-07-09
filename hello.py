import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet')
def hello(name):
    """Greet the person specified by --name."""
    click.echo(f"Hello {name}!")
