import datetime
import json
import os

notes_file = "notes.json"

def load_notes():
    try:
      if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Returning empty list")
        return[]
    

def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=2)


def add_note(title, body):
    notes = load_notes()
    if notes is None:
        notes = []
    note_id = len(notes) + 1
    create_time = datetime.datetime.now().strftime("%H:%M %d:%m:%Y")
    note = {"id": note_id, "title": title, "body": body, "create_time": create_time}
    notes.append(note)
    save_notes(notes)


def delete_note(note_id):
    notes = load_notes()
    if notes is None:
        notes = []
        print("Empty file, nothing to delete!")
        return
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)


def edit_note(note_id, title, body):
    notes = load_notes()
    if notes is None or len(notes) == 0:
        print("File is empty. Nothing to edit")
        return
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["body"] = body
            note["edit_time"] = datetime.datetime.now().strftime("%H:%M %d:%m:%Y")
            break
    else: 
        print(f"Note with ID {note_id} not found!")
    save_notes(notes)


def view_notes():
    notes = load_notes()
    if not notes:
        print("Empty Notes file!")
    else:
        for note in notes:
            print(f"ID: {note['id']}; Title: {note['title']}; Time create: {note['create_time']}")
            print(f"Body: {note['body']}")
            if "edit_time" in note:
                print(f" Last edit: {note['edit_time']}")
            print("-"*40)
    

def main():

    while True:
        print("""
                MENU
              
            1 - Add Note
            2 - Delete Note
            3 - Edid Note
            4 - View Notes
            0 - Exit
              """)
        action = input("Enter your action (enter number): ")
        
        if action == "1":
            add_note(input("Enter note title: "), input("Enter body note: "))
        elif action == "2":
            delete_note(int(input("Enter note ID to delete: ")))
        elif action == "3":
            edit_note(int(input("Enter note ID to edit: ")), 
                      input("Enter new title note: "), 
                      input("Enter new body note: "))
        elif action == "4":
             view_notes()
        
        elif action == "0":
            print("Exiting...")
            break
        else:
            print("""
                  Invalid number!
                  Please, try again...
                  """)
            
if __name__ == "__main__":
    main()