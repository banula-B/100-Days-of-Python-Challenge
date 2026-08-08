# Day 013 - Nested Loops

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand the concept of **nested loops** (a loop inside another loop).
- Trace the execution flow of **outer** and **inner** loops.
- Apply nested loops to work with patterns and multi-dimensional data.
- Build a **Pyramid Pattern** project using nested loops.

---

# 📚 What are Nested Loops?

A **nested loop** is a loop placed inside another loop.

The outer loop executes first.

For **every iteration** of the outer loop, the inner loop completes **all** of its iterations.

### Basic Syntax

```python
for outer_item in outer_sequence:
    for inner_item in inner_sequence:
        # Code to execute
```

---

# 🔄 Understanding the Execution Flow

The outer loop controls how many times the inner loop starts.

Example:

```python
for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")
```

Output:

```text
(0, 0)
(0, 1)
(1, 0)
(1, 1)
(2, 0)
(2, 1)
```

Notice that for each value of `x`, the value of `y` starts again from **0**.

---

# ⏱️ How Nested Loops Work

Think of a clock:

- The **hour hand** is the outer loop.
- The **minute hand** is the inner loop.

The minute hand must complete an entire cycle before the hour hand moves forward.

This is exactly how nested loops behave.

---

# 🖨️ Printing Patterns

Nested loops are commonly used to create text patterns.

### Example

```python
for row in range(3):
    for column in range(4):
        print("*", end="")
    print()
```

Output:

```text
****
****
****
```

The `end=""` parameter prevents `print()` from moving to a new line immediately.

The final `print()` moves to the next row.

---

# 🏋️ Exercises

## Exercise 1

Print a **5 × 5** grid of hash (`#`) symbols using nested loops.

### Expected Output

```text
#####
#####
#####
#####
#####
```

---

## Exercise 2

Use nested loops to print a multiplication table for the numbers **1 to 5**.

### Expected Output

```text
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
```

---

## Exercise 3

Use nested loops to print every combination of the following lists:

```python
categories = ["Fruit", "Color"]
items = ["Apple", "Red"]
```

### Expected Output

```text
Fruit - Apple
Fruit - Red
Color - Apple
Color - Red
```

---
# 🚀 Mini Project - Pyramid Pattern

Create a file named **`pyramid.py`**.

### Requirements

Your program should:

- Ask the user for the number of pyramid levels.
- Use nested loops to print a centered pyramid made of `*`.
- Print one level per line.

### Sample Input

```text
How many levels? 3
```

### Expected Output

```text
  *
 ***
*****
```

---

# ❌ Common Mistakes

## Using the Same Variable Name

Incorrect:

```python
for i in range(5):
    for i in range(5):
        print(i)
```

The inner loop overwrites the outer loop variable.

Use different names:

```python
for row in range(5):
    for column in range(5):
        print("*")
```

---

## Incorrect Indentation

Incorrect:

```python
for row in range(3):
    for col in range(3):
        print("*", end="")
        print()
```

This prints one star per line.

Correct:

```python
for row in range(3):
    for col in range(3):
        print("*", end="")
    print()
```

---

## Forgetting `end=""` When Printing Patterns

Without `end=""`, each `print()` starts a new line.

Use:

```python
print("*", end="")
```

to keep printing on the same line.

---

# 📝 Summary

Today you learned how to:

- ✅ Create nested loops.
- ✅ Understand the relationship between outer and inner loops.
- ✅ Use nested loops to print patterns and tables.
- ✅ Build a Pyramid Pattern project.

---

# 🔑 Key Takeaways

- A nested loop is simply a loop inside another loop.
- The inner loop completes all of its iterations before the outer loop continues.
- Nested loops are useful for working with grids, tables, matrices, and text patterns.
- Proper indentation is essential when writing nested loops.
- The `end=""` parameter is useful when printing patterns on the same line.

---

# 📖 What's Next?

## Day 014 – `break` & `continue`