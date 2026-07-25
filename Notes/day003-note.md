# Day 003 - Numbers and Operators

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Distinguish between different numeric types (**integers** and **floats**).
- Perform mathematical calculations using arithmetic operators.
- Understand and apply operator precedence (PEMDAS).
- Build a **Simple Calculator** project using the concepts learned.

---

# 📚 Numeric Types in Python

Python primarily uses two numeric data types:

## Integer (`int`)

Integers are whole numbers without decimal points.

Examples:

- `10`
- `25`
- `-5`
- `0`

```python
age = 25
temperature = -5

print(age)
print(temperature)
```

---

## Float (`float`)

Floats are numbers that contain decimal points.

Examples:

- `19.99`
- `10.5`
- `-0.2`

```python
price = 19.99
height = 175.5

print(price)
print(height)
```

---

## Example

```python
age = 25          # Integer
price = 19.99     # Float

print(age)
print(price)
```

**Output**

```text
25
19.99
```

---

# ➕ Arithmetic Operators

Operators allow you to perform mathematical calculations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulo (Remainder) | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

---

## Example

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Exponent:", a ** b)
```

**Output**

```text
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulo: 1
Exponent: 1000
```

---

# 🧮 Operator Precedence (PEMDAS)

Python follows the same order of operations as mathematics.

The order is:

1. Parentheses `()`
2. Exponents `**`
3. Multiplication `*`, Division `/`, Floor Division `//`, Modulo `%`
4. Addition `+` and Subtraction `-`

---

## Example 1

```python
result = 2 + 3 * 5

print(result)
```

**Output**

```text
17
```

Python performs multiplication first.

---

## Example 2

```python
result = (2 + 3) * 5

print(result)
```

**Output**

```text
25
```

The parentheses are evaluated first.

---

# 🔄 Converting User Input to Numbers

Remember:

`input()` always returns a **string**.

To perform calculations, convert the input to a number using:

- `int()` for whole numbers
- `float()` for decimal numbers

Example:

```python
age = int(input("Enter your age: "))

print(age + 1)
```

Or with decimal numbers:

```python
price = float(input("Enter a price: "))

print(price * 2)
```

---

# 🚀 Mini Project: Simple Calculator

Create a file named **`calculator.py`**.

The program should:

1. Ask the user for two numbers.
2. Convert them to numbers.
3. Display the results of different arithmetic operations.

## Example Code

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulo:", num1 % num2)
print("Exponent:", num1 ** num2)
```

### Sample Output

```text
Enter first number: 10
Enter second number: 3

Addition: 13.0
Subtraction: 7.0
Multiplication: 30.0
Division: 3.3333333333333335
Floor Division: 3.0
Modulo: 1.0
Exponent: 1000.0
```

---

# 🏋️ Exercises

## Exercise 1

Calculate the remainder of **10 divided by 3** using the modulo operator.

Example:

```python
print(10 % 3)
```

Expected Output:

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

Example:

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area:", area)
```

---

## Exercise 3

Use the exponentiation operator to calculate **2 to the power of 10**.

Example:

```python
print(2 ** 10)
```

Expected Output:

```text
1024
```

---

# ❌ Common Mistakes

## 1. Dividing by Zero

Incorrect:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

Python cannot divide by zero.

---

## 2. Incorrect Data Types

Incorrect:

```python
number = input("Enter a number: ")

print(number + 5)
```

This causes a **TypeError** because you're trying to add a string and an integer.

Correct:

```python
number = int(input("Enter a number: "))

print(number + 5)
```

---

## 3. Forgetting Operator Precedence

Incorrect expectation:

```python
print(2 + 3 * 5)
```

Some beginners expect `25`, but the result is:

```text
17
```

Use parentheses when necessary:

```python
print((2 + 3) * 5)
```

---

# 📝 Summary

Today you learned how to:

- ✅ Identify integers and floats.
- ✅ Perform mathematical calculations using arithmetic operators.
- ✅ Understand the order of operations (PEMDAS).
- ✅ Convert user input into numbers.
- ✅ Build a Simple Calculator.

---

# 🔑 Key Takeaways

- Python has two common numeric types: **integers** and **floats**.
- Arithmetic operators make calculations simple and powerful.
- Division (`/`) always returns a **float**.
- Use `int()` or `float()` to convert user input before performing calculations.
- Parentheses help control the order in which calculations are performed.

---

# 💻 Challenge (Optional)

Upgrade your calculator by adding:

- Floor Division (`//`)
- Modulo (`%`)
- Exponentiation (`**`)

Then make it display the results in a clean format like this:

```text
===== Simple Calculator =====

Addition       : 13
Subtraction    : 7
Multiplication : 30
Division       : 3.3333333333333335
Floor Division : 3
Modulo         : 1
Exponent       : 1000
```

---

# 📖 What's Next?

## Day 004 – Type Conversion

In the next lesson, you'll learn about:

- Converting between data types
- `int()`
- `float()`
- `str()`
- `bool()`
- Why type conversion is important
- Building a BMI Calculator using type conversion