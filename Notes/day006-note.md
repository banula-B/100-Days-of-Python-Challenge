# Day 006 - `if-else`

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand the **`if-else` statement** for binary decision-making.
- Write code that provides an alternative action when a condition is not met.
- Use the **modulo operator (`%`)** to check for divisibility.
- Build an **Even/Odd Checker** project.

---

# 📚 The `else` Statement

An `if` statement executes code only when its condition is **True**.

The **`else`** statement defines a block of code that runs **only when the `if` condition is False**.

### Basic Syntax

```python
if condition:
    # Runs if the condition is True
else:
    # Runs if the condition is False
```

> **Important:**
>
> - The `else` statement must always follow an `if` statement.
> - Both `if` and `else` end with a colon (`:`).
> - Their code blocks must be properly indented.

---

# ⚖️ Binary Logic: Either/Or

Many situations in programming have only two possible outcomes.

Examples:

- Yes / No
- True / False
- Pass / Fail
- Even / Odd

The `if-else` statement is perfect for handling these situations.

### Example

```python
is_raining = True

if is_raining:
    print("Take an umbrella.")
else:
    print("Enjoy the sunshine!")
```

Output:

```text
Take an umbrella.
```

---

# ➗ Using the Modulo Operator (`%`)

The **modulo operator (`%`)** returns the remainder after division.

Examples:

| Expression | Result |
|------------|--------|
| `10 % 2` | `0` |
| `11 % 2` | `1` |
| `15 % 4` | `3` |

A number is:

- **Even** if `number % 2 == 0`
- **Odd** if `number % 2 != 0`

### Example

```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Even
```

---

# 🚀 Mini Project - Even/Odd Checker

Create a file named **`even_odd.py`**.

### Requirements

Your program should:

- Ask the user to enter a whole number.
- Convert the input into an integer.
- Determine whether the number is even or odd using the modulo operator (`%`).
- Display the appropriate message.

### Sample Input

```text
Enter a number: 17
```

### Expected Output

```text
17 is an Odd number.
```

---

# 🏋️ Exercises

## Exercise 1

Ask the user for their exam score.

- If the score is **50 or higher**, print:

```
You passed!
```

- Otherwise, print:

```
Please try again.
```

### Sample Input

```text
Enter your score: 75
```

### Expected Output

```text
You passed!
```

---

## Exercise 2

Ask the user to enter a password.

- If the password is **`secret`**, print:

```
Welcome
```

- Otherwise, print:

```
Wrong password
```

### Sample Input

```text
Enter password: secret
```

### Expected Output

```text
Welcome
```

---

## Exercise 3

Ask the user to enter a number.

- If the number is **greater than or equal to zero**, print:

```
Positive
```

- Otherwise, print:

```
Negative
```

### Sample Input

```text
Enter a number: -5
```

### Expected Output

```text
Negative
```

---

# ❌ Common Mistakes

## Putting a Condition After `else`

Incorrect:

```python
else number < 0:
```

The `else` statement **never** has a condition.

Correct:

```python
else:
```

---

## Incorrect Indentation

Incorrect:

```python
if number % 2 == 0:
    print("Even")
  else:
    print("Odd")
```

The `if` and `else` statements must be aligned at the same indentation level.

---

## Forgetting the Colon (`:`)

Incorrect:

```python
else
```

Correct:

```python
else:
```

---

# 📝 Summary

Today you learned how to:

- ✅ Use **`if-else`** for binary decision-making.
- ✅ Execute code when a condition is **False**.
- ✅ Use the **modulo operator (`%`)** to determine whether a number is even or odd.
- ✅ Build an Even/Odd Checker.

---

# 🔑 Key Takeaways

- The `else` statement always follows an `if` statement.
- Exactly **one** block of an `if-else` statement is executed.
- The modulo operator (`%`) is commonly used to check whether a number is even or odd.
- Always convert numerical user input using `int()` before performing mathematical operations.

---

# 📖 What's Next?

## Day 007 – `elif` Statements