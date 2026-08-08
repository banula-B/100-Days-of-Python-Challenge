# Day 004 - Type Conversion

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand why **type conversion** (typecasting) is necessary in Python.
- Identify the difference between **implicit** and **explicit** type conversion.
- Use built-in functions like `int()`, `float()`, and `str()` to change data types.
- Build a **BMI Calculator** that processes numerical user input.

---

# 📚 What is Type Conversion?

Type conversion is the process of changing a value from one data type to another.

Since the `input()` function always returns a **string**, you often need to convert that string into a number before performing calculations.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

---

# 🔄 Implicit Type Conversion

Implicit type conversion happens automatically when Python converts one data type to another to avoid losing information.

Example:

```python
num_int = 10
num_float = 1.5

result = num_int + num_float

print(result)
print(type(result))
```

Output:

```text
11.5
<class 'float'>
```

Python automatically converts the integer into a float before performing the calculation.

---

# ✍️ Explicit Type Conversion

Explicit type conversion is when you manually convert one data type into another using Python's built-in functions.

Common conversion functions:

| Function | Description | Example |
|----------|-------------|---------|
| `int()` | Converts a value to an integer | `int("25")` |
| `float()` | Converts a value to a float | `float("10.5")` |
| `str()` | Converts a value to a string | `str(100)` |

---

## Using `int()`

```python
number = int("25")

print(number)
print(type(number))
```

Output:

```text
25
<class 'int'>
```

---

## Using `float()`

```python
price = float("19.99")

print(price)
print(type(price))
```

Output:

```text
19.99
<class 'float'>
```

---

## Using `str()`

```python
age = 20

text = str(age)

print(text)
print(type(text))
```

Output:

```text
20
<class 'str'>
```

---

# 💬 Converting User Input

Remember:

The `input()` function always returns a **string**.

If you want to perform mathematical calculations, convert the input first.

Example:

```python
age = int(input("Enter your age: "))

print(age + 1)
```

Output (Example):

```text
Enter your age: 20
21
```

---

# 🏋️ Exercises

## Exercise 1

Ask the user for two whole numbers, add them together, and display the result.

### Sample Input

```text
Enter first number: 10
Enter second number: 20
```

### Expected Output

```text
30
```

---

## Exercise 2

Ask the user to enter a decimal number. Convert it to an integer and print the result.

Observe what happens to the decimal part.

### Sample Input

```text
Enter a decimal number: 15.9
```

### Expected Output

```text
15
```

---

## Exercise 3

Ask the user for their birth year. Calculate their age and display the following message:

```
You are [age] years old.
```

### Sample Input

```text
Enter your birth year: 2005
```

### Expected Output

```text
You are 21 years old.
```

> *Assuming the current year is 2026.*

---
# 🚀 Mini Project - BMI Calculator

Create a file named **`bmi_calculator.py`**.

### Requirements

Your program should:

- Ask the user for their height in meters.
- Ask the user for their weight in kilograms.
- Convert both inputs into floating-point numbers.
- Calculate the BMI using the formula:

```
BMI = Weight / (Height × Height)
```

- Display the calculated BMI.

### Sample Input

```text
Enter your height (meters): 1.75
Enter your weight (kg): 70
```

### Expected Output

```text
Your BMI is: 22.86
```

> **Note:** The exact decimal value may vary depending on formatting.

---

# ❌ Common Mistakes

## Mixing Strings and Numbers

Incorrect:

```python
age = 20

print("Your age is " + age)
```

This causes a **TypeError** because Python cannot combine a string and an integer directly.

Correct:

```python
print("Your age is " + str(age))
```

---

## Invalid Integer Conversion

Incorrect:

```python
number = int("10.5")
```

This causes a **ValueError** because `"10.5"` is not a valid integer.

Use `float()` instead:

```python
number = float("10.5")
```

---

## Forgetting to Convert User Input

Incorrect:

```python
age = input("Enter your age: ")

print(age + 1)
```

Remember that `input()` returns a string.

Convert it before performing calculations.

---

# 📝 Summary

Today you learned how to:

- ✅ Differentiate between implicit and explicit type conversion.
- ✅ Use the `int()`, `float()`, and `str()` functions.
- ✅ Convert user input into the correct data type.
- ✅ Build a BMI Calculator using type conversion.

---

# 🔑 Key Takeaways

- Type conversion changes a value from one data type to another.
- Python automatically performs some conversions (implicit conversion).
- You can manually convert values using `int()`, `float()`, and `str()`.
- User input always arrives as a string.
- Always convert user input before performing calculations.

---

# 📖 What's Next?

## Day 005 – `if` Statements