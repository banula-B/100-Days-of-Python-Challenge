# Day 019 - Sets

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the unique characteristics of **Sets** (unordered, unindexed, and unique elements).
* Create and modify sets using `add()` and `remove()`.
* Perform powerful mathematical set operations like **union** and **intersection**.
* Build a **Duplicate Remover** project to clean up data.

---

## What is a Set?

A **set** is a built-in Python data type used to store multiple items in a single variable. Sets are unique because they are **unordered** (items have no defined order) and **unindexed**. Most importantly, **sets do not allow duplicate values**.

**Basic Syntax:** Sets are written with curly brackets `{}`.

```python
# A set of fruits
fruits = {"apple", "banana", "cherry"}

# Duplicate values are automatically ignored
numbers = {1, 2, 2, 3, 4, 4, 5}

print(numbers)
```

### Expected Output

```text
{1, 2, 3, 4, 5}
```

> **Note:** Since sets are unordered, the order of elements may vary.

---

## Modifying Sets

Since sets are unordered, you cannot access items by referring to an index. However, you can add and remove items.

### `.add(item)`

Adds a single item to the set.

### `.update(iterable)`

Adds multiple items from another collection.

### `.remove(item)`

Removes a specific item. It raises an error if the item does not exist.

### `.discard(item)`

Removes a specific item but does not raise an error if the item does not exist.

**Example:**

```python
colors = {"red", "blue"}

colors.add("green")
colors.discard("yellow")
```

---

## Set Operations

Sets are incredibly useful for mathematical operations between two groups of data.

### Union `|`

Returns a new set containing all unique items from both sets.

### Intersection `&`

Returns a new set containing only the items present in both sets.

### Difference `-`

Returns the items present in the first set but not in the second set.

**Example:**

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
```

### Expected Output

```text
{1, 2, 3, 4, 5}
{3}
{1, 2}
```

> **Note:** The order of set elements may vary.

---

## Exercises

### Exercise 1

Create a set named `my_hobbies` with three hobbies.

Add a fourth hobby to the set using the `.add()` method.

---

### Exercise 2

Given two sets:

```python
set1 = {10, 20, 30}
set2 = {30, 40, 50}
```

Find the **intersection** of the two sets and print the result.

### Expected Output

```text
{30}
```

---

### Exercise 3

Try to create a set that contains a list.

Observe the error and explain why it happened.

**Hint:** Think about **mutability** and **hashable objects**.

---

## Mini Project: Duplicate Remover

Create a file named:

```text
duplicate_remover.py
```

This program takes a list of items that might contain duplicates and uses a **set** to remove all repeating values.

The program should:

1. Store a list containing duplicate items.
2. Convert the list into a set to remove duplicates.
3. Convert the set back into a list.
4. Display the original list.
5. Display the unique items.
6. Display how many duplicate items were removed.

### Sample Input

```text
apple
banana
apple
orange
banana
grape
apple
```

### Expected Output

```text
Original List: ['apple', 'banana', 'apple', 'orange', 'banana', 'grape', 'apple']
Unique Items: ['apple', 'banana', 'orange', 'grape']
Items removed: 3
```

> **Note:** Because sets are unordered, the order of the unique items may be different.

---

## Common Mistakes

### ❌ Attempting to Access a Set by Index

Cause:

```python
my_set[0]
```

Because sets are unordered, they do not support indexing.

**Solution:** Use a `for` loop to iterate through the set or check membership with:

```python
if item in my_set:
```

---

### ❌ Creating an Empty Set with `{}`

Cause:

```python
empty_set = {}
```

This actually creates an empty **dictionary**, not a set.

**Solution:**

```python
empty_set = set()
```

---

### ❌ Including Mutable Items

Cause:

Trying to put a **list** or another **set** inside a set.

Set elements must be **hashable**, which means mutable objects such as lists and sets cannot be stored directly inside another set.

---

## Summary

Today you learned how to:

* ✅ Define and create **Sets** for unique data storage.
* ✅ Use **Set Methods** to modify collections.
* ✅ Perform mathematical operations like **union, intersection, and difference**.
* ✅ Understand why sets do not support indexing.
* ✅ Remove duplicate values using sets.
* ✅ Build a **Duplicate Remover** project.

---

## Key Takeaways

* Sets are the best tool for ensuring data contains **no duplicates**.
* Because sets are unordered, you cannot rely on the position of items.
* Use `.add()` to add a single item.
* Use `.update()` to add multiple items.
* Use `.remove()` or `.discard()` to remove items.
* Use `|` for **union**.
* Use `&` for **intersection**.
* Use `-` for **difference**.
* Set operations can be much more efficient than manually comparing lists using loops.

---

## What's Next?

**Day 020 - Review Week**
