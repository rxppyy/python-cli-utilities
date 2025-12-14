notepad_txt = "data/notepad.txt"

def addnote(note_input):
    with open(notepad_txt, "a") as file:
        file.write(f"-- {note_input}\n")

def read_notes():
    with open(notepad_txt, "r") as file:
        content = file.read()
    return content.strip()

def clear_notes():
    with open(notepad_txt, "w") as file:
        file.write("")
