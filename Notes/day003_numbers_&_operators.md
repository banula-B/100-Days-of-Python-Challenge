# Day 003 - Numbers and Operators

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Distinguish between integers and floating-point numbers.
- Perform mathematical calculations using arithmetic operators.
- Understand and apply operator precedence (PEMDAS).
- Build a Simple Calculator project using the concepts learned.

---

# 📚 Numeric Types in Python

Python mainly uses two numeric data types.

## Integer (`int`)

Integers are whole numbers without decimal points.

Examples:

- `10`
- `25`
- `-5`
- `0`

Example:

```python
age = 25

print(age)
```

Output:

```text
25
```

---

## Float (`float`)

Floats are numbers that contain decimal points.

Examples:

- `19.99`
- `10.5`
- `-0.2`

Example:

```python
price = 19.99

print(price)
```

Output:

```text
19.99
```

---

# ➕ Arithmetic Operators

Python provides several arithmetic operators for performing mathematical calculations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulo | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
13
7
30
3.3333333333333335
3
1
1000
```

---

# 🧮 Operator Precedence (PEMDAS)

Python follows the same order of operations as mathematics.

1. Parentheses `()`
2. Exponents `**`
3. Multiplication, Division, Floor Division, Modulo
4. Addition and Subtraction

Example:

```python
result = (2 + 3) * 5

print(result)
```

Output:

```text
25
```

---

# 🔄 Type Conversion for Calculations

The `input()` function always returns a **string**.

To perform mathematical calculations, convert the input to a number using:

- `int()` for whole numbers.
- `float()` for decimal numbers.

Example:

```python
number = float(input("Enter a number: "))

print(number * 2)
```

---

# 🏋️ Exercises

## Exercise 1

Calculate the remainder when **10** is divided by **3** using the modulo operator.

### Expected Output

```text
1
```

---

## Exercise 2

Write a program that calculates the area of a rectangle.

Formula:

```
Area = Length × Width
```

### Sample Input

```text
Enter length: 8
Enter width: 5
```

### Expected Output

```text
Area: 40
```

---

## Exercise 3

Use the exponentiation operator to calculate **2 to the power of 10**.

### Expected Output

```text
1024
```

---
# 🚀 Mini Project - Simple Calculator

Create a file named **`calculator.py`**.

### Requirements

Your program should:

- Ask the user to enter two numbers.
- Convert the inputs into numbers.
- Display the following results:
  - Addition
  - Subtraction
  - Multiplication
  - Division

### Sample Input

```text
Enter first number: 10
Enter second number: 5
```

### Expected Output

```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

---

# ❌ Common Mistakes

## Dividing by Zero

```python
10 / 0
```

This causes a `ZeroDivisionError` because Python cannot divide by zero.

---

## Mixing Strings and Numbers

Incorrect:

```python
number = input("Enter a number: ")

print(number + 5)
```

Remember to convert the input using `int()` or `float()` before performing calculations.

---

## Forgetting Operator Precedence

```python
2 + 3 * 5
```

Python performs multiplication before addition.

Use parentheses when you want a different order.

---

# 📝 Summary

Today you learned how to:

- ✅ Identify integers and floats.
- ✅ Perform mathematical calculations using arithmetic operators.
- ✅ Understand operator precedence (PEMDAS).
- ✅ Convert user input into numbers.
- ✅ Build a Simple Calculator.

---

# 🔑 Key Takeaways

- Python supports both integers (`int`) and floating-point numbers (`float`).
- Arithmetic operators make mathematical calculations easy.
- Division (`/`) always returns a float.
- Convert user input to numbers before performing calculations.
- Parentheses help control the order of operations.

---

# 📖 What's Next?

## Day 004 – Type Conversion