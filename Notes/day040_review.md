# Day 040 - Review

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Consolidate all key concepts covered in **Phase 2 (Days 21–39)**.
* Understand how **Functions**, **Lambdas**, **File Handling**, **Exceptions**, **JSON**, and **Datetime** work together in real-world application architectures.
* Recognise common architectural traps and edge cases when combining different systems.
* Build a complete, crash-resistant, persistent **CLI Contact Book** project.

---

# Phase 2 Consolidation & Architecture

Congratulations! You have officially reached the end of **Phase 2: Functions & Data Structures**.

Over the past twenty days, you have moved from writing simple linear scripts toward building **modular, structured, and resilient applications**.

The goal of this review is not simply to remember individual concepts. It is to understand how these concepts work together to form a complete application.

---

## How the Concepts Fit Together

A typical command-line application can be organised into several layers:

```text
┌────────────────────────────────────────────────────────┐
│                   User Interface (CLI)                 │
│              User input and menu system                │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                     Business Logic                     │
│  • Input validation                                    │
│  • Data filtering                                      │
│  • Functions and custom exceptions                     │
│  • Lambda expressions                                  │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                    Data Persistence                    │
│  • JSON storage                                        │
│  • CSV files                                           │
│  • File handling                                       │
│  • Datetime timestamps                                 │
└────────────────────────────────────────────────────────┘
```

This separation makes programs easier to understand, test, maintain, and extend.

---

# Phase 2 Concepts Review

## 1. Functions & Scope — Days 21–24

Functions allow you to divide a large program into smaller, reusable pieces.

Instead of placing every operation inside one large block of code, you can create functions responsible for specific tasks.

For example:

```python
def calculate_total(price, quantity):
    return price * quantity
```

Functions help with:

* Reusability.
* Organisation.
* Testing.
* Readability.
* Reducing duplicated code.

### Scope

Python variables can exist in different scopes.

You learned about:

* Local scope.
* Global scope.
* The LEGB rule.

The **LEGB** rule describes the order Python follows when looking for a variable:

```text
Local
Enclosing
Global
Built-in
```

---

# 2. Functional Programming — Days 25–28

You learned several tools that allow you to process collections efficiently.

### `lambda`

A `lambda` is a small anonymous function.

Example:

```python
square = lambda x: x ** 2

print(square(5))
```

### `map()`

`map()` applies a function to every element in an iterable.

```python
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, numbers))
```

### `filter()`

`filter()` selects elements that satisfy a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)
```

These tools can be particularly useful when working with lists of dictionaries and structured data.

---

# 3. Modules & Packages — Days 29–30

As programs become larger, putting everything into one file becomes difficult to manage.

**Modules** allow related functionality to be separated into different Python files.

For example:

```text
project/
├── main.py
├── calculator.py
└── utilities.py
```

Packages take organisation a step further by grouping related modules into directories.

This helps prevent a main script from becoming a large, difficult-to-maintain file.

---

# 4. File Input/Output — Days 31–33

You learned how Python can interact with files.

Common file operations include:

* Reading.
* Writing.
* Appending.

You also learned the importance of using context managers:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

The `with` statement automatically handles closing the file.

### File Modes

| Mode  | Purpose             |
| ----- | ------------------- |
| `"r"` | Read                |
| `"w"` | Write and overwrite |
| `"a"` | Append              |

Be careful with `"w"` because it replaces the existing contents of a file.

---

# 5. Exception Handling — Days 34–35

Programs can encounter errors during execution.

Python allows you to handle expected runtime errors using:

```python
try:
    # Code that might fail
    pass

except ValueError:
    # Handle the error
    pass
```

You also learned about custom exceptions.

For example:

```python
class InvalidContactError(Exception):
    pass
```

Custom exceptions allow applications to represent specific business rules and validation failures.

---

# 6. JSON — Day 36

JSON provides a structured way to store and exchange data.

Python's built-in `json` module provides four important functions:

| Function       | Purpose                     |
| -------------- | --------------------------- |
| `json.dumps()` | Python object → JSON string |
| `json.dump()`  | Python object → JSON file   |
| `json.loads()` | JSON string → Python object |
| `json.load()`  | JSON file → Python object   |

JSON is commonly used for:

* Configuration files.
* Application settings.
* API communication.
* Persistent application data.

---

# 7. CSV — Day 37

CSV files are commonly used for tabular data.

You learned:

* `csv.reader()`
* `csv.DictReader()`
* `csv.writer()`
* `csv.DictWriter()`

`DictReader` and `DictWriter` are especially useful when working with named columns.

Example structure:

```csv
name,grade,status
Alice,85,Passed
Bob,45,Failed
```

Remember that CSV values are normally read as **strings**, so numerical values may need to be converted before calculations.

---

# 8. Datetime — Day 38

Python's `datetime` module allows programs to work with dates and times.

Important tools include:

```python
datetime.now()
```

```python
strftime()
```

```python
strptime()
```

```python
timedelta()
```

You can use these tools to:

* Record timestamps.
* Format dates.
* Parse dates.
* Calculate deadlines.
* Compare dates.
* Create countdown systems.

---

# 9. Random — Day 39

The `random` module allows programs to generate pseudorandom values.

Important functions include:

```python
random.random()
random.randint()
random.uniform()
random.choice()
random.shuffle()
random.sample()
```

The module is useful for:

* Games.
* Simulations.
* Random selection.
* Testing.
* Sampling.

Remember that `random` is **not appropriate for security-sensitive randomness**. Use the `secrets` module for those situations.

---

# How These Concepts Work Together

A real application may combine many of these concepts.

For example, a contact application could use:

```text
Functions
    ↓
