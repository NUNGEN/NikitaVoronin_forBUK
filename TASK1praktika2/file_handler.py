import os

def read_notes():
    notes = []
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:
                notes = content.split("\n---\n")
    return notes

def write_notes(notes):
    with open("notes.txt", "w", encoding="utf-8") as file:
        file.write("\n---\n".join(notes))

def add_note(title, text):
    notes = read_notes()
    note = f"Title: {title}\nText: {text}"
    notes.append(note)
    write_notes(notes)

def delete_note(title):
    notes = read_notes()
    notes = [note for note in notes if not note.startswith(f"Title: {title}")]
    write_notes(notes)