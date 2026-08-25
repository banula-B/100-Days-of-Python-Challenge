import os

print("--- Welcome to Note Saver! ---")

title = input("Enter a title for your note: ").strip()

# Clean the title slightly so it's a safe filename
safe_title = "".join(
    c for c in title if c.isalnum() or c in (" ", "_")
).replace(" ", "_")

if not safe_title:
    print("Invalid title. Note creation cancelled.")
else:
    # Directory where notes will be saved
    # if you dont need to change the directory from default, remove this.
    notes_directory = r"Projects\day32\notes" # Change as you need

    # Create the full file path 
    filename = os.path.join(notes_directory, f"{safe_title}.txt")
    #if the file directory is default:
    # filename = f"{safe_title}.txt" 

    # Step 2: Get the note content
    print("\nType your note below. Press Enter to complete.")
    content = input("> ")

    # Step 3: Write the note to the file
    with open(filename, "w") as file:
        file.write(f"Title: {safe_title}\n")
        file.write("=============================\n")
        file.write(content + "\n")

    print(f"\n✅ Note successfully saved to '{filename}'!")