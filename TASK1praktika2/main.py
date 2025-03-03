from notes_manager import add_note, view_notes, delete_note

def display_menu():
    print("1) Add a note")
    print("2) View all notes")
    print("3) Delete a note")
    print("4) Exit")
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            title = input("Enter note title: ")
            text = input("Enter note text: ")
            add_note(title, text)
        elif choice == "2":
            view_notes()
        elif choice == "3":
            title = input("Enter the title of the note to delete: ")
            delete_note(title)
        elif choice == "4":
            print("Operation end")
            break
        else:
            print("Please try again.")