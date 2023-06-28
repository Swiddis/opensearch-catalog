import click
from .diff import diff
from .scanviz import scanviz

@click.group()
def cli():
    """Utilities for developing OpenSearch Integrations."""
    pass


cli.add_command(diff)
cli.add_command(scanviz)


if __name__ == "__main__":
    cli()
