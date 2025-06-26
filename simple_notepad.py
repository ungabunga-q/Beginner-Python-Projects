"""
Simple Notepad
Write and read notes from a file.
"""
def write_note():
    note = input("Write your note: ")
    with open("note.txt", "a") as f:
        f.write(note + "\n")
    print("Note saved!")

def read_notes():
    try:
        with open("note.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No notes found.")

if __name__ == "__main__":
    while True:
        print("1. Write Note\n2. Read Notes\n3. Exit")
        c = input("Choose: ")
        if c == '1':
            write_note()
        elif c == '2':
            read_notes()
        elif c == '3':
            break
        else:
            print("Invalid choice.")
