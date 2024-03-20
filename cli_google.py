from typer import Typer
from googlesearch import search
from selenium import webdriver

from rich import print as rprint
import subprocess

google_cli = Typer()


@google_cli.command("check")
def cli_hello():
    rprint("[white]This is a[/white] [blue bold]Python cli[/blue bold]")


class GoogleSearchAgent:
    def __init__(self, search_term, num_results):
        self.search_term = search_term
        self.num_results = num_results

    def get_results(self):
        search_results = search(self.search_term, self.num_results)

        return search_results


@google_cli.command("search")
def cli_google():
    search_input = input("Enter search query: ")
    result_limit = int(input("How many results?"))
    google_agent = GoogleSearchAgent(search_input, result_limit)
    top_results = google_agent.get_results()

    print("Top results")
    for idx, result in enumerate(top_results, 1):
        rprint(f"[white]{idx}[/white] [blue bold]{result}[/blue bold]")


@google_cli.command("list")
def list_func():
    subprocess.run(f"ls -l", shell=True)

    

if __name__ == "__main__":
    google_cli()
