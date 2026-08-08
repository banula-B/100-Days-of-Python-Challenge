# Day 005 - `if` Statements

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand the concept of **control flow** in programming.
- Use the **`if` statement** to execute code based on a condition.
- Master the importance of **indentation** in Python.
- Build an **Age Checker** project to determine user eligibility.

---

# 📚 What is an `if` Statement?

In programming, we often want our programs to make decisions.

An **`if` statement** allows a program to execute a block of code **only when a condition is `True`**.

### Basic Syntax

```python
if condition:
    print("This condition is met!")
```

### Example

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

Output:

```text
You are an adult.
```

> **Important:**
>
> - Every `if` statement ends with a colon (`:`).
> - The code inside the `if` block must be indented (usually 4 spaces).

---

# 🔍 Boolean Logic and Conditions

An `if` statement checks whether a condition is **True** or **False**.

Python uses comparison operators to create these conditions.

| Operator | Meaning | Example |
|----------|---------|---------|
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `>=` | Greater than or equal to | `18 >= 18` |
| `<=` | Less than or equal to | `5 <= 10` |
| `==` | Equal to | `10 == 10` |
| `!=` | Not equal to | `10 != 5` |

### Example

```python
score = 85

if score > 80:
    print("Great job!")
```

Output:

```text
Great job!
```

---

# 📏 The Importance of Indentation

Unlike many programming languages that use curly braces (`{}`), Python uses **indentation** to define code blocks.

Everything indented under an `if` statement belongs to that block.

Example:

```python
if 5 > 2:
    print("Inside the if block")

print("Outside the if block")
```

Output:

```text
Inside the if block
Outside the if block
```

---

# 🏋️ Exercises

## Exercise 1

Ask the user to enter a number.

If the number is greater than **0**, print:

```
Positive!
```

### Sample Input

```text
Enter a number: 8
```

### Expected Output

```text
Positive!
```

---

## Exercise 2

Create a variable named `password`.

Ask the user to enter a secret word.

If the entered value matches **`python123`**, print:

```
Access Granted
```

### Sample Input

```text
Enter password: python123
```

### Expected Output

```text
Access Granted
```

---

## Exercise 3

Ask the user for their name.

If the name is **Admin**, print:

```
Welcome, System Administrator.
```

### Sample Input

```text
Enter your name: Admin
```

### Expected Output

```text
Welcome, System Administrator.
```

---

# 🚀 Mini Project - Age Checker

Create a file named **`age_checker.py`**.

### Requirements

Your program should:

- Ask the user for their age.
- Convert the input into an integer.
- If the user is **13 or older**, display:

```
You are old enough to watch a PG-13 movie!
```

- If the user is **under 13**, display:

```
You must be at least 13 years old to watch this movie.
```

### Sample Input

```text
Please enter your age: 15
```

### Expected Output

```text
You are old enough to watch a PG-13 movie!
```

---

# ❌ Common Mistakes

## Forgetting the Colon (`:`)

Incorrect:

```python
if age > 18
```

This causes a **SyntaxError**.

Correct:

```python
if age > 18:
```

---

## Incorrect Indentation

Incorrect:

```python
if age >= 18:
print("Adult")
```

Python expects the code inside the `if` block to be indented.

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Using `=` Instead of `==`

Remember:

```python
x = 5
```

Assigns a value.

```python
if x == 5:
```

Checks whether two values are equal.

---

# 📝 Summary

Today you learned how to:

- ✅ Use **control flow** to make decisions.
- ✅ Write basic **`if` statements**.
- ✅ Create conditions using comparison operators.
- ✅ Use indentation correctly in Python.

---

# 🔑 Key Takeaways

- An `if` statement executes code only when a condition is **True**.
- Comparison operators help create logical conditions.
- Python uses indentation to define code blocks.
- Always compare values using `==`, not `=`.
- Make sure data types match when comparing values.

---

# 📖 What's Next?

## Day 006 – `if-else`