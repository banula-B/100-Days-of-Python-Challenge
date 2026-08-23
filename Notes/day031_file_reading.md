# Day 031 - File Reading

#### 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand how Python interacts with the file system.
* Open and close files safely using the **`with` statement** (Context Managers).
* Read file content using **`read()`**, **`readline()`**, and **`readlines()`**.
* Understand how to iterate through a file line-by-line.
* Build a **Diary Reader** project.

---

### Introduction to File Handling

In Python, **file handling** allows programs to interact with files stored on a computer.

Common file operations include:

1. **Open** the file.
2. **Process** the file by reading or writing data.
3. **Close** the file.

Python provides the built-in `open()` function for opening files.

**Basic Syntax:**

```python
file = open("filename.txt", "mode")
```

The `mode` determines what you want to do with the file.

Common modes include:

| Mode   | Purpose               |
| ------ | --------------------- |
| `"r"`  | Read from a file      |
| `"w"`  | Write to a file       |
| `"a"`  | Append data to a file |
| `"x"`  | Create a new file     |
| `"r+"` | Read and write        |

For today's lesson, the main focus is the **`"r"` read mode**.

---

### The Safe Way: Context Managers (`with`)

The recommended way to work with files is by using the **`with` statement**.

The `with` statement creates a **context manager** that automatically closes the file when the block finishes, even if an error occurs.

**Example:**

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

Once the `with` block ends, Python automatically closes the file.

This is safer than manually opening and closing files.

---

### Why Use `with`?

Using a context manager provides several advantages:

* Automatically closes the file.
* Prevents resources from remaining open.
* Makes code cleaner and easier to read.
* Helps prevent file-related resource leaks.
* Properly handles cleanup when errors occur.

**Recommended pattern:**

```python
with open("filename.txt", "r") as file:
    # Work with the file here
```

---

### Reading Files

Python provides several methods for reading file contents.

The most common methods are:

* `.read()`
* `.readline()`
* `.readlines()`

The best method depends on the amount and structure of data you need to process.

---

### 1. `.read()`

The `.read()` method reads the **entire content** of a file and returns it as a single string.

```python
with open("story.txt", "r") as file:
    content = file.read()
    print(content)
```

#### Best Used For

* Small text files.
* When you need the entire file content at once.

#### Important

For very large files, reading everything at once can consume a significant amount of memory.

---

### 2. `.readline()`

The `.readline()` method reads **one line at a time**.

Each time `.readline()` is called, the file position moves to the next line.

```python
with open("story.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()

    print("Line 1:", first_line.strip())
    print("Line 2:", second_line.strip())
```

#### Best Used For

* Reading specific lines.
* Processing a file sequentially.
* Situations where you don't need the entire file at once.

---

### 3. `.readlines()`

The `.readlines()` method reads all lines and returns them as a **list of strings**.

```python
with open("story.txt", "r") as file:
    all_lines = file.readlines()

print(all_lines)
```

For example, a file containing:

```text
Line 1
Line 2
```

may produce:

```python
["Line 1\n", "Line 2\n"]
```

The `\n` represents the newline character.

---

### 4. Iterating Line-by-Line

A file object can be directly used in a `for` loop.

This is often more **memory efficient** when working with large files because Python processes the file one line at a time.

```python
with open("large_file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

This approach avoids loading the entire file into memory.

---

### Comparing Reading Methods

| Method             | Returns            | Typical Use                         |
| ------------------ | ------------------ | ----------------------------------- |
| `.read()`          | One string         | Read the entire file                |
| `.readline()`      | One string         | Read one line                       |
| `.readlines()`     | List of strings    | Read all lines as a list            |
| `for line in file` | One line at a time | Efficient processing of large files |

---

### Understanding `.strip()`

When reading text files, lines often contain a newline character `\n`.

For example:

```python
"Hello World\n"
```

The `.strip()` method removes leading and trailing whitespace, including the newline character.

Example:

```python
line = "Hello World\n"
clean_line = line.strip()

print(clean_line)
```

Result:

```text
Hello World
```

This is especially useful when processing files line-by-line.

---

### File Position and the Read Pointer

When Python reads a file, it maintains a **file position** that indicates where the next read operation will begin.

For example:

```python
with open("example.txt", "r") as file:
    content = file.read()
