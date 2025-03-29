import click
from app.note_app import NoteApp

@click.group()
@click.pass_context
def cli(ctx):
    """Note Taking CLI Application."""
    ctx.obj = NoteApp()

@cli.command()
@click.argument("title")
@click.argument("content")
@click.pass_obj
def add(note_app: NoteApp, title: str, content: str):
    "Add a new note."
    try:
        result = note_app.add_note(title, content)
        click.echo(result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument("title")
@click.pass_obj
def delete(note_app: NoteApp, title: str):
    """Delete a note by title."""
    result = note_app.delete_notes(title)
    click.echo(result)
