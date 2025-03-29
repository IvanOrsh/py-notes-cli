import pytest
from click.testing import CliRunner
from app.cli import cli
from tests.helpers import reset_storage

def test_add_note_command():
    """Test the CLI add command."""
    reset_storage()
    runner = CliRunner()
    result = runner.invoke(cli, [
        "add",
        "Test Title",
        "Test Content",
    ])
    assert result.exit_code == 0
    assert "Note added: Test Title - Test Content" in result.output

def test_delete_note_command():
    """Test the CLI delete command."""
    reset_storage()
    runner = CliRunner()
    runner.invoke(cli, [
        "add",
        "Delete Test",
        "Content for delete test",
    ])
    result = runner.invoke(cli, [
        "delete",
        "Delete Test",
    ])
    assert result.exit_code == 0
    assert "Note with title 'Delete Test' has been deleted." in result.output
