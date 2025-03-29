import os
import json

class NoteApp:
    def __init__(self):
        """Initialize the NoteApp."""
        self.notes = []

    def add_note(self, title, content):
        "Add a new note"
        note = {
            "title": title,
            "content": content,
        }
        self.notes.append(note)
        return f"Note added: {title}"
