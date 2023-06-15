import typer
from rich import print
from rich.console import Console #consola.print
from rich.table import Table #tablas
from rich.prompt import Confirm #cuadro de confimación
from rich.style import Style #crear estilos como clases
from rich.theme import Theme #crear estylos englobados por tema
from rich.panel import Panel
from rich.text import Text

import time
from rich.progress import Progress

from os import system

system("clear")

danger_style = Style(color="red", blink=True, bold=True)
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}

def progreso () :

    with Progress() as progress:

        # task1 = progress.add_task("[red]Downloading...", total=1000)
        # task2 = progress.add_task("[green]Processing...", total=1000)
        task3 = progress.add_task("[cyan]Cooking...", total=1000)

        while not progress.finished:
            # progress.update(task1, advance=0.5)
            # progress.update(task2, advance=0.3)
            progress.update(task3, advance=10)
            time.sleep(0.02)

def main():
    progreso()
    panel = Panel(Text("Hello", justify="right"))
    print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))
    print(panel)
    console_theme = Console(theme=custom_theme)
    console_theme.print("This is information", style="info")
    console_theme.print("[warning]The pod bay doors are locked[/warning]")
    console_theme.print("Something terrible happened!", style="danger")

    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")
    #aplicación de estilos
    console = Console()
    console.print("Hello", style="#af00ff")
    console.print("DANGER!", style="red on white")
    console.print("Danger, Will Robinson!", style="blink bold red underline on white")
    console.print("foo [not bold]bar[/not bold] baz", style="bold")
    console.print("Google", style="link https://google.com")
    console.print("Danger, Will Robinson!", style=danger_style)
    #imprimir tablas
    table = Table("Name", "Item")
    table.add_row("Rick", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    print(table)
    print(Panel(table , title="Tabla en el panel", subtitle="total registros"))


    # validar_confirmacion = Confirm.ask("Esto es un cuadro de confimación?")
    # print("la confirmación es")
    # if validar_confirmacion:
    #     print(f"[green]{validar_confirmacion}[/green]")
    # else:
    #     print(f"[red]{validar_confirmacion}[/red]")


if __name__ == "__main__":
    typer.run(main)
