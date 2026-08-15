# Day 023 - Return Values

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the purpose of the **`return`** keyword.
* Differentiate between **printing** a value and **returning** a value.
* Capture function output into **variables** for later use.
* Return **multiple values** from a single function.
* Build a **Unit Converter** project.

---

## The `return` Statement

In previous lessons, your functions mainly performed actions such as printing information.

However, professional functions often perform a calculation and **send the result back** to the part of the program that called the function.

This is done using the `return` statement.

### Basic Syntax

```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result)
```

Output:

```text
15
```

Here, the function calculates `a + b` and returns the result.

The returned value is then stored in the `result` variable.

---

## Returning vs. Printing

A common point of confusion is the difference between `print()` and `return`.

### `print()`

`print()` displays a value on the screen for the user to see.

The printed value is not automatically available for further calculations.

### `return`

`return` sends a value back to the part of the program that called the function.

The returned value can then be stored, calculated with, or passed to another function.

### Example

```python
def multiply_print(a, b):
    print(a * b)

def multiply_return(a, b):
    return a * b
```

With the first function:

```python
multiply_print(2, 3)
```

The result is displayed, but the function does not return the result for further use.

With the second function:

```python
y = multiply_return(2, 3) + 10
print(y)
```

Output:

```text
16
```

The returned value can be used in another calculation.

### Key Difference

```text
print()  → Displays information
return   → Sends information back to the program
```

---

## Returning Multiple Values

Python allows a function to return multiple values by separating them with commas.

Technically, Python packages these values into a **tuple**.

This connects to the tuples you learned about earlier.

### Example

```python
def get_user_data():
    name = "Alice"
    age = 30

    return name, age

user_name, user_age = get_user_data()

print(user_name)
print(user_age)
```

Output:

```text
Alice
30
```

The returned tuple is automatically unpacked into the two variables.

---

## The `return` Statement Ends a Function

When Python reaches a `return` statement, the function immediately stops executing.

For example:

```python
def check_number(number):
    if number > 0:
        return "Positive"

    return "Not positive"
```

Once a `return` statement is executed, Python leaves the function and sends the value back to the caller.

---

## Exercises

### Exercise 1

Write a function called `square(number)` that returns the square of a number.

Store the result of:

```text
square(4)
```

in a variable and print it.

### Exercise 2

Create a function called `get_full_name(first, last)` that returns the two names joined with a space.

Ensure the first letter of each name is capitalized.

### Exercise 3

Write a function called `min_max(numbers_list)` that returns both the smallest and largest numbers from a list of integers.

---

## Mini Project: Unit Converter

Create a file named:

```text
unit_converter.py
```

This project will use functions with **return values** to convert distances and temperatures.

### Project Requirements

Your program should:

1. Display a conversion menu.
2. Allow the user to select a conversion.
3. Ask the user for the required value.
4. Pass the value to a conversion function.
5. Return the converted result.
6. Store the returned value in a variable.
7. Display the final result.
8. Handle invalid selections.

### Functions to Create

Create a function for converting kilometers to miles:

```text
km_to_miles(km)
```

Create a function for converting Celsius to Fahrenheit:

```text
celsius_to_fahrenheit(c)
```

The functions should **return** their results instead of directly printing them.

> **Challenge:** Build the Unit Converter yourself using functions, parameters, user input, conditional statements, and return values. Try to avoid copying a complete solution.

---

## Common Mistakes

### ❌ Code After `return`

**Cause:** Placing executable code inside a function after a `return` statement.

Once `return` is executed, the function exits immediately.

Example:

```python
def example():
    return 10
    print("This will never run")
```

The `print()` statement will never execute.

---

### ❌ Returning `None`

**Cause:** Forgetting to use the `return` keyword when a function is expected to provide a result.

For example:

```python
def add(a, b):
    result = a + b
```

This function does not explicitly return `result`, so Python returns `None`.

Correct:

```python
def add(a, b):
    result = a + b
    return result
```

---

### ❌ Not Capturing the Result

**Cause:** Calling a function that returns a value without storing or using the result.

For example:

```python
calculate_total(price)
```

If the returned value is not stored or used, you may lose the opportunity to use it later.

Instead:

```python
total = calculate_total(price)
```

Now the returned value is stored in `total`.

---

## Summary

Today you learned how to:

* ✅ Use the **`return`** keyword to send data from functions.
* ✅ Understand the difference between **`print()`** and **`return`**.
* ✅ Store function outputs in **variables**.
* ✅ Use **multiple return values**.
* ✅ Understand that `return` immediately ends a function.
* ✅ Build a functional **Unit Converter**.

---

## Key Takeaways

* The `return` statement is the primary way functions communicate results back to the main program.
* Returning values makes functions more reusable, modular, and useful.
* Returned values can be stored in variables and used in additional calculations.
* A function can return multiple values, which Python packages into a tuple.
* Once Python executes a `return` statement, the function immediately ends.
* A function without an explicit `return` statement returns `None`.

---

## What's Next?

### Day 024 - Scope

Next, you will learn about **scope**, including local and global variables, and how Python determines where variables can be accessed.
