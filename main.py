import click
from timestream_query.client import TimeStreamQuery
from boto3.session import Session
from timestream_query.file import generate_csv, read_text_file


@click.command()
@click.option(
    "--sql_file", prompt="Path to the SQL file", help="The path to the SQL file."
)
@click.option(
    "--csv_file",
    prompt="Path for the output CSV file",
    help="The path for the output CSV file.",
)
@click.option(
    "--region",
    prompt="Region of the table",
    help="Region when creating new connections",
)
@click.option(
    "--aws-access-keid",
    default=None,
    help="AWS access key ID",
    show_default=True,
)
@click.option(
    "--aws-secret-access-key",
    default=None,
    help="AWS secret access key",
    show_default=True,
)
@click.option(
    "--aws-session-token",
    default=None,
    help="AWS temporary session token",
    show_default=True,
)
@click.option(
    "--delimiter", default=",", help="Delimiter for the CSV file.", show_default=True
)
def main(sql_file, csv_file,region,aws_access_key_id, aws_secret_access_key, aws_session_token  delimiter):
    """
    This script executes a SQL query from a file against Amazon Timestream and saves the result in a CSV file.
    """
    session = None
    if (aws_access_key_id is not None and aws_secret_access_key is not None and  aws_session_token is not None):
        session = Session(aws_access_key_id, aws_secret_access_key,aws_session_token )
    tsq = TimeStreamQuery(session, region=region)

    try:
        sql_query = read_text_file(sql_file)
    except FileNotFoundError:
        click.echo(f"Error: SQL file not found at {sql_file}")
        return

    try:
        timestream_result = tsq.execute_query(sql_query)
    except Exception as e:
        click.echo(f"Error executing query: {e}")
        return

    columns, data = timestream_result.get_columns_and_data()

    try:
        generate_csv(columns, data, path=csv_file, delimiter=delimiter)
        click.echo(f"CSV file generated successfully at {csv_file}")
    except Exception as e:
        click.echo(f"Error generating CSV file: {e}")


if __name__ == "__main__":
    main()
