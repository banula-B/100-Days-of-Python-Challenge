# Day 036 - JSON (Settings Manager)

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand what **JSON** is and why it is a standard format for data exchange.
* Import Python's built-in **`json`** module.
* Convert Python dictionaries to JSON strings and files using **`json.dumps()`** and **`json.dump()`** (Serialization).
* Parse JSON back into Python dictionaries using **`json.loads()`** and **`json.load()`** (Deserialization).
* Build a reusable **Settings Manager** project to save and load user preferences.

---

## What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight, text-based format used to store and transport data.

It is language-independent, but its structure is very similar to **Python dictionaries**, using key-value pairs.

Because of this similarity, working with JSON in Python is straightforward.

### JSON and Python Data Types

| JSON Data Type | Python Equivalent | Example               |
| -------------- | ----------------- | --------------------- |
| Object         | Dictionary        | `{"key": "value"}`    |
| Array          | List              | `["apple", "banana"]` |
| String         | String            | `"Hello"`             |
| Number         | Integer / Float   | `42` / `3.14`         |
| Boolean        | Boolean           | `true` / `false`      |
| Null           | None              | `null`                |

> **Important:** JSON uses lowercase `true`, `false`, and `null`, while Python uses `True`, `False`, and `None`.

---

# Python to JSON — Serialization

Converting a Python object into JSON data is called **serialization** or **encoding**.

Python's built-in `json` module provides several functions for working with JSON.

```python
import json
```

---

## 1. `json.dumps()`

The `s` in `dumps` stands for **string**.

`json.dumps()` converts a Python object into a JSON **string**.

### Example

```python
import json

user_data = {
    "username": "coder123",
    "is_active": True,
    "points": 150
}

json_string = json.dumps(user_data, indent=4)

print(json_string)
```

### Output

```text
{
    "username": "coder123",
    "is_active": true,
    "points": 150
}
```

The `indent=4` argument makes the JSON easier for humans to read.

---

## 2. `json.dump()`

`json.dump()` serializes a Python object and writes it **directly to a file**.

### Example

```python
with open("user.json", "w") as file:
    json.dump(user_data, file, indent=4)
```

This creates a `user.json` file containing the dictionary as JSON data.

### Important Difference

| Function       | Works With | Purpose                     |
| -------------- | ---------- | --------------------------- |
| `json.dumps()` | String     | Python object → JSON string |
| `json.dump()`  | File       | Python object → JSON file   |

---

# JSON to Python — Deserialization

Converting JSON data back into a Python object is called **deserialization** or **decoding**.

---

## 1. `json.loads()`

The `s` in `loads` stands for **string**.

`json.loads()` takes a JSON string and converts it into a Python object, usually a dictionary or list.

### Example

```python
raw_json = '{"name": "Alice", "age": 25, "languages": ["Python", "JS"]}'

python_dict = json.loads(raw_json)

print(python_dict["languages"])
```

### Output

```text
['Python', 'JS']
```

---

## 2. `json.load()`

`json.load()` reads JSON data **directly from an open file** and converts it into a Python object.

### Example

```python
with open("user.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data["username"])
```

### Important Difference

| Function       | Works With | Purpose                     |
| -------------- | ---------- | --------------------------- |
| `json.loads()` | String     | JSON string → Python object |
| `json.load()`  | File       | JSON file → Python object   |

---

# `dump` vs `dumps` vs `load` vs `loads`

This is one of the most important things to remember.

| Function       | Direction     | Source / Destination |
| -------------- | ------------- | -------------------- |
| `json.dumps()` | Python → JSON | String               |
| `json.dump()`  | Python → JSON | File                 |
| `json.loads()` | JSON → Python | String               |
| `json.load()`  | JSON → Python | File                 |

### Easy Memory Trick

The **`s` means string**:

* `dump()` → File
* `dumps()` → String
* `load()` → File
* `loads()` → String

---

# Working with JSON Files

JSON is especially useful for storing application data and configuration.

For example, a settings file might contain:

```json
{
    "theme": "dark",
    "volume": 80,
    "notifications_enabled": true
}
```

Python can load this JSON file into a dictionary:

```python
with open("settings.json", "r") as file:
    settings = json.load(file)
```

The resulting Python object can then be accessed like a normal dictionary:

```python
print(settings["theme"])
print(settings["volume"])
```
---

# Handling Missing or Invalid JSON Files

When working with real applications, JSON files may:

* Not exist.
* Be empty.
* Contain invalid JSON.
* Become corrupted.
* Contain unexpected data.

Python provides exceptions that can be handled using `try` and `except`.

### Example

```python
try:
    with open("settings.json", "r") as file:
        settings = json.load(file)

except FileNotFoundError:
    print("Settings file does not exist.")

except json.JSONDecodeError:
    print("Settings file contains invalid JSON.")
```

This prevents the program from crashing when the file cannot be loaded correctly.

