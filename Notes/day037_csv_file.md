# Day 037 - CSV Files

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand what **CSV (Comma-Separated Values)** files are and how they represent tabular data.
* Import Python's built-in **`csv`** module.
* Read CSV datasets as lists using **`csv.reader`** and as dictionaries using **`csv.DictReader`**.
* Write tabular data to files using **`csv.writer`** and **`csv.DictWriter`**.
* Build a **Student CSV Manager** project.

---

# What is a CSV File?

A **CSV (Comma-Separated Values)** file is a plain-text file that stores tabular data in a structured format.

Each line of a CSV file represents a **row**, while each value within a row represents a **column**. Columns are separated by a delimiter, most commonly a comma `,`.

CSV files are widely used to transfer data between different systems, including:

* Excel
* Google Sheets
* Databases
* Python applications
* Data analysis tools

### Example CSV Content

```csv
name,grade,status
Alice,85,Passed
Bob,45,Failed
Charlie,92,Passed
```

The first row usually contains the **column headers**, while the remaining rows contain the actual data.

---

# The Python `csv` Module

Python provides a built-in **`csv`** module for working with CSV files.

You can import it using:

```python
import csv
```

The module handles many CSV-specific details, including fields containing commas, quotation marks, and different delimiters.

---

# Reading CSV Files

There are two important ways to read CSV files:

* `csv.reader()`
* `csv.DictReader()`

---

## 1. Using `csv.reader()`

`csv.reader()` reads each row and returns it as a **list of strings**.

### Example

```python
import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

For the following CSV:

```csv
name,grade,status
Alice,85,Passed
Bob,45,Failed
```

The rows will be represented approximately as:

```python
["name", "grade", "status"]
["Alice", "85", "Passed"]
["Bob", "45", "Failed"]
```

### Accessing Columns

Because each row is a list, you can access values using indexes:

```python
print(row[0])
print(row[1])
print(row[2])
```

This works, but it can become difficult to understand when a CSV has many columns.

---

# 2. Using `csv.DictReader()`

`csv.DictReader()` is especially useful when working with labeled data.

It reads the first row as the **column headers** and uses those headers as dictionary keys.

### Example

```python
import csv

with open("students.csv", "r", newline="") as file:
    dict_reader = csv.DictReader(file)

    for row in dict_reader:
        print(f"Student: {row['name']} | Grade: {row['grade']}")
```

Each row behaves like a Python dictionary:

```python
{
    "name": "Alice",
    "grade": "85",
    "status": "Passed"
}
```

You can then access columns using their names:

```python
row["name"]
row["grade"]
row["status"]
```

### Why `DictReader` Is Useful

Compare:

```python
row[1]
```

with:

```python
row["grade"]
```

The second version is much easier to understand, especially when working with larger datasets.

---

# `reader()` vs `DictReader()`

| Function           | Returns      | Access Method |
| ------------------ | ------------ | ------------- |
| `csv.reader()`     | Lists        | Indexes       |
| `csv.DictReader()` | Dictionaries | Column names  |

### Example

With `csv.reader()`:

```python
row[0]
```

With `csv.DictReader()`:

```python
row["name"]
```

For datasets with meaningful column names, `DictReader` is often more convenient.

---

# Writing CSV Files

Python provides two main tools for writing CSV data:

* `csv.writer()`
* `csv.DictWriter()`

---

# 1. Using `csv.writer()`

`csv.writer()` is useful when your data is represented as lists.

### Example Data

```python
data_to_write = [
    ["name", "grade", "status"],
    ["Alice", "85", "Passed"],
    ["Bob", "45", "Failed"]
]
```

### Writing the Data

```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(data_to_write[0])
    writer.writerows(data_to_write[1:])
```

### Important Methods

#### `writer.writerow()`

Writes **one row**.

```python
writer.writerow(["Alice", "85", "Passed"])
```

#### `writer.writerows()`

Writes **multiple rows**.

```python
writer.writerows([
    ["Alice", "85", "Passed"],
    ["Bob", "45", "Failed"]
])
```

---

# 2. Using `csv.DictWriter()`

`csv.DictWriter()` allows you to write dictionary data using predefined column names.

### Example

```python
import csv

