# Day 033 - Append Files

#### 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand how to open a file in **append mode (`"a"`)**.
* Differentiate between **write mode (`"w"`)** and **append mode (`"a"`)**.
* Add data to the end of an existing file without deleting its original contents.
* Understand how append mode behaves when a file does not exist.
* Build a **System Log Book** project.

---

### The Append Mode (`"a"`)

In Day 032, you learned that opening a file in `"w"` mode can overwrite all existing content.

When you want to **add new data to the end of an existing file while preserving its original content**, you should use **append mode (`"a"`)**.

The `"a"` stands for **append**.

**Basic Syntax:**

```python
with open("example.txt", "a") as file:
    file.write("This line is appended to the end!\n")
```

---

### How `"a"` Mode Behaves

Append mode has two important behaviors.

#### 1. Creates a New File

If the specified file does not exist, Python automatically creates it.

```python
with open("new_file.txt", "a") as file:
    file.write("First entry\n")
```

After running the program, `new_file.txt` will exist.

---

#### 2. Preserves Existing Content

If the file already exists, Python preserves its existing contents and positions new writes at the end.

Suppose `example.txt` contains:

```text
Hello
```

Then:

```python
with open("example.txt", "a") as file:
    file.write("World\n")
```

The file becomes:

```text
Hello
World
```

The original content is not deleted.

---

### Write (`"w"`) vs. Append (`"a"`)

Understanding the difference between these two modes is extremely important.

Suppose a file already contains:

```text
Hello
```

#### Using `"w"`:

```python
with open("example.txt", "w") as file:
    file.write("World\n")
```

Result:

```text
World
```

The original `Hello` is replaced.

#### Using `"a"`:

```python
with open("example.txt", "a") as file:
    file.write("World\n")
```

Result:

```text
Hello
World
```

The original content remains untouched.

---

### Comparison Table

| Mode  | File Exists                 | File Does Not Exist | Existing Content |
| ----- | --------------------------- | ------------------- | ---------------- |
| `"w"` | Opens and overwrites        | Creates file        | ❌ Deleted        |
| `"a"` | Opens and writes at the end | Creates file        | ✅ Preserved      |

### Simple Rule

> `"w"` = **Replace**
> `"a"` = **Add**

---

### When Should You Use Append Mode?

Append mode is useful whenever information needs to accumulate over time.

Common examples include:

* System logs.
* Application logs.
* Diary entries.
* Activity histories.
* User-generated records.
* Event tracking.
* Transaction histories.
* Simple text-based databases.

For example, a logging system should usually **append** new events instead of replacing previous events.

---

### Newline Characters and Append Mode

When appending multiple entries, remember to include `\n`.

For example:

```python
with open("log.txt", "a") as file:
    file.write("First event\n")
    file.write("Second event\n")
```

The resulting file will be:

```text
First event
Second event
```

Without the newline:

```python
with open("log.txt", "a") as file:
    file.write("First event")
    file.write("Second event")
```

The result would be:

```text
First eventSecond event
```

---

### Append Mode and the File Pointer

When a file is opened using `"a"` mode, new data is written at the **end of the file**.

This makes append mode ideal for continuously adding information without having to manually find the end of the file.

```text
Existing Data
      ↓
-------------------
| Previous entries |
-------------------
          ↑
      New data
      is added here
```

---

### Reading and Appending

Basic `"a"` mode is intended for writing, not reading.

For example:

```python
with open("example.txt", "a") as file:
    file.write("New entry\n")
```

If you also need to read the file, you can close the append operation and reopen the file in read mode:

```python
with open("example.txt", "r") as file:
    content = file.read()
```

Python also provides `"a+"` mode for applications that need both reading and appending.

```python
with open("example.txt", "a+") as file:
    ...
```

However, `"a+"` has additional file-position behavior that you should understand before using it.

For today's lesson, keep the main focus on `"a"`.

---

### Exercises

#### Exercise 1

Open the `about_me.txt` file created on Day 032 using append mode.

Add the following sentence on a new line:

```text
PS: I am currently learning about file appending!
```

---

#### Exercise 2

