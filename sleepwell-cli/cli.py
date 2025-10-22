# sleepwell-cli/cli.py
import click
from sleepwell_cli.suggestion import generate_suggestion

@click.command()
@click.argument('query')
def main(query):
    """CLI for generating suggestions based on a user query."""
    suggestion = generate_suggestion(query)
    click.echo(suggestion)

if __name__ == '__main__':
    main()