from app.note_app import NoteApp

def test_add_note():
    app = NoteApp(use_memory=True)
    result = app.add_note("Test", "This is a test")
    assert result == "Note added: Test - This is a test"

def test_delete_note_success():
    app = NoteApp(use_memory=True)
    app.add_note("Test Title", "Test Content")
    result = app.delete_notes("Test Title")
    assert result == "Note with title 'Test Title' has been deleted."

def test_delete_note_failure():
    app = NoteApp(use_memory=True)
    result = app.delete_notes("Test Not Found")
    assert result == "Note with title 'Test Not Found' not found."

def test_view_notes_empty():
    app = NoteApp(use_memory=True)
    result = app.view_notes()
    assert "No notes found. Total pages: 0." in result