```

After `.read()` finishes, the file position is at the **end of the file**.

If you attempt another read operation immediately, there may be nothing left to read.

You can reset the position using:

```python
file.seek(0)
```

The `0` moves the file position back to the beginning.

---

### File Paths

Python needs to know where the file is located.

For example:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

This looks for `data.txt` relative to the program's current working directory.

A project might look like:

```text
project/
│
├── main.py
└── data.txt
```

Running `main.py` from the project directory allows Python to find `data.txt` using the relative path.

---

### Exercises

#### Exercise 1

Create a plain text file named `sample.txt` containing a short paragraph.

Write a Python script using a context manager (`with`) to:

* Open the file.
* Read the entire file.
* Print its contents.

---

#### Exercise 2

Write a program that opens `sample.txt` and calculates:

* The total number of characters, including spaces.
* The total number of words.

---

#### Exercise 3

Write a script that reads a text file line-by-line and prints only the lines that start with the word **`"Note"`**, ignoring differences in capitalization.

---

### Mini Project: Diary Reader

Create a **Diary Reader** application that works with a text file named `diary.txt`.

The application should:

1. Check whether `diary.txt` exists.
2. Display an appropriate message if the file does not exist.
3. Open the diary safely using a context manager.
4. Read the diary entries.
5. Identify entries using a date marker such as `Date:`.
6. Display each diary entry with a clear header.
7. Count the total number of diary entries.

#### Suggested Diary Structure

Your `diary.txt` file could contain entries similar to:

```text
Date: 2026-08-23
Today I studied Python file handling.

Date: 2026-08-24
Today I practiced reading files.

Date: 2026-08-25
Today I learned about writing files.
```

#### Project Requirements

Your program should display:

* A title such as **Personal Diary Reader**.
* Each diary entry with an entry number.
* The contents of each entry.
* The total number of entries.
* A helpful message if `diary.txt` cannot be found.

> **Practice Requirement:** Implement the project yourself using the file-handling concepts learned today. The solution code is intentionally not included in this note.

---

### Common Mistakes

#### ❌ `FileNotFoundError`

**Cause:** Trying to read a file that does not exist or using an incorrect filename/path.

**Solution:**

* Check the filename carefully.
* Check the file extension.
* Make sure the file exists.
* Check your current working directory.
* Use the correct relative or absolute path.

---

#### ❌ Forgetting to Use `with`

**Cause:** Opening files manually and forgetting to close them.

For example:

```python
file = open("data.txt", "r")
```

If the file is not properly closed, system resources may remain occupied.

**Solution:**

Prefer:

```python
with open("data.txt", "r") as file:
    # Process file
```

The context manager handles closing automatically.

---

#### ❌ Reading the File Twice

**Cause:** Calling `.read()` and then trying another read method on the same file without resetting the file position.

For example:

```python
with open("data.txt", "r") as file:
    content = file.read()
    lines = file.readlines()
```

After `.read()`, the file position is already at the end.

**Solution:**

Either reopen the file or reset the position:

```python
file.seek(0)
```

---

#### ❌ Incorrect File Path

**Cause:** The Python script is running from a different directory than expected.

**Solution:**

Understand the difference between:

* The directory containing your Python file.
* The current working directory.
* Relative paths.
* Absolute paths.

---

#### ❌ Forgetting Newline Characters

Lines read from a text file often contain `\n`.

For example:

```text
Hello\n
```

Use `.strip()` when you need to remove surrounding whitespace and newline characters.

---

### Summary

Today you learned how to:

* ✅ Interact with files using Python's **`open()`** function.
* ✅ Understand common file modes.
* ✅ Safely manage files using **Context Managers (`with`)**.
* ✅ Read entire files using **`.read()`**.
* ✅ Read individual lines using **`.readline()`**.
* ✅ Read all lines as a list using **`.readlines()`**.
* ✅ Process large files efficiently using line-by-line iteration.
* ✅ Understand the file's current reading position.
* ✅ Work with file paths.
* ✅ Build a **Diary Reader** project.

---

### Key Takeaways

* The `open()` function is used to interact with files.
* The `"r"` mode is used for reading files.
* The `with` statement automatically closes files and is the recommended approach.
* Use `.read()` when you need the entire file.
* Use `.readline()` when you need to process one line at a time.
* Use `.readlines()` when you want all lines as a list.
* Iterating directly over a file is useful for processing large files efficiently.
* `.strip()` is useful for removing newline characters and surrounding whitespace.
* Incorrect file paths are one of the most common causes of file-reading errors.
* After reading to the end of a file, use `seek(0)` or reopen the file to read it again.

---

### What's Next?

**Day 032 - File Writing**