Write a program that asks the user for **three items** and appends them to a file named `wishlist.txt`.

Requirements:

* Ask for three separate items.
* Append each item to the file.
* Place each item on a new line.
* Do not delete existing wishlist items.

---

#### Exercise 3

Create a script that checks whether `counter.txt` exists.

If it does not exist:

* Create it.
* Write the number `1`.

If it already exists:

* Read the last number.
* Increase it by `1`.
* Append the new number to the file.

---

### Mini Project: System Log Book

Create a **System Log Book** application.

The application should simulate a simple event-logging system that continuously adds events to a file named `system_log.txt`.

### Project Requirements

Your program should:

1. Display a **System Log Book** title.
2. Ask the user for a log level:

   * `INFO`
   * `WARNING`
   * `ERROR`
3. Ask the user for a short log message.
4. Validate that the log level and message are not empty.
5. Format the information into a structured log entry.
6. Open `system_log.txt` using **append mode (`"a"`)**.
7. Add the new log entry without deleting previous entries.
8. Display a confirmation message.
9. Read and display the current contents of the log file.

### Suggested Log Format

Each entry could follow a structure such as:

```text
[INFO] - Message: Application started
[WARNING] - Message: Low disk space
[ERROR] - Message: Database connection failed
```

### Suggested Project Structure

```text
system-log-book/
│
├── log_book.py
└── system_log.txt
```

> **Practice Requirement:** Implement the project yourself using the append-mode concepts learned today. The project solution code is intentionally not included in this note.

---

### Common Mistakes

#### ❌ Expecting to Read Files in `"a"` Mode

**Cause:** Trying to call `.read()` after opening a file using `"a"` mode.

```python
with open("example.txt", "a") as file:
    content = file.read()
```

Basic `"a"` mode is intended for writing and will raise an error if you attempt to read from it.

**Solution:**

Close the append operation and reopen the file in `"r"` mode when you need to read it.

Alternatively, Python provides `"a+"` mode for combined reading and appending.

---

#### ❌ Writing on the Same Line

**Cause:** The existing file does not end with a newline character.

For example, if the file contains:

```text
Hello
```

and you append:

```python
file.write("World")
```

the result may become:

```text
HelloWorld
```

**Solution:**

Include `\n` when writing entries:

```python
file.write("World\n")
```

When building logging systems, it is good practice to make sure every log entry ends with a newline.

---

#### ❌ Typing the Wrong Mode

**Cause:** Writing something like:

```python
open("file.txt", "append")
```

`"append"` is not a valid file mode.

**Solution:**

Use:

```python
open("file.txt", "a")
```

---

#### ❌ Confusing `"a"` with `"w"`

This is one of the most important mistakes to avoid.

```text
"w" → Deletes existing content and writes new content
"a" → Preserves existing content and adds new content
```

Always choose the mode based on whether existing data needs to be preserved.

---

#### ❌ Forgetting That `"a"` Creates Files

Some beginners assume the file must already exist.

It does not.

```python
with open("new_log.txt", "a") as file:
    file.write("First log\n")
```

If `new_log.txt` doesn't exist, Python creates it automatically.

---

### Summary

Today you learned how to:

* ✅ Open files using **append mode (`"a"`)**.
* ✅ Preserve existing file contents.
* ✅ Add new information to the end of a file.
* ✅ Understand the difference between `"w"` and `"a"`.
* ✅ Create a new file automatically using append mode.
* ✅ Use newline characters when adding multiple entries.
* ✅ Understand the basic purpose of `"a+"` mode.
* ✅ Build an append-based **System Log Book** application.

---

### Key Takeaways

* `"a"` stands for **append**.
* Append mode preserves existing file contents.
* If the file doesn't exist, `"a"` creates it automatically.
* New data is written at the end of the file.
* Use `"w"` when you intentionally want to replace existing content.
* Use `"a"` when you want to preserve existing content and add new data.
* Always consider using `\n` when appending separate entries.
* Append mode is especially useful for logs, diaries, histories, and other continuously growing files.
* Basic `"a"` mode is for writing; use `"r"` separately when you need to read the file.

---

### What's Next?

**Day 034 - Exceptions**