Organise application logic
    ↓
Exceptions
    ↓
Validate user input
    ↓
Lambda / filter
    ↓
Search and process data
    ↓
JSON
    ↓
Persist contact records
    ↓
Datetime
    ↓
Store registration timestamps
```

This is the major lesson of Phase 2:

> Individual Python features become much more powerful when they are combined into a structured application.

---

# Exercises

## Exercise 1

Write a single-line expression using `map()` and a `lambda` to strip whitespace and capitalize all names in the following list:

```python
[" alice ", "bob ", " CHARLIE "]
```

The resulting values should be equivalent to:

```text
Alice
Bob
Charlie
```

---

## Exercise 2

Create a custom exception class named:

```text
InvalidPhoneNumberError
```

Write a function that raises this exception if a phone number string does not contain exactly **10 digits**.

---

## Exercise 3

Given the dictionary:

```python
{
    "name": "Alice",
    "created_at": "2026-09-01 15:30:00"
}
```

Write a program that:

1. Reads the `"created_at"` value.
2. Parses it into a Python `datetime` object.
3. Adds **7 days** using `timedelta`.
4. Converts the updated datetime back into a formatted string.
5. Prints the updated date.

---

# Mini Project: CLI Contact Book

## Project Overview

Build a **CLI Contact Book** as the Phase 2 capstone project.

The application should act as a persistent command-line contact database.

It should allow users to:

* Add contacts.
* View contacts.
* Search contacts.
* Delete contacts.
* Validate contact information.
* Store contact data permanently.
* Record when contacts were added.

The database should be stored in:

```text
contacts.json
```

---

# Project Requirements

Your Contact Book should include the following features.

## 1. Persistent Storage

Use JSON to store contact information.

The application should:

* Load existing contacts when the program starts.
* Create an empty contact book if no database exists.
* Save changes back to the JSON file.

---

## 2. Add Contacts

Allow the user to enter:

* Name.
* Phone number.
* Email address.

Validate the information before saving it.

---

## 3. Contact Validation

Create a custom exception such as:

```python
InvalidContactError
```

Use it to handle invalid contact information.

Your validation rules can include:

* Contact name cannot be blank.
* Phone number must contain valid digits.
* Email must follow a basic valid format.
* Duplicate contact names should be detected.

---

## 4. Contact Timestamps

When a contact is added, store the date and time they were registered.

Example:

```text
2026-09-01 15:30:00
```

Use Python's `datetime` module to generate the timestamp.

---

## 5. View Contacts

Display all contacts in a clean, readable format.

For example:

```text
================ CONTACTS ================

NAME                 PHONE           EMAIL
------------------------------------------------
Alice                0771234567      alice@example.com
Bob                  0719876543      bob@example.com

============================================
```

---

## 6. Search Contacts

Allow users to search contacts using:

* Contact name.
* Phone number.

Use `filter()` and a `lambda` expression to practice the functional programming concepts learned earlier.

The search should be case-insensitive.

---

## 7. Delete Contacts

Allow the user to delete a contact by name.

Before deleting, ask the user for confirmation.

Example:

```text
Are you sure you want to delete 'Alice'? (y/n):
```

---

## 8. Main Menu

The application should provide a menu similar to:

```text
--- CLI Contact Book ---

1. View All Contacts
2. Add Contact
3. Search Contacts
4. Delete Contact
5. Exit
```

The program should continue running until the user chooses **Exit**.

---

# Suggested Project Structure

For this capstone, you can initially keep the project in a single file:

```text
contact_book.py
```

A possible logical structure is:

```text
contact_book.py
│
├── Custom Exceptions
│
├── Database Operations
│   ├── load_contacts()
│   └── save_contacts()
│
├── Validation
│   └── validate_contact()
│
├── Contact Operations
│   ├── add_contact()
│   ├── view_contacts()
│   ├── search_contacts()
│   └── delete_contact()
│
└── Main Program
    └── main()
```

This structure gives you practice organising a larger program into logical responsibilities.

---

# Skills Practiced

This project combines many concepts from Phase 2:

* Functions.
* Function parameters.
* Return values.
* Scope.
* Lambda expressions.
* `map()`.
* `filter()`.
* Modules.
* File handling.
* Context managers.
* JSON.
* Dictionaries.
* Lists.
* Exception handling.
* Custom exceptions.
* Datetime.
* String formatting.
* User input.
* Input validation.
* Loops.
* Conditional statements.
* Persistent data storage.

---

# Common Mistakes

## ❌ Modifying a Dictionary During Iteration

### Cause

Trying to delete dictionary entries while directly iterating over the dictionary:

```python
for key in contacts:
    if condition:
        del contacts[key]
```

Python can raise a `RuntimeError` because the size of the dictionary changes during iteration.

### Solution

If you need to modify the dictionary while iterating, work with a static list of keys:

```python
for key in list(contacts.keys()):
    # Safe modification
    pass
```

---

## ❌ Forgetting `json.JSONDecodeError`

### Cause

A JSON file may be:

* Empty.
* Corrupted.
* Incomplete.
* Manually edited incorrectly.

Calling `json.load()` on invalid JSON can raise:

```python
json.JSONDecodeError
```

### Solution

Handle the parsing error:

```python
try:
    # Load JSON
    pass

except json.JSONDecodeError:
    # Handle corrupted JSON
    pass
```

This prevents the entire application from crashing.

---

## ❌ Case-Sensitive Searches

### Cause

Python string comparisons are case-sensitive.

For example:

```python
"Alice" == "alice"
```

returns:

```text
False
```

### Solution

Normalise the values before comparing them:

```python
name.lower()
```

For example:

```python
name.lower() == search_name.lower()
```

This makes the comparison case-insensitive.

---

## ❌ Mixing Different Data Formats

A common problem in larger applications is expecting one data format while receiving another.

For example:

```text
CSV → strings
JSON → Python dictionaries/lists
User input → strings
Datetime → datetime objects
```

Always convert data into the appropriate type before performing operations.

---

## ❌ Putting Everything Inside `main()`

A large application becomes difficult to maintain if every operation is placed inside one function.

Instead, separate responsibilities into functions such as:

```text
load_contacts()
save_contacts()
validate_contact()
add_contact()
view_contacts()
search_contacts()
delete_contact()
```

This keeps the program modular and easier to understand.

---

# Phase 2 Summary

Today you reviewed the major concepts from **Days 21–39**.

You learned how to combine:

* ✅ Functions and scope.
* ✅ Lambda expressions.
* ✅ `map()` and `filter()`.
* ✅ Modules and packages.
* ✅ File handling.
* ✅ Exception handling.
* ✅ Custom exceptions.
* ✅ JSON.
* ✅ CSV.
* ✅ Datetime.
* ✅ Random number generation.
* ✅ Data validation.
* ✅ Persistent storage.

Most importantly, you learned that these features are not isolated topics.

They can be combined to create **real, functional applications**.

---

# Key Takeaways

* **Functions** divide applications into reusable components.
* **Scope** controls where variables can be accessed.
* **Lambda**, `map()`, and `filter()` provide useful tools for processing collections.
* **Modules and packages** help organise larger applications.
* **File handling** allows programs to store and retrieve information.
* **Exceptions** allow programs to handle unexpected situations gracefully.
* **Custom exceptions** allow applications to represent specific validation or business-rule failures.
* **JSON** is useful for structured application storage.
* **CSV** is useful for tabular data.
* **Datetime** provides tools for timestamps and date calculations.
* **Random** provides pseudorandom values for simulations and games.
* Good application architecture separates **input, business logic, validation, and data persistence**.
* Defensive validation helps prevent invalid data from entering permanent storage.

---

# Phase 2 Capstone Achievement

By completing the **CLI Contact Book**, you are combining many of the concepts learned throughout Phase 2 into one application.

Instead of simply learning individual Python features, you are now beginning to think about:

```text
How should I structure a program?
        ↓
How should data flow through the application?
        ↓
How should I validate user input?
        ↓
How should I handle errors?
        ↓
How should I store data permanently?
        ↓
How can I keep the code maintainable?
```

This transition from **writing individual pieces of code** to **designing complete applications** is an important step in your Python journey.

---

# What's Next?

## Day 041 - Classes and Objects

🎉 **Phase 2 is officially complete!**

Tomorrow, you will begin **Phase 3: Object-Oriented Programming (OOP)**.

You will start learning how to model real-world entities using:

* Classes.
* Objects.
* Attributes.
* Methods.
* Constructors.
* Encapsulation.
* Object-oriented design.

This will mark the transition from primarily procedural Python programming toward **Object-Oriented Python development**.
