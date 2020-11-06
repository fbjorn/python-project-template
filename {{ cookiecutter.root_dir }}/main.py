import typer

app = typer.Typer()


@app.command()
def main():
    print("Hello world")


if __name__ == "__main__":
    app()