headers = ["name", "grade", "status"]

student_record = {
    "name": "Charlie",
    "grade": "92",
    "status": "Passed"
}

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writerow(student_record)
```

The `fieldnames` parameter defines the column headers.

---

## Writing Headers with `writeheader()`

If the CSV file is new or empty, you can write the headers using:

```python
writer.writeheader()
```

Example:

```python
with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writeheader()
    writer.writerow(student_record)
```

---

# `writer()` vs `DictWriter()`

| Function           | Data Format  | Best Used For                      |
| ------------------ | ------------ | ---------------------------------- |
| `csv.writer()`     | Lists        | Simple tabular data                |
| `csv.DictWriter()` | Dictionaries | Structured data with named columns |

---

# CSV Data Types

One important thing to remember is that CSV files are **text files**.

When Python reads a CSV file, values are initially returned as strings.

For example:

```csv
name,age,score
Alice,21,85
```

The values are initially read approximately as:

```python
{
    "name": "Alice",
    "age": "21",
    "score": "85"
}
```

Notice that `"21"` and `"85"` are strings.

If you need to perform calculations, convert them first:

```python
age = int(row["age"])
score = float(row["score"])
```

---

# Opening CSV Files Correctly

When working with CSV files, it is recommended to use:

```python
with open("students.csv", "r", newline="") as file:
```

for reading, and:

```python
with open("students.csv", "w", newline="") as file:
```

for writing.

The `newline=""` argument allows Python's `csv` module to handle newlines correctly across operating systems.

---

# Reading and Writing Modes

CSV files use the same file modes you learned previously.

| Mode  | Purpose                      |
| ----- | ---------------------------- |
| `"r"` | Read existing CSV data       |
| `"w"` | Write and overwrite the file |
| `"a"` | Append new data to the file  |

### Be Careful With `"w"`

Using `"w"` will overwrite the existing contents of the CSV file.

If you want to preserve existing records and add new ones, use `"a"`.

---

# Exercises

## Exercise 1

Create a file named `inventory.csv` containing the following columns:

* `item`
* `quantity`
* `price`

Use Python's `csv.writer` to add three rows of tools or groceries.

---

## Exercise 2

Write a program that:

1. Opens `inventory.csv` using `csv.DictReader`.
2. Converts the numeric values from strings.
3. Calculates the total cost of the inventory.

Use the following calculation:

```text
total cost = quantity × price
```

Then calculate the total cost across all rows.

---

## Exercise 3

Create a program that:

1. Prompts the user for an item name.
2. Searches for that item in `inventory.csv`.
3. Displays its quantity and price if the item is found.
4. Displays an appropriate message if the item does not exist.

---

# Mini Project: Student CSV Manager

## Project Overview

Build a **Student CSV Manager** that works as a simple command-line student registry.

The application should allow users to:

* Add student records.
* Store student names.
* Store numerical grades.
* Automatically determine whether a student passed or failed.
* View all student records.
* Permanently store records inside a CSV file.

The database file should be:

```text
students.csv
```

---

## Project Requirements

Your program should:

1. Create `students.csv` if it does not already exist.
2. Add the appropriate column headers.
3. Allow users to enter a student's name.
4. Allow users to enter the student's grade.
5. Validate that the grade is between `0` and `100`.
6. Determine the student's status automatically.
7. Use **50** as the passing grade.
8. Save the student's record to the CSV file.
9. Display all saved student records.
10. Provide a simple command-line menu.
11. Allow the user to exit the program.
12. Handle invalid user input gracefully.

---

## Suggested CSV Structure

Your CSV file can use these columns:

```csv
Name,Grade,Status
```

Example records:

```csv
Alice,85,Passed
Bob,45,Failed
Charlie,92,Passed
```

---

## Suggested Program Functions

To keep your project organised, consider creating functions such as:

```text
initialize_database()
add_student()
view_students()
```

You can also create additional functions if you need them.

---

## Passing Rule

The application should determine the status using this rule:

```text
Grade >= 50 → Passed
Grade < 50  → Failed
```

---

## Skills Practiced

This project gives you practice with:

* `csv`
* `csv.reader`
* `csv.DictReader`
* `csv.writer`
* `csv.DictWriter`
* `writerow()`
* `writerows()`
* `writeheader()`
* File handling
* `"r"`, `"w"`, and `"a"` modes
* Dictionaries
* Lists
* Functions
* Loops
* Conditional statements
* Exception handling
* User input
* Data validation
* Persistent data storage

---

# Common Mistakes

## ❌ Forgetting `newline=""`

### Cause

When writing CSV files without specifying `newline=""`, you may encounter unwanted blank lines between rows, particularly on Windows.

### Solution

Use:

```python
with open("students.csv", "w", newline="") as file:
```

For consistency, use `newline=""` when opening CSV files for both reading and writing.

---

## ❌ Treating Numerical Data as Strings

### Cause

CSV data is read as strings.

For example:

```python
row["grade"]
```

may return:

```python
"85"
```

instead of:

```python
85
```

Trying to perform calculations directly on string values can cause errors.

### Solution

Convert the values explicitly:

```python
grade = float(row["grade"])
quantity = int(row["quantity"])
```

---

## ❌ Column Key Mismatch in `DictWriter`

### Cause

The dictionary keys do not match the column names defined in `fieldnames`.

For example:

```python
headers = ["name", "grade"]
```

but the dictionary contains:

```python
{
    "student": "Alice",
    "grade": 85
}
```

The key `student` does not match the defined field name `name`.

### Solution

Make sure the dictionary keys match the `fieldnames`.

---

## ❌ Accidentally Overwriting the CSV

### Cause

Using `"w"` mode when you intended to add a new record.

```python
open("students.csv", "w")
```

The `"w"` mode clears the existing contents before writing.

### Solution

Use append mode when adding new records:

```python
open("students.csv", "a")
```

---

## ❌ Forgetting the CSV Header

When using `DictWriter`, remember to write the header when creating a new CSV file:

```python
writer.writeheader()
```

Otherwise, your CSV may not contain the column names required by `DictReader`.

---

# Summary

Today you learned how to:

* ✅ Understand the structure of **CSV files**.
* ✅ Import Python's built-in **`csv`** module.
* ✅ Read CSV files using **`csv.reader()`**.
* ✅ Read labeled CSV data using **`csv.DictReader()`**.
* ✅ Write list-based data using **`csv.writer()`**.
* ✅ Write dictionary-based data using **`csv.DictWriter()`**.
* ✅ Write headers using `writeheader()`.
* ✅ Write individual rows using `writerow()`.
* ✅ Write multiple rows using `writerows()`.
* ✅ Convert CSV strings into numerical values.
* ✅ Build a **Student CSV Manager** project.

---

# Key Takeaways

* **CSV files** are simple text files commonly used to represent tabular data.
* Each row represents a record, while columns represent individual fields.
* `csv.reader()` returns rows as lists.
* `csv.DictReader()` returns rows as dictionaries.
* `csv.writer()` works with list-based data.
* `csv.DictWriter()` works with dictionary-based data.
* CSV values are initially read as **strings**.
* Convert numerical values before performing calculations.
* Use `newline=""` when opening CSV files.
* Be careful when using `"w"` because it overwrites existing data.
* Use `"a"` when you want to add new records.
* CSV files are an important foundation for **data analysis and machine learning workflows**.

---

# What's Next?

## Day 038 - Datetime

In the next lesson, you will learn how to work with **dates and times** using Python's `datetime` module.

You will learn how to:

* Get the current date and time.
* Create specific dates and times.
* Format dates and times.
* Extract information such as year, month, and day.
* Perform calculations with dates and times.
* Work with timestamps.
