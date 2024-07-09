import click
import subprocess

@click.command()
@click.option('--os', type=click.Choice(['Windows', 'Linux'], case_sensitive=False),
              default=None, help='Option for installing on Windows or Linux')
def installdev(os):
    """Setup local DevOps development environment"""
    if os == 'Windows':
        click.echo("You've chosen Windows!")
    elif os == 'Linux':
        script_path = '/path/to/your/script.sh'  # Replace with your actual script path
        try:
            subprocess.run(['bash', script_path], check=True)
        except subprocess.CalledProcessError as e:
            click.echo(f"Error running Bash script: {e}")
    else:
        click.echo("Please specify a valid operating system (Windows or Linux).")
