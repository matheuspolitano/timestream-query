import click
from timestream_query.cli.generate_file import generate_csv_command


@click.group()
def cli():
    """Command Line group for handling various commands."""
    pass


cli.add_command(generate_csv_command)

if __name__ == "__main__":
    cli()
