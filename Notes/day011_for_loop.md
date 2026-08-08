# Day 011 - `for` Loop

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand the concept of **definite iteration** using the `for` loop.
- Iterate over **sequences** such as strings and lists.
- Compare the use cases of `for` loops and `while` loops.
- Build a **Multiplication Table Generator** project.

---

# 📚 What is a `for` Loop?

A **`for` loop** is used to iterate over a sequence, such as:

- Strings
- Lists
- Tuples
- Dictionaries
- Sets

Unlike a `while` loop, which runs while a condition is `True`, a `for` loop is typically used when you know exactly what items you want to process.

### Basic Syntax

```python
for item in sequence:
    # Code to execute
```

---

# 🔤 Iterating Over a String

A string is a sequence of characters.

A `for` loop can process one character at a time.

### Example

```python
word = "PYTHON"

for letter in word:
    print(letter)
```

Output:

```text
P
Y
T
H
O
N
```

---

# 📋 Iterating Over a List

A list is a collection of items.

A `for` loop visits each item one by one.

### Example

```python
fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print("I like", fruit)
```

Output:

```text
I like Apple
I like Banana
I like Cherry
```

---

# ⚖️ `for` Loop vs `while` Loop

| `for` Loop | `while` Loop |
|------------|--------------|
| Used when the number of iterations is known. | Used when the number of iterations is unknown. |
| Iterates over a sequence. | Runs while a condition is `True`. |
| No manual counter is usually needed. | Often requires a control variable. |
| Less likely to create infinite loops. | Can create infinite loops if the condition never changes. |

---

# 🏋️ Exercises

## Exercise 1

Write a `for` loop that prints every character in your name.

### Sample Input

```text
Name: Alice
```

### Expected Output

```text
A
l
i
c
e
```

---

## Exercise 2

Create a list containing five different colors.

Use a `for` loop to print each color followed by:

```
is a beautiful color.
```

### Expected Output

```text
Red is a beautiful color.
Blue is a beautiful color.
Green is a beautiful color.
Yellow is a beautiful color.
Purple is a beautiful color.
```

> *Your colors may be different.*

---

## Exercise 3

Use a `for` loop to calculate the total length of all strings in the following list:

```python
["cat", "dog", "elephant"]
```

### Expected Output

```text
14
```

---
# 🚀 Mini Project - Multiplication Table Generator

Create a file named **`multiplication_table.py`**.

### Requirements

Your program should:

- Ask the user to enter a number.
- Generate the multiplication table for that number from **1 to 10**.
- Display each multiplication result.

> **Note:** This project uses the `range()` function, which will be explained in detail in the next lesson.

### Sample Input

```text
Enter a number: 5
```

### Expected Output

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

# ❌ Common Mistakes

## Forgetting the Colon (`:`)

Incorrect:

```python
for item in sequence
```

Correct:

```python
for item in sequence:
```

---

## Incorrect Indentation

Incorrect:

```python
for fruit in fruits:
print(fruit)
```

Correct:

```python
for fruit in fruits:
    print(fruit)
```

---

## Modifying a List While Iterating

Avoid changing a list while looping through it.

Incorrect:

```python
for fruit in fruits:
    fruits.remove(fruit)
```

This may skip items or produce unexpected results.

---

# 📝 Summary

Today you learned how to:

- ✅ Use `for` loops to iterate over sequences.
- ✅ Loop through strings and lists.
- ✅ Understand when to use a `for` loop instead of a `while` loop.
- ✅ Build a Multiplication Table Generator.

---

# 🔑 Key Takeaways

- A `for` loop is used to process each item in a sequence.
- Strings and lists are iterable objects.
- `for` loops automatically move to the next item, so manual counters are usually unnecessary.
- Use a `for` loop when you know what collection you want to iterate through.

---

# 📖 What's Next?

## Day 012 – `range()`