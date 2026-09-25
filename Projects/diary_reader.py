from pathlib import Path

file_path = Path("../Resources/text files/diary.txt")

if not file_path.exists():
    print("File is not found. Please check the file path")

else:
    with open (file_path , "r") as file:
        contents = file.readlines()

    entry = []
    count = 0

    for content in contents:
        content = content.strip()

        if content.startswith("Date:"):
            
            if entry:
                print(f"========Diary Entry {count}========")

                for entry_line in entry:
                    print(f"{entry_line}")

                entry = []

            count+=1
            entry.append(content)

        elif content:
            entry.append(content)

    #Print full entry

    if entry:
        print(f"========Diary Entry {count}========")

        for entry_line in entry:
            print(f"{entry_line}")

    print(f"========Total Diary Entries: {count}========")