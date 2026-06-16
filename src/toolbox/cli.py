"""Console script for toolbox."""

import typer
from rich.console import Console

from toolbox import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for toolbox."""
    console.print("Replace this message by putting your code into toolbox.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
