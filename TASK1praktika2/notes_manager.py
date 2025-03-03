from file_handler import add_note, read_notes, delete_note

def add_note(title, text):
    add_note_to_file(title, text)
    print(f"Note titled '{title}' added successfully.")

def view_notes():
    notes = read_notes()
    if notes:
        print("\n--- All Notes ---")
        for note in notes:
            print(note)
            print("\n---")
    else:
        print("No notes available.")

def delete_note(title):
    notes = read_notes()
    if any(note.startswith(f"Title: {title}") for note in notes):
        delete_note(title)
        print(f"Note titled '{title}' deleted successfully.")
    else:
        print(f"No note found with the title '{title}'.")