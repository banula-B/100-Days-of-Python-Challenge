# Day 032 - File Writing

#### 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand how to open a file in **write mode (`"w"`)**.
* Write text data to a file using **`.write()`** and **`.writelines()`**.
* Understand the **destructive nature of `"w"` mode**.
* Understand how to create new files using Python.
* Convert non-string data types to strings before writing them.
* Build a **Note Saver** project.

---

### Writing to Files in Python

In Day 031, you learned how to **read** files. Today, you will learn how to **write** data to files.

Python uses the built-in `open()` function for writing files. The main difference is that we use **`"w"` mode**, where `"w"` stands for **write**.

**Basic Syntax:**

```python
with open("my_file.txt", "w") as file:
    file.write("Hello, World!")
```

Using the `with` statement ensures that the file is automatically closed after the writing operation is finished.

---

### Understanding `"w"` Mode

When you open a file using `"w"` mode, Python behaves in two important ways.

#### 1. Creates a New File

If the specified file does not exist, Python creates it automatically.

```python
with open("new_file.txt", "w") as file:
    file.write("This is a new file.")
```

After running the program, `new_file.txt` will be created.

---

#### 2. Overwrites Existing Content

If the file already exists, `"w"` mode **deletes its existing contents** before writing new data.

For example, suppose `data.txt` contains:

```text
Old information
Important information
```

If you run:

```python
with open("data.txt", "w") as file:
    file.write("New information")
```

The previous contents are replaced.

The resulting file contains:

```text
New information
```

> ⚠️ **Important:** Opening an existing file in `"w"` mode can cause permanent data loss.

---

### File Writing Modes

Python provides several modes for working with files:

| Mode   | Purpose                                            |
| ------ | -------------------------------------------------- |
| `"r"`  | Read an existing file                              |
| `"w"`  | Write and overwrite a file                         |
| `"a"`  | Append data to the end of a file                   |
| `"x"`  | Create a new file only if it doesn't already exist |
| `"r+"` | Read and write an existing file                    |

Today's focus is **`"w"` mode**.

---

### Methods for Writing Files

Python provides several ways to write data to a file.

The two important methods for today are:

* `.write()`
* `.writelines()`

---

### 1. `.write()`

The `.write()` method writes a **single string** to a file.

```python
with open("shopping.txt", "w") as file:
    file.write("Apples")
```

Unlike `print()`, `.write()` does **not automatically add a newline**.

For example:

```python
with open("shopping.txt", "w") as file:
    file.write("Apples")
    file.write("Bananas")
```

The file will contain:

```text
ApplesBananas
```

To place each item on a separate line, add `\n` manually:

```python
with open("shopping.txt", "w") as file:
    file.write("Apples\n")
    file.write("Bananas\n")
```

The result will be:

```text
Apples
Bananas
```

---

### 2. `.writelines()`

The `.writelines()` method writes multiple strings to a file.

It is useful when you already have a list of formatted strings.

```python
shopping_items = ["Apples\n", "Bananas\n", "Cherries\n"]

with open("shopping.txt", "w") as file:
    file.writelines(shopping_items)
```

The resulting file contains:

```text
Apples
Bananas
Cherries
```

### Important

`.writelines()` **does not automatically add newline characters**.

This:

```python
items = ["Apples", "Bananas", "Cherries"]
```

will produce:

```text
ApplesBananasCherries
```

Therefore, newline characters need to be included when separate lines are required.

---

### `.write()` vs `.writelines()`

| Method          | Input                    | Adds Newline Automatically? | Best Used For                     |
| --------------- | ------------------------ | --------------------------- | --------------------------------- |
| `.write()`      | Single string            | ❌ No                        | Writing individual pieces of text |
| `.writelines()` | List/iterable of strings | ❌ No                        | Writing multiple prepared strings |

---

### Writing Different Data Types

The `.write()` method expects a **string**.

This will cause an error:

```python
file.write(100)
```

The same applies to other non-string values:

```python
file.write(True)
```

To write these values, convert them to strings first:

```python
file.write(str(100))
```

Or:

```python
file.write(str(True))
```

You can also use formatted strings:

```python
age = 21

file.write(f"Age: {age}")
```

This is often more convenient when combining text with variables.

---

### Writing Multiple Lines

You can combine multiple pieces of information using newline characters.

```python
name = "Alice"
country = "Sri Lanka"
goal = "Become a Python Developer"

with open("about_me.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Country: {country}\n")
    file.write(f"Goal: {goal}\n")
```

The resulting file will contain:

```text
Name: Alice
Country: Sri Lanka
Goal: Become a Python Developer
```

---

### Exercises

#### Exercise 1

Write a Python script that opens a file called `about_me.txt` in write mode and saves:

* Your name.
* Your country.
* Your learning goal.

Each item should appear on a separate line.

---

#### Exercise 2

Given a list of numbers, write a script that:

1. Converts each number to a string.
2. Writes the numbers to `numbers.txt`.
3. Places each number on its own line.

---

#### Exercise 3

Write a program that:

1. Prompts the user to enter a sentence.
2. Checks whether the input is empty.
3. Saves the sentence to `user_input.txt` only if the input is not empty.

---

### Mini Project: Note Saver

Create a command-line **Note Saver** application.

The application should allow the user to:

1. Enter a title for a note.
2. Enter the note content.
3. Convert the title into a safe filename.
4. Create a text file based on the title.
5. Save the title and note content to the file.
6. Display a confirmation message after the note has been saved.

#### Suggested Project Structure

```text
note-saver/
│
├── note_saver.py
└── notes/
```

#### Project Requirements

Your application should:

* Ask the user for a note title.
* Ask the user for note content.
* Prevent empty titles from creating invalid files.
* Convert spaces in the title into underscores.
* Remove or avoid problematic filename characters.
* Save the note using `"w"` mode.
* Include the title inside the saved file.
* Display a success message after saving.

#### Example Output

```text
--- Welcome to Note Saver! ---

Enter a title for your note: Python Learning
Enter your note: Today I learned how to write files.

Note successfully saved!
```

> **Practice Requirement:** Implement the project yourself using today's file-writing concepts. The project solution code is intentionally not included in this note.

---

### Common Mistakes

#### ❌ Accidental Data Loss

**Cause:** Opening an existing file using `"w"` mode.

```python
with open("important.txt", "w") as file:
    ...
```

If `important.txt` already contains data, its contents are removed when the file is opened in write mode.

**Solution:**

Be careful when using `"w"` mode. If you want to add new information without deleting existing content, use **append mode (`"a"`)**.

---

#### ❌ Writing Non-String Data

**Cause:** Passing an integer, float, Boolean, or another non-string value directly to `.write()`.

For example:

```python
file.write(100)
```

This causes a `TypeError`.

**Solution:**

Convert the value to a string:

```python
file.write(str(100))
```

Or use an f-string:

```python
number = 100
file.write(f"{number}")
```

---

#### ❌ Forgetting Newlines

**Cause:** Calling `.write()` multiple times without adding `\n`.

```python
file.write("Line 1")
file.write("Line 2")
```

Result:

```text
Line 1Line 2
```

**Solution:**

Add `\n` when you want a new line:

```python
file.write("Line 1\n")
file.write("Line 2\n")
```

---

#### ❌ Confusing `"w"` and `"a"`

`"w"` **overwrites** the existing content.

`"a"` **adds** new content to the end.

```text
"w" → Replace existing content
"a" → Keep existing content and add new content
```

Understanding this difference is essential when working with persistent data.

---

### Summary

Today you learned how to:

* ✅ Open files using **write mode (`"w"`)**.
* ✅ Create new files using Python.
* ✅ Understand that `"w"` overwrites existing file contents.
* ✅ Use **`.write()`** to write individual strings.
* ✅ Use **`.writelines()`** to write multiple strings.
* ✅ Add newline characters using `\n`.
* ✅ Convert non-string data into strings before writing.
* ✅ Build a **Note Saver** command-line application.

---

### Key Takeaways

* `"w"` mode is used to write data to a file.
* `"w"` creates a file if it doesn't exist.
* `"w"` **overwrites existing content** if the file already exists.
* `.write()` writes a string to a file.
* `.writelines()` writes multiple strings to a file.
* Neither `.write()` nor `.writelines()` automatically adds newline characters.
* Use `\n` when you need separate lines.
* `.write()` requires string data, so convert other data types using `str()` or formatted strings.
* Always use the `with` statement when working with files.
* Use `"a"` instead of `"w"` when you need to preserve existing content and add new data.

---

### What's Next?

**Day 033 - Append Files**
