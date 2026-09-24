from pathlib import Path

file_path = Path("../Resources/text files/diary.txt")

if not file_path.exists():
    print("Diary file is not available.")
else:
    with open(file_path, "r") as file:
        lines = file.readlines()

    entry_count = 0
    current_entry = []

    for line in lines:
        line = line.strip()

        if line.startswith("Date:"):
            # Print the previous entry before starting a new one
            if current_entry:
                print("\n" + "=" * 40)
                print(f"Diary Entry {entry_count}")
                print("=" * 40)

                for entry_line in current_entry:
                    print(entry_line)

                current_entry = []

            entry_count += 1
            current_entry.append(line)

        elif line:
            current_entry.append(line)

    # Print the final entry
    if current_entry:
        print("\n" + "=" * 40)
        print(f"Diary Entry {entry_count}")
        print("=" * 40)

        for entry_line in current_entry:
            print(entry_line)

    print("\n" + "=" * 40)
    print(f"Total diary entries: {entry_count}")