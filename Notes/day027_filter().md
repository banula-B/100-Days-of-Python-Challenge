# Day 027 - filter()

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the purpose and syntax of the **`filter()` function**.
* Extract specific data from an **iterable** based on a condition.
* Combine `filter()` with **lambda functions** for efficient data processing.
* Understand how `filter()` returns an iterator.
* Build an **Even Number Filter** project.

---

## What is the `filter()` Function?

The **`filter()`** function is a built-in Python function used to select elements from an iterable based on a condition.

While `map()` **transforms** every item, `filter()` decides whether each item should be **kept or discarded**.

### Basic Syntax

```python
filter(function, iterable)
```

Where:

* **`function`** → A function that tests each element.
* **`iterable`** → The collection you want to filter.
* The function should return a value that evaluates to `True` or `False`.

If the function returns `True`, the item is kept.

If the function returns `False`, the item is discarded.

---

## Example

Consider a list of ages:

```python
def is_adult(age):
    return age >= 18

ages = [12, 16, 18, 21, 25]

adults = filter(is_adult, ages)

print(list(adults))
```

Output:

```text
[18, 21, 25]
```

The `is_adult()` function checks every age.

Only values where the condition evaluates to `True` are included in the result.

---

## How `filter()` Works

Suppose we have:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

and want only the even numbers.

The filtering condition is:

```python
number % 2 == 0
```

The result is:

```text
[2, 4, 6]
```

The original list is not modified.

Instead, `filter()` produces an iterator containing the elements that satisfy the condition.

---

## Using `filter()` with Lambda Functions

Like `map()`, `filter()` is commonly used with **lambda functions**.

This allows you to define simple filtering logic directly where it is needed.

### Example

```python
numbers = [5, 8, 12, 15, 20, 25]

large_numbers = list(filter(lambda x: x > 10, numbers))

print(large_numbers)
```

Output:

```text
[12, 15, 20, 25]
```

Here:

```python
lambda x: x > 10
```

checks whether each number is greater than `10`.

Only numbers that satisfy the condition are kept.

---

## `filter()` Returns an Iterator

Just like `map()`, `filter()` returns an **iterator** rather than a regular list.

For example:

```python
numbers = [1, 2, 3, 4]

result = filter(lambda x: x % 2 == 0, numbers)

print(result)
```

The output will look similar to:

```text
<filter object at 0x...>
```

To see the actual values as a list:

```python
result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

Output:

```text
[2, 4]
```

---

## Exercises

### Exercise 1

Given the list:

```python
["Alice", "Bob", "Anna", "Dave"]
```

Use `filter()` and a lambda function to create a new list containing only names that start with the letter `"A"`.

### Exercise 2

Create a list of 10 random numbers.

Use `filter()` to extract all numbers that are greater than `50`.

### Exercise 3

Take the following list:

```python
["apple", "", "banana", "", "cherry"]
```

Use `filter()` to remove the empty strings.

**Hint:** In Python, an empty string `""` evaluates to `False`.

---

## Mini Project: Even Number Filter

Create a file named:

```text
even_filter.py
```

This project uses the `filter()` function to process a list of integers and extract only the even numbers.

### Project Requirements

Your program should:

1. Create or receive a list of integers.
2. Create a function called `is_even()`.
3. Check whether each number is even.
4. Use `filter()` to select only even numbers.
5. Convert the result into a list.
6. Display the original list.
7. Display the filtered list of even numbers.

### Suggested Function

Create:

```python
def is_even(n):
    return n % 2 == 0
```

Then use the function with `filter()`.

> **Challenge:** Modify the project so that the user can enter multiple numbers and the program filters the even numbers from the user's input.

---

## Common Mistakes

### ❌ Forgetting to Convert the Result to a List

**Cause:** Printing the result of `filter()` directly.

For example:

```python
result = filter(is_even, numbers)

print(result)
```

You will see something similar to:

```text
<filter object at 0x...>
```

This happens because `filter()` returns an iterator.

### Solution

Convert the result into a list:

```python
result = list(filter(is_even, numbers))
```

---

### ❌ Function Not Returning a Boolean Condition

**Cause:** Using a function with `filter()` that does not properly evaluate the condition.

A filtering function should determine whether an item should be kept.

For example:

```python
def is_even(number):
    return number % 2 == 0
```

The expression evaluates to either:

```text
True
```

or:

```text
False
```

---

### ❌ Confusing `map()` and `filter()`

This is an important distinction.

### `map()`

Use `map()` when you want to **transform** every item.

Example:

```python
numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))
```

Result:

```text
[2, 4, 6]
```

### `filter()`

Use `filter()` when you want to **select specific items**.

Example:

```python
numbers = [1, 2, 3, 4]

result = list(filter(lambda x: x % 2 == 0, numbers))
```

Result:

```text
[2, 4]
```

### Simple Rule

```text
map()    → Change every item
filter() → Keep specific items
```

---

## Summary

Today you learned how to:

* ✅ Use **`filter()`** to selectively extract data from a collection.
* ✅ Create Boolean conditions for filtering.
* ✅ Use **lambda functions** for quick, one-line filtering logic.
* ✅ Understand that `filter()` returns an iterator.
* ✅ Convert a filter object into a list.
* ✅ Build an **Even Number Filter**.

---

## Key Takeaways

* `filter()` extracts elements from an iterable based on a condition.
* The filtering function determines whether each item should be kept.
* `True` means the item is kept.
* `False` means the item is discarded.
* `filter()` returns a lazy iterator.
* Use `list()` when you need to view or store the filtered results as a list.
* `filter()` is useful for data validation, selection, and preprocessing.
* Remember:

```text
map()    → Transform data
filter() → Select data
```

---

## What's Next?

### Day 028 - `reduce()`

Next, you will learn how to use **`reduce()`** to repeatedly combine elements of a collection into a single result.
