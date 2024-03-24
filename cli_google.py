from typer import Typer
from googlesearch import search
from typing_extensions import Annotated
from rich import print as rprint

import subprocess
import typer

app_cli = Typer()


@app_cli.command("check")
def cli_hello():
    rprint("[white]This is a[/white] [blue bold]Python cli[/blue bold]")


class GoogleSearchAgent:
    def __init__(self, search_term, num_results):
        self.search_term = search_term
        self.num_results = num_results

    def get_results(self):
        search_results = search(self.search_term, self.num_results)

        return search_results


@app_cli.command("search")
def cli_google():
    search_query = typer.prompt("Enter search query")
    result_limit = typer.prompt("Enter result limit", type=int)
    
    google_agent = GoogleSearchAgent(search_query, result_limit)
    top_results = google_agent.get_results()
    print('______________________________')
    rprint(f"[bold]Top results[/bold]")
    for idx, result in enumerate(top_results, 1):
        rprint(f"[white]{idx}[/white] [blue bold]{result}[/blue bold]")
    
    open_browser = typer.confirm("Open link?")
    if open_browser:
        typer.launch(top_results[0])


@app_cli.command("list")
def list_func():
    subprocess.run(f"ls -l", shell=True)


if __name__ == "__main__":
    app_cli()
