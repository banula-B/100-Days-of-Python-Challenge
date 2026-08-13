# Day 021 - Functions

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the purpose of **functions** in programming.
* Define and call your own functions using the `def` keyword.
* Understand the **DRY (Don't Repeat Yourself)** principle.
* Organize code into reusable blocks.
* Build a **Calculator using Functions**.

---

## What is a Function?

A **function** is a block of organized, reusable code that is used to perform a specific, related action.

Functions provide better modularity and allow code to be reused throughout an application.

You have already been using built-in Python functions such as:

```python
print()
input()
len()
```

### Why Use Functions?

1. **Reusability:** Write code once and use it multiple times.
2. **Organization:** Break complex problems into smaller, manageable pieces.
3. **Readability:** Give meaningful names to blocks of code so their purpose is clear.
4. **Maintainability:** Make programs easier to modify and debug.

---

## Defining and Calling a Function

To define a function, use the `def` keyword followed by the function name and parentheses `()`.

The code inside the function must be indented.

### Basic Syntax

```python
def my_function():
    print("Hello from inside a function!")

# Calling the function
my_function()
```

### Important Concept

Defining a function does **not** immediately execute the code inside it.

The function must be **called** before its code runs.

```python
def greet():
    print("Hello!")

greet()
```

Output:

```text
Hello!
```

---

## The DRY Principle

**DRY** stands for:

> **Don't Repeat Yourself**

The idea is to avoid writing the same code repeatedly.

For example, instead of writing the same greeting logic several times, you can create one function and reuse it:

```python
def greet():
    print("Welcome!")

greet()
greet()
greet()
```

This makes your code shorter, cleaner, and easier to maintain.

---

## Exercises

### Exercise 1

Define a function named `greet_user` that prints:

```text
Welcome to Phase 2: Functions!
```

Call the function to see the output.

### Exercise 2

Create a function called `show_date` that prints today's date.

You can provide the date as a string for now.

### Exercise 3

Write a program that has two functions:

* `start_program()`
* `end_program()`

Call them one after another to simulate a program lifecycle.

---

## Mini Project: Calculator Using Functions

Create a file named:

```text
func_calculator.py
```

The goal of this project is to build a simple calculator using separate functions for different mathematical operations.

Instead of putting all the logic into one large block of code, organize the program into reusable functions.

### Project Requirements

Your calculator should:

1. Display a calculator menu.
2. Allow the user to select an operation.
3. Ask the user for two numbers.
4. Perform the selected calculation.
5. Display the result.
6. Use separate functions for each operation.
7. Display an appropriate message when the user selects an invalid option.

### Suggested Functions

Create separate functions for operations such as:

```text
add()
subtract()
```

You can extend the project later with:

```text
multiply()
divide()
```

> **Challenge:** Try to build the calculator yourself using the concepts learned today instead of copying a complete solution.

---

## Common Mistakes

### ❌ Forgetting the `def` Keyword

**Cause:** Trying to define a function without using the `def` keyword.

Correct:

```python
def greet():
    print("Hello!")
```

### ❌ Forgetting the Parentheses `()`

**Cause:** Writing a function definition without parentheses.

Incorrect:

```python
def greet:
```

Correct:

```python
def greet():
```

When calling a function, parentheses are also required:

```python
greet()
```

### ❌ Defining but Not Calling the Function

**Cause:** Creating the function but never calling it.

For example:

```python
def greet():
    print("Hello!")
```

Nothing will be printed until the function is called:

```python
greet()
```

### ❌ Incorrect Indentation

Python uses indentation to determine which statements belong to a function.

Correct:

```python
def greet():
    print("Hello!")
```

Incorrect:

```python
def greet():
print("Hello!")
```

---

## Summary

Today you learned how to:

* ✅ Transition into **Phase 2: Functions & Data Structures**.
* ✅ Use the **`def`** keyword to create custom functions.
* ✅ Define and call functions.
* ✅ Organize code into reusable blocks.
* ✅ Understand the **DRY principle**.
* ✅ Build a **Calculator using Functions**.

---

## Key Takeaways

* Functions are fundamental building blocks of professional Python programs.
* A function definition creates the instructions, while calling the function executes them.
* Functions help make code more reusable, readable, and maintainable.
* The **DRY principle** encourages you to avoid unnecessary repetition.
* Breaking a large program into smaller functions makes it easier to understand and modify.

---

## What's Next?

### Day 022 - Parameters

Next, you will learn how to pass information into functions using **parameters and arguments**.
