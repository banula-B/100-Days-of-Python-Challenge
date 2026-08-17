# Day 025 - Lambda

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand what **Lambda functions** are and how they differ from regular functions.
* Master the **syntax** for creating anonymous, one-line functions.
* Recognize appropriate **use cases** for lambdas, particularly as arguments to other functions.
* Build a **Sort Names** project to organize data using custom logic.

---

## What is a Lambda Function?

A **lambda function** is a small, anonymous function in Python.

It is called **anonymous** because it is defined without a traditional function name using the `def` keyword.

Lambda functions are designed for short, simple pieces of logic that are usually needed only in one place.

### Basic Syntax

```python id="l0y9k3"
lambda arguments: expression
```

A lambda function:

* Can accept any number of arguments.
* Contains only **one expression**.
* Automatically returns the result of that expression.
* Does not require the `return` keyword.

### Example

A regular function:

```python id="w8zj3e"
def square_def(x):
    return x * x
```

The equivalent lambda:

```python id="5b0z2y"
square_lambda = lambda x: x * x
```

Both can be called in the same way:

```python id="xv6h0h"
print(square_def(5))
print(square_lambda(5))
```

Output:

```text id="4y7k2q"
25
25
```

---

## Why Use Lambdas?

Lambdas are particularly useful when you need a **small function temporarily**, especially when passing a function as an argument to another function.

Common places where lambdas are useful include:

* `sort()`
* `sorted()`
* `map()`
* `filter()`

They allow you to write simple logic without defining a separate function using `def`.

---

## Lambda with Multiple Arguments

A lambda can accept multiple arguments.

For example:

```python id="w1q5g0"
add = lambda a, b, c: a + b + c

print(add(5, 6, 2))
```

Output:

```text id="d9q2ai"
13
```

The lambda accepts three arguments and returns their sum.

---

## Lambda vs. Regular Function

| Regular Function                | Lambda Function             |
| ------------------------------- | --------------------------- |
| Uses `def`                      | Uses `lambda`               |
| Usually has a name              | Usually anonymous           |
| Can contain multiple statements | Contains one expression     |
| Better for complex logic        | Best for simple logic       |
| Easier to document and maintain | Useful for short operations |

### General Rule

Use a **regular function** when the logic is complex or needs to be reused.

Use a **lambda** when the operation is short, simple, and used temporarily.

---

## Exercises

### Exercise 1

Write a lambda function that takes one argument and returns that number multiplied by `10`.

### Exercise 2

Create a lambda function that takes two numbers and returns the first number raised to the power of the second number.

For example:

```text
a^b
```

### Exercise 3

Write a lambda function that returns:

* `True` if a given number is even.
* `False` if the number is odd.

---

## Mini Project: Sort Names

Create a file named:

```text
sort_names.py
```

This project demonstrates how to use a lambda function as a custom sorting key.

The program should take a list of full names and sort them alphabetically by their **last name** instead of their first name.

### Project Requirements

Your program should:

1. Create a list containing several full names.
2. Display the original list.
3. Sort the names alphabetically by last name.
4. Use a lambda function as the sorting key.
5. Display the sorted list.

### Key Concept

The lambda function should:

1. Receive a full name.
2. Split the name into individual words.
3. Select the last word.
4. Use that word as the sorting key.

For example:

```text
"Zoe Smith"
```

becomes:

```text
["Zoe", "Smith"]
```

The last element is:

```text
"Smith"
```

This allows the names to be sorted by surname.

> **Challenge:** Build the project yourself using `.sort()`, `lambda`, `split()`, and list operations. Try to avoid copying a complete solution.

---

## Common Mistakes

### ❌ Trying to Write Multiple Statements

**Cause:** Treating a lambda like a regular multi-line function.

Lambdas are limited to a **single expression**.

For example, this is not appropriate:

```text
lambda x:
    statement_1
    statement_2
```

For complex logic, use a regular `def` function instead.

---

### ❌ Overusing Lambdas

**Cause:** Using a lambda for an operation that is too complex to understand easily.

If a lambda becomes difficult to read, replace it with a regular function.

For example, instead of creating complicated lambda logic, use:

```python id="5k7q6b"
def calculate_result(value):
    # Complex logic here
    return value
```

Readable code is more important than writing the shortest possible code.

---

### ❌ Assigning Lambdas to Variables

It is possible to write:

```python id="3u1k9s"
my_func = lambda x: x + 1
```

However, when you need a named, reusable function, a regular `def` function is generally preferred.

A better approach is:

```python id="9p6tq8"
def my_func(x):
    return x + 1
```

Lambdas are most useful when used directly as short, temporary functions.

---

## Summary

Today you learned how to:

* ✅ Create **anonymous functions** using the `lambda` keyword.
* ✅ Understand lambda function syntax.
* ✅ Create one-line functions.
* ✅ Use lambdas with multiple arguments.
* ✅ Use lambdas as custom sorting keys.
* ✅ Build a **Sort Names** utility.

---

## Key Takeaways

* Lambdas are small, anonymous functions designed for simple operations.
* The basic syntax is:

```python
lambda arguments: expression
```

* A lambda can accept multiple arguments.
* A lambda contains a single expression whose result is automatically returned.
* Lambdas are especially useful with functions such as `sort()`, `map()`, and `filter()`.
* Use regular `def` functions when logic becomes complex or needs to be clearly named and reused.
* Readability should always be prioritized over unnecessarily short code.

---

## What's Next?

### Day 026 - `map()`

Next, you will learn how to use **`map()`** to apply a function to every item in an iterable.
