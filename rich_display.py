from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

def show_round(round_num: int, responses: list, judgment: dict):
    console.print(f"\n[bold underline]ROUND {round_num}[/]")

    for r in responses:
        color = {
            "Visionary": "cyan", "Cynic": "red", "Engineer": "green",
            "Ethicist": "magenta", "Capitalist": "yellow"
        }.get(r['agent'], "white")
        console.print(f"[{color}]{r['agent']}:[/] {r['text']}")

    table = Table(title=f"Round {round_num} Scores", box=box.ROUNDED)
    table.add_column("Agent")
    table.add_column("Total")
    table.add_column("Justification")

    for name, data in judgment.get("scores", {}).items():
        table.add_row(name, str(data["total"]), data["justification"])

    console.print(table)
    console.print(f"[bold gold]Winner:[/] {judgment.get('winner', 'N/A')}")