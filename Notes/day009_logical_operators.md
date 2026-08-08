# Day 009 - Logical Operators

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand and use the three **logical operators**: `and`, `or`, and `not`.
- Combine multiple comparison expressions into a single condition.
- Understand how logical operators evaluate Boolean expressions.
- Build a **Login System** using logical operators.

---

# 📚 What are Logical Operators?

Logical operators are used to combine multiple Boolean expressions into a single condition.

Python provides three logical operators:

- `and`
- `or`
- `not`

These operators are commonly used with `if`, `elif`, and `else` statements.

---

# 🔗 The `and` Operator

The **`and`** operator returns **True** only if **both** conditions are `True`.

### Truth Table

| Condition A | Condition B | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Example

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
```

Output:

```text
You can drive.
```

---

# 🔀 The `or` Operator

The **`or`** operator returns **True** if **at least one** condition is `True`.

### Truth Table

| Condition A | Condition B | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Example

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("You can sleep in!")
```

Output:

```text
You can sleep in!
```

---

# 🔄 The `not` Operator

The **`not`** operator reverses a Boolean value.

- `not True` → `False`
- `not False` → `True`

### Example

```python
is_admin = False

if not is_admin:
    print("Access denied.")
```

Output:

```text
Access denied.
```

---

# 🚀 Mini Project - Login System

Create a file named **`login_system.py`**.

### Requirements

Your program should:

- Store a predefined username and password.
- Ask the user to enter a username.
- Ask the user to enter a password.
- Grant access only if **both** the username and password are correct.
- Otherwise, display an access denied message.

### Sample Input

```text
Enter username: admin
Enter password: password123
```

### Expected Output

```text
Login Successful! Welcome back.
```

---

# 🏋️ Exercises

## Exercise 1

Ask the user to enter a number.

Check whether the number is between **1 and 100 (inclusive)** using the `and` operator.

### Sample Input

```text
Enter a number: 75
```

### Expected Output

```text
The number is between 1 and 100.
```

---

## Exercise 2

Create a **Discount Eligibility Checker**.

A customer receives a discount if they are:

- Over **65 years old**, **or**
- A **VIP** member.

### Sample Input

```text
Enter age: 70
Are you a VIP member? no
```

### Expected Output

```text
You are eligible for a discount.
```

---

## Exercise 3

Ask the user to enter some text.

Use the `not` operator to check whether the input is **not empty**.

### Sample Input

```text
Enter some text: Hello
```

### Expected Output

```text
Input accepted.
```

---

# ❌ Common Mistakes

## Using `and` Instead of `or`

Incorrect:

```python
if color == "red" and color == "blue":
```

A variable cannot be `"red"` and `"blue"` at the same time.

Use:

```python
if color == "red" or color == "blue":
```

---

## Comparing Boolean Values Unnecessarily

Instead of:

```python
if is_valid == True:
```

Simply write:

```python
if is_valid:
```

Python already knows `is_valid` contains a Boolean value.

---

## Forgetting Parentheses in Complex Conditions

When combining multiple logical operators, parentheses improve readability.

Example:

```python
if (age >= 18 and has_license) or is_admin:
    print("Access granted.")
```

---

# 📝 Summary

Today you learned how to:

- ✅ Use the **`and`** operator to require multiple conditions.
- ✅ Use the **`or`** operator to allow alternative conditions.
- ✅ Use the **`not`** operator to reverse Boolean values.
- ✅ Build a Login System using logical operators.

---

# 🔑 Key Takeaways

- Logical operators combine multiple conditions into a single expression.
- `and` returns `True` only when **all** conditions are `True`.
- `or` returns `True` when **at least one** condition is `True`.
- `not` reverses a Boolean value.
- Logical operators are essential for writing more powerful conditional statements.

---

# 📖 What's Next?

## Day 010 – `while` Loop