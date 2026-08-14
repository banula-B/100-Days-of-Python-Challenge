# Day 022 - Parameters

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the difference between **parameters** and **arguments**.
* Define functions that accept **input data**.
* Differentiate between **positional** and **keyword** arguments.
* Use **default parameter values** to make functions more flexible.
* Build an **Area Calculator** project.

---

## Parameters and Arguments

Yesterday, you learned how to create basic functions. Today, you will make them more powerful by allowing them to accept data.

### Parameters

**Parameters** are the variable names listed in a function definition. They act as placeholders for the data the function will receive.

### Arguments

**Arguments** are the actual values passed into a function when it is called.

### Example

```python
def greet(name):  # 'name' is the parameter
    print(f"Hello, {name}!")

greet("Alice")  # "Alice" is the argument
```

In this example:

* `name` → parameter
* `"Alice"` → argument

### Simple Analogy

Think of a function as a machine:

```text
Function → Input → Processing → Output
```

Parameters define what kind of input the machine expects, while arguments are the actual values you provide.

---

## Positional vs. Keyword Arguments

Python allows you to provide function arguments in different ways.

### 1. Positional Arguments

Positional arguments are passed according to the order in which the parameters were defined.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Hamster", "Harry")
```

Here:

```text
"Hamster" → animal_type
"Harry"   → pet_name
```

The order matters.

---

### 2. Keyword Arguments

Keyword arguments are passed by explicitly specifying the parameter name.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Goldie", animal_type="Fish")
```

With keyword arguments, the order does not matter because each value is explicitly associated with a parameter.

---

## Default Parameters

You can provide a default value for a parameter.

If the caller does not provide a value for that parameter, Python automatically uses the default value.

### Example

```python
def make_coffee(size="Medium"):
    print(f"Making a {size} cup of coffee.")

make_coffee()
make_coffee("Large")
```

The first call uses the default value:

```text
Medium
```

The second call provides its own value:

```text
Large
```

### Why Use Default Parameters?

Default parameters are useful when:

* A value is commonly used.
* You want to make a function easier to call.
* You want to provide a fallback value.
* You want your functions to be more flexible.

---

## Exercises

### Exercise 1

Write a function called `favorite_book(title)` that prints:

```text
One of my favorite books is [title].
```

Call it with a real book title.

### Exercise 2

Create a function called `make_shirt(size, message)` that prints a sentence summarizing the size of the shirt and the message printed on it.

Call the function:

1. Once using positional arguments.
2. Once using keyword arguments.

### Exercise 3

Modify the `make_shirt()` function so that:

* The shirt size is `"Large"` by default.
* The message is `"I love Python"` by default.

---

## Mini Project: Area Calculator

Create a file named:

```text
area_calculator.py
```

This project will use functions with parameters to calculate the area of different shapes based on user input.

### Project Requirements

Your program should:

1. Display an area calculator menu.
2. Allow the user to choose a shape.
3. Ask for the required measurements.
4. Pass those measurements into functions as arguments.
5. Calculate the area.
6. Display the result.
7. Use a default parameter for the value of π when calculating a circle.
8. Handle an invalid shape selection.

### Functions to Create

Create a function for calculating the area of a rectangle:

```text
calculate_rectangle(length, width)
```

Create a function for calculating the area of a circle:

```text
calculate_circle(radius, pi=3.14159)
```

> **Challenge:** Try to build the project yourself using parameters, arguments, conditional statements, user input, and functions. Avoid copying a complete solution.

---

## Common Mistakes

### ❌ Missing Arguments

**Cause:** Defining a function with multiple required parameters but providing fewer arguments when calling it.

Example:

```python
def calculate(a, b):
    print(a + b)

calculate(5)
```

Python will raise a `TypeError` because the required `b` argument is missing.

---

### ❌ Positional Argument After Keyword Argument

Incorrect:

```python
func(name="Alice", 25)
```

Positional arguments must come before keyword arguments.

Correct:

```python
func(25, name="Alice")
```

---

### ❌ Confusing Parameters and Arguments

Remember:

> **Parameters** are the placeholders defined in the function.

> **Arguments** are the actual values passed when calling the function.

For example:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

Here:

* `name` is the **parameter**.
* `"Alice"` is the **argument**.

---

## Summary

Today you learned how to:

* ✅ Define functions that accept **inputs**.
* ✅ Understand the difference between **parameters** and **arguments**.
* ✅ Use **positional arguments**.
* ✅ Use **keyword arguments**.
* ✅ Set **default values** for parameters.
* ✅ Build an **Area Calculator** using functions.

---

## Key Takeaways

* Parameters make functions dynamic and reusable for different data.
* Arguments are the actual values supplied to functions.
* Positional arguments depend on the order of parameters.
* Keyword arguments explicitly identify which parameter receives a value.
* Default parameters provide fallback values and make functions easier to use.
* Functions with parameters are an important step toward writing reusable and maintainable Python programs.

---

## What's Next?

### Day 023 - Return Values

Next, you will learn how functions can **return data** instead of simply displaying it with `print()`.
