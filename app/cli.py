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

@cli.command(name="list")
@click.option("--page", default=1, help="Page number to view", type=int)
@click.option("--limit", default=5, help="Number of notes per page", type=int)
@click.pass_obj
def list_notes(note_app: NoteApp, page, limit):
    """List notes with pagination."""
    try:
        result = note_app.view_notes(page, limit)
        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {e}")