---

# Exercises

## Exercise 1

Create a Python dictionary representing a book with the following keys:

* `title`
* `author`
* `genres` — a list
* `available` — a boolean

Convert the dictionary into a JSON string using `json.dumps()` with an indent of **2 spaces**, and print it.

---

## Exercise 2

Given the JSON string:

```json
{"item": "Laptop", "price": 999.99, "in_stock": true}
```

Write a Python program that:

1. Deserializes the JSON string.
2. Applies a **10% discount** to the price.
3. Updates the dictionary.
4. Prints the updated dictionary.

---

## Exercise 3

Write a program that attempts to open a file called `high_scores.json`.

If the file does not exist:

1. Catch the `FileNotFoundError`.
2. Create a default high-score dictionary:

```python
{"Player1": 100}
```

3. Save the default data to `high_scores.json`.

---

# Mini Project: Settings Manager

## Project Overview

Build a **Settings Manager** that stores and manages application preferences using a JSON file.

The application should use a file named:

```text
settings.json
```

The program should be able to remember user preferences between program runs.

---

## Project Requirements

Your Settings Manager should:

1. Check whether `settings.json` exists.
2. Load existing settings if the file is available.
3. Use default settings when the file does not exist.
4. Handle invalid or corrupted JSON data.
5. Allow the user to modify settings.
6. Save updated settings back to the JSON file.
7. Use functions to keep the program organised.

---

## Suggested Default Settings

Your application can include settings such as:

```text
theme
volume
notifications_enabled
auto_save_interval
```

Example configuration:

```json
{
    "theme": "dark",
    "volume": 80,
    "notifications_enabled": true,
    "auto_save_interval": 10
}
```

---

## Skills Practiced

This project gives you practice with:

* `json`
* `json.dump()`
* `json.load()`
* Dictionaries
* File reading
* File writing
* `try` / `except`
* `FileNotFoundError`
* `JSONDecodeError`
* Functions
* User input
* Data persistence

---

# Common Mistakes

## ❌ Confusing `dump()` / `load()` with `dumps()` / `loads()`

### Cause

Trying to use:

```python
json.dump(my_dict)
```

without providing a file object.

### Solution

Remember:

> **The `s` stands for string.**

* `dump()` → Files
* `dumps()` → Strings
* `load()` → Files
* `loads()` → Strings

---

## ❌ Using Single Quotes in JSON

### Cause

Writing JSON like:

```python
json.loads("{'name': 'Bob'}")
```

This produces a `JSONDecodeError` because single quotes are not valid JSON syntax.

### Solution

JSON requires **double quotes** for keys and string values:

```json
{"name": "Bob"}
```

---

## ❌ Using Python Boolean Values Directly in Raw JSON

Python uses:

```python
True
False
None
```

JSON uses:

```json
true
false
null
```

For example, this is valid JSON:

```json
{
    "active": true
}
```

But this is not valid JSON:

```json
{
    "active": True
}
```

---

## ❌ Attempting to Serialize Unsupported Data Types

Not every Python object can automatically be converted into JSON.

For example, a Python `set` cannot be directly serialized using the standard JSON encoder.

### Solution

Convert unsupported data into JSON-compatible structures first.

For example:

```python
numbers = {1, 2, 3}

json_data = list(numbers)
```

You can then serialize the resulting list.

---

## ❌ Forgetting File Modes

When working with JSON files, use the appropriate file mode:

```python
"r"
```

for reading and:

```python
"w"
```

for writing.

Remember that `"w"` can overwrite the existing file.

---

# Summary

Today you learned how to:

* ✅ Understand the structure and purpose of **JSON**.
* ✅ Import Python's built-in **`json`** module.
* ✅ Convert Python objects into JSON strings using `json.dumps()`.
* ✅ Save Python objects directly to JSON files using `json.dump()`.
* ✅ Convert JSON strings back into Python objects using `json.loads()`.
* ✅ Read JSON files using `json.load()`.
* ✅ Handle missing and corrupted JSON files.
* ✅ Understand the difference between serialization and deserialization.
* ✅ Build a **Settings Manager** concept for storing application preferences.

---

# Key Takeaways

* **JSON** is a lightweight and widely used format for storing and exchanging structured data.
* Python dictionaries and JSON objects have very similar structures.
* **Serialization** converts Python data into JSON.
* **Deserialization** converts JSON data back into Python objects.
* `dump()` and `load()` are primarily used with **files**.
* `dumps()` and `loads()` are used with **strings**.
* `indent=4` makes JSON files easier for humans to read.
* JSON is commonly used for **configuration files, APIs, data storage, and application settings**.
* Always handle possible errors when loading external JSON files.

---

# What's Next?

## Day 037 - CSV Files

In the next lesson, you will learn how to work with **CSV (Comma-Separated Values)** files and process tabular data using Python.
