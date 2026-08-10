# Day 018 - Dictionaries

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand the concept of **key-value pairs**.
- Create and access data in a **Dictionary**.
- Modify, add, and remove dictionary items.
- Use dictionary methods such as `.get()`, `.keys()`, `.values()`, and `.items()`.
- Build a **Phone Book** project to store and retrieve contact information.

---

# 📚 What is a Dictionary?

A **dictionary** is a built-in Python data type used to store data in **key-value pairs**.

Unlike lists, which use numerical indexes to access items, dictionaries use **keys** to retrieve values.

### Basic Syntax

Dictionaries are created using curly brackets `{}`.

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
```

In this example:

- `"name"` is a key.
- `"Alice"` is its value.
- `"age"` is a key.
- `20` is its value.

The general structure is:

```text
key: value
```

---

# 🔑 Accessing Dictionary Data

You can access a value by referring to its key.

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

print(student["name"])
```

Output:

```text
Alice
```

### Using `.get()`

If you try to access a key that doesn't exist using square brackets, Python raises a `KeyError`.

```python
print(student["grade"])
```

A safer approach is to use `.get()`:

```python
print(student.get("grade", "Not Found"))
```

Output:

```text
Not Found
```

---

# ✏️ Modifying and Adding Items

Dictionaries are **mutable**, meaning you can change them after they are created.

### Modifying an Existing Value

```python
student = {
    "name": "Alice",
    "age": 20
}

student["age"] = 21
```

The value of `"age"` is now `21`.

### Adding a New Key-Value Pair

```python
student["email"] = "alice@example.com"
```

The dictionary now contains:

```text
{
    "name": "Alice",
    "age": 21,
    "email": "alice@example.com"
}
```

---

# 🗑️ Removing Dictionary Items

The `.pop()` method can be used to remove an item using its key.

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

student.pop("course")
```

The `"course"` item is removed.

---

# 🛠️ Dictionary Methods

Python provides several useful dictionary methods.

## `.keys()`

Returns all the keys in the dictionary.

```python
student.keys()
```

---

## `.values()`

Returns all the values in the dictionary.

```python
student.values()
```

---

## `.items()`

Returns the dictionary's key-value pairs.

Each pair is represented as a tuple.

```python
student.items()
```

This is especially useful when looping through a dictionary.

```python
for key, value in student.items():
    print(key, value)
```

---

## `.get()`

Returns the value associated with a key.

If the key doesn't exist, you can provide a default value.

```python
student.get("grade", "Not Found")
```

---

## 📋 Dictionary Methods Quick Reference

| Method | Purpose |
|---|---|
| `.get(key)` | Safely retrieves a value |
| `.keys()` | Returns all keys |
| `.values()` | Returns all values |
| `.items()` | Returns key-value pairs |
| `.pop(key)` | Removes an item by key |

---

# 🏋️ Exercises

## Exercise 1

Create a dictionary called `car` containing:

- `brand`
- `model`
- `year`

Print the model of the car.

### Expected Output

```text
Model: Civic
```

> Your car information can be different.

---

## Exercise 2

Change the `year` value of your `car` dictionary to `2024`.

Then add a new key called `color` with the value `"Silver"`.

### Expected Output

```text
{'brand': 'Honda', 'model': 'Civic', 'year': 2024, 'color': 'Silver'}
```

> Your dictionary values can be different.

---

## Exercise 3

Loop through your `car` dictionary using `.items()` and print both the keys and values.

### Expected Output

```text
brand: Honda
model: Civic
year: 2024
color: Silver
```

> Your car information can be different.

---

# 🚀 Mini Project - Phone Book

Create a file named **`phone_book.py`**.

### Requirements

Your program should:

- Start with an empty dictionary.
- Allow users to add contacts.
- Store a person's name as the key.
- Store their phone number as the value.
- Allow users to search for a contact.
- Display all saved contacts.
- Allow the user to exit the program.

### Sample Input

```text
--- Digital Phone Book ---

1. Add Contact
2. Search Contact
3. View All
4. Exit

Choose an option: 1
Enter name: Alice
Enter phone number: 0771234567

Choose an option: 1
Enter name: Bob
Enter phone number: 0719876543

Choose an option: 2
Enter name to search: Alice

Choose an option: 3

Choose an option: 4
```

### Expected Output

```text
Contact Alice saved!
Contact Bob saved!

Number: 0771234567

All Contacts:
Alice: 0771234567
Bob: 0719876543
```

---

# ❌ Common Mistakes

## `KeyError`

A `KeyError` occurs when you try to access a key that doesn't exist.

For example:

```python
student = {"name": "Alice"}

print(student["age"])
```

The key `"age"` doesn't exist.

### Solution

Use `.get()`:

```python
student.get("age", "Not Found")
```

Or check whether the key exists:

```python
if "age" in student:
    print(student["age"])
```

---

## Using Duplicate Keys

Dictionaries cannot contain multiple values under the same key.

For example:

```python
student = {
    "name": "Alice",
    "name": "Bob"
}
```

The second `"name"` replaces the first one.

The result will contain:

```text
name: Bob
```

---

## Using Mutable Objects as Keys

Dictionary keys must be based on immutable values.

Valid keys include:

```python
"name"
42
(10, 20)
```

A list cannot be used as a dictionary key:

```python
[1, 2, 3]
```

This is because lists are mutable.

---

## Confusing Keys and Values

Consider:

```python
student = {
    "name": "Alice"
}
```

Here:

```text
"name"  → key
"Alice" → value
```

The key is used to find the value.

---

# 📝 Summary

Today you learned how to:

- ✅ Create **Dictionaries** using key-value pairs.
- ✅ Access dictionary values using keys.
- ✅ Safely retrieve values using `.get()`.
- ✅ Add and modify dictionary items.
- ✅ Remove items using `.pop()`.
- ✅ Use `.keys()`, `.values()`, and `.items()`.
- ✅ Build a **Phone Book** application.

---

# 🔑 Key Takeaways

- Dictionaries store information as **key-value pairs**.
- Keys are used to identify and retrieve values.
- Dictionaries are **mutable**, so they can be changed after creation.
- `.get()` is useful when a key might not exist.
- `.items()` is useful when you need both keys and values while looping.
- Dictionaries are ideal when you need to look up information using a meaningful label instead of a numerical index.

---

# 📖 What's Next?

## Day 019 - Sets