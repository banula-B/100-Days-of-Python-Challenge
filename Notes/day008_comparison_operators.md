# Day 008 - Comparison Operators

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Identify and use all six **comparison operators** in Python.
- Understand that comparison operations return **Boolean values** (`True` or `False`).
- Apply comparison operators inside conditional statements.
- Build a **Number Guessing Game** using comparison logic.

---

# 📚 What are Comparison Operators?

Comparison operators are used to compare two values.

When Python evaluates a comparison, it returns either:

- `True`
- `False`

These Boolean values are the foundation of decision-making in Python programs.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 10` | `False` |
| `<` | Less than | `5 < 10` | `True` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `8 <= 7` | `False` |

---

# ✅ Boolean Values

Comparison operators always return a **Boolean** value.

Python has two Boolean values:

- `True`
- `False`

### Example

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)
```

Output:

```text
True
False
True
False
```

---

# 🔍 Using Comparison Operators in Conditions

Comparison operators are commonly used with `if`, `elif`, and `else` statements.

### Example

```python
target_score = 100
user_score = 120

if user_score > target_score:
    print("New High Score!")
elif user_score == target_score:
    print("You tied the record!")
else:
    print("Try again to beat the high score.")
```

Output:

```text
New High Score!
```

---

# 🚀 Mini Project - Number Guessing Game

Create a file named **`guessing_game.py`**.

### Requirements

Your program should:

- Set a secret number.
- Ask the user to guess the number.
- Compare the user's guess with the secret number.
- Display one of the following messages:
  - Correct!
  - Too high!
  - Too low!

### Sample Input

```text
Guess the secret number (1-10): 5
```

> Assume the secret number is **7**.

### Expected Output

```text
Too low! Try a larger number next time.
```

---

# 🏋️ Exercises

## Exercise 1

Ask the user to enter two numbers.

Print **`True`** if the first number is greater than the second.

Otherwise, print **`False`**.

### Sample Input

```text
Enter first number: 15
Enter second number: 10
```

### Expected Output

```text
True
```

---

## Exercise 2

Ask the user for their age.

If the age is **not equal to 21**, print:

```
"You are not exactly 21 years old."
```

### Sample Input

```text
Enter your age: 18
```

### Expected Output

```text
You are not exactly 21 years old.
```

---

## Exercise 3

Ask the user to enter a temperature.

If the temperature is **less than or equal to 0**, print:

```
It is freezing!
```

### Sample Input

```text
Enter temperature: -3
```

### Expected Output

```text
It is freezing!
```

---

# ❌ Common Mistakes

## Confusing `=` and `==`

Incorrect:

```python
if x = 5:
```

The single equals sign (`=`) is used for **assignment**, not comparison.

Correct:

```python
if x == 5:
```

---

## Comparing Different Data Types

Incorrect:

```python
if "10" > 5:
```

A string cannot be compared directly with a number.

Convert the input first:

```python
number = int(input("Enter a number: "))
```

---

## Forgetting That Comparisons Return Booleans

Remember that comparison expressions always evaluate to either:

```text
True
```

or

```text
False
```

---

# 📝 Summary

Today you learned how to:

- ✅ Use comparison operators to compare values.
- ✅ Understand Boolean values (`True` and `False`).
- ✅ Apply comparison operators inside conditional statements.
- ✅ Build a Number Guessing Game.

---

# 🔑 Key Takeaways

- Comparison operators allow Python to compare two values.
- Every comparison returns either `True` or `False`.
- Comparison operators are commonly used inside `if`, `elif`, and `else` statements.
- Always convert user input into the correct data type before comparing numbers.

---

# 📖 What's Next?

## Day 009 – Logical Operators