import click


@click.command(name="new-tf-project")
@click.argument("project_type")
@click.argument("project_name")
def new_tf_project(project_type, project_name):
    """Create a new Terraform project."""
    click.echo(f"Would create Terraform project '{project_name}' of type '{project_type}'.")