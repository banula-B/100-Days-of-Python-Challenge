import os
print("--- Welcome to Note Saver! ---")

name = input("Please enter a title for your note: ").strip()

safe_title = "".join(
    c for c in name if c.isalnum() or c in (" ", "_")
).replace(" ", "_")

if not safe_title:
    print("Your name is not safe. Please try different!.")



else:
    notes_folder = "Projects/note_saver/notes" # Create the notes folder if it doesn't exist

    os.makedirs(notes_folder, exist_ok=True)

    file_name = f"{notes_folder}/{safe_title}.txt"

    print("Enter your note content below.")
    content = input("> ")

    with open(file_name,"w") as file:
        file.write(f"===={safe_title}====\n")
        file.write("")
        file.write(content +"\n")

print(f"\n✅ Note successfully saved to '{file_name}'!")