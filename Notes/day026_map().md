# Day 026 - map()

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the purpose and syntax of the **`map()` function**.
* Apply a function to every item in an **iterable** such as a list or tuple.
* Combine `map()` with **lambda functions** for concise data transformation.
* Understand how `map()` returns an iterator.
* Build a **Temperature Converter** project to process batches of data.

---

## What is the `map()` Function?

The **`map()`** function is a built-in Python function that applies a function to every item in an iterable.

Instead of manually writing a `for` loop to transform every element in a list, `map()` allows you to express the transformation more directly.

### Basic Syntax

```python
map(function, iterable)
```

Where:

* **`function`** → The function that should be applied to each item.
* **`iterable`** → The collection of items to process.

### Example

```python
def double(n):
    return n * 2

numbers = [1, 2, 3, 4, 5]

result = map(double, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8, 10]
```

The `double()` function is applied to every number in the list.

---

## How `map()` Works

Suppose you have:

```python
numbers = [1, 2, 3, 4]
```

and want to double every number.

Without `map()`, you could use a loop:

```python
result = []

for number in numbers:
    result.append(number * 2)
```

With `map()`:

```python
result = list(map(lambda x: x * 2, numbers))
```

Both approaches produce the same transformed data.

The `map()` approach is especially useful when you already have a function that describes the transformation you want to perform.

---

## Using `map()` with Lambda Functions

The `map()` function is frequently combined with **lambda functions**.

This is useful when the transformation is simple enough that you do not need to create a separate named function.

### Example

```python
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))

print(squared)
```

Output:

```text
[1, 4, 9, 16, 25]
```

Here:

```python
lambda x: x ** 2
```

defines the transformation, while:

```python
map(...)
```

applies that transformation to every item.

---

## `map()` Returns an Iterator

In Python 3, `map()` does not immediately return a list.

It returns a **map object**, which is an iterator.

For example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)
```

You will see something similar to:

```text
<map object at 0x...>
```

To see the actual results as a list, convert the map object:

```python
result = list(map(lambda x: x * 2, numbers))

print(result)
```

Output:

```text
[2, 4, 6]
```

---

## Exercises

### Exercise 1

Create a list of strings representing numbers:

```python
["1", "2", "3"]
```

Use `map()` to convert all of them into actual integers.

### Exercise 2

Given a list of names:

```python
["alice", "bob", "charlie"]
```

Use `map()` and a lambda function to capitalize the first letter of each name.

### Exercise 3

Write a program that takes a list of prices and applies a **10% tax** to each price using `map()`.

---

## Mini Project: Temperature Converter

Create a file named:

```text
temp_map.py
```

This project uses `map()` to convert a list of temperatures from **Celsius to Fahrenheit**.

### Project Requirements

Your program should:

1. Create a list of Celsius temperatures.
2. Create a function that converts Celsius to Fahrenheit.
3. Use `map()` to apply the conversion to every temperature.
4. Convert the resulting iterator into a list.
5. Display the original Celsius temperatures.
6. Display the converted Fahrenheit temperatures.

### Conversion Formula

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

### Suggested Function

Create a function named:

```text
to_fahrenheit(c)
```

The function should receive a Celsius temperature and **return** the Fahrenheit temperature.

> **Challenge:** Try using both approaches: first use a regular function with `map()`, then rewrite the transformation using a lambda function.

---

## Common Mistakes

### ❌ Forgetting to Convert the Result to a List

**Cause:** Printing the result of `map()` directly.

For example:

```python
result = map(lambda x: x * 2, numbers)

print(result)
```

You will see something similar to:

```text
<map object at 0x...>
```

This happens because `map()` returns an iterator.

### Solution

Convert the result into a list:

```python
result = list(map(lambda x: x * 2, numbers))
```

---

### ❌ Passing the Function with Parentheses

**Cause:** Calling the function instead of passing the function itself.

Incorrect:

```python
map(my_func(), my_list)
```

Correct:

```python
map(my_func, my_list)
```

When using `map()`, pass the **function itself**.

---

### ❌ Mismatched Arguments

**Cause:** Using a function that requires more arguments than the supplied iterables provide.

For example, a function requiring two arguments needs two corresponding iterables:

```python
def add(a, b):
    return a + b
```

You can use:

```python
map(add, list_a, list_b)
```

rather than providing only one iterable.

---

### ❌ Expecting `map()` to Modify the Original List

`map()` does not change the original iterable.

For example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)
```

The original `numbers` list remains unchanged.

The transformed values are produced separately.

---

## Summary

Today you learned how to:

* ✅ Use **`map()`** to transform collections of data.
* ✅ Understand the syntax of `map(function, iterable)`.
* ✅ Apply functions to every item in an iterable.
* ✅ Combine `map()` with **lambda functions**.
* ✅ Understand that `map()` returns an iterator.
* ✅ Convert a `map` object into a list.
* ✅ Build a **Temperature Converter** that processes multiple values.

---

## Key Takeaways

* `map()` applies a function to every item in an iterable.
* The basic syntax is:

```python
map(function, iterable)
```

* `map()` is commonly combined with lambda functions for simple transformations.
* `map()` returns a **lazy iterator**, meaning the values are produced as they are consumed.
* Use `list()` when you need to materialize the results as a list.
* `map()` does not modify the original list.
* `map()` is useful for transforming collections without manually writing a loop.

---

## What's Next?

### Day 027 - `filter()`

Next, you will learn how to use **`filter()`** to select specific items from a collection based on a condition.
