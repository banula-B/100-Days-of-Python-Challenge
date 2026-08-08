# Day 016 - List Methods

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand the difference between a function and a **method**.
- Use methods to **add** elements to a list (`append`, `insert`, `extend`).
- Use methods to **remove** elements from a list (`remove`, `pop`, `clear`).
- **Organise** and **search** lists using `sort`, `reverse`, `index`, and `count`.
- Build a **Student Marks Manager** to track and analyse academic performance.

---

# 📚 What are List Methods?

In Python, a **method** is a function that belongs to an object.

Since a list is an object, it has many built-in methods that allow us to add, remove, search, and organise items.

Methods are called using **dot notation**:

```python
list_name.method()
```

For example:

```python
fruits.append("orange")
```

Here, `.append()` is a list method.

---

# ➕ Adding Elements to a List

Python provides several methods for adding items to lists.

## `.append()`

The `.append()` method adds **one item to the end** of a list.

```python
grades = [75, 80, 85]

grades.append(92)

print(grades)
```

Output:

```text
[75, 80, 85, 92]
```

---

## `.insert()`

The `.insert()` method adds an item at a specific position.

### Syntax

```python
list.insert(index, item)
```

Example:

```python
grades = [75, 80, 85]

grades.insert(1, 88)

print(grades)
```

Output:

```text
[75, 88, 80, 85]
```

---

## `.extend()`

The `.extend()` method adds multiple items from another iterable to the end of a list.

```python
grades = [75, 80, 85]

grades.extend([90, 95])

print(grades)
```

Output:

```text
[75, 80, 85, 90, 95]
```

### Difference Between `append()` and `extend()`

```python
numbers = [1, 2, 3]

numbers.append([4, 5])
```

Result:

```text
[1, 2, 3, [4, 5]]
```

Whereas:

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])
```

Result:

```text
[1, 2, 3, 4, 5]
```

---

# ➖ Removing Elements from a List

Python also provides several methods for removing items.

## `.remove()`

The `.remove()` method removes the **first occurrence** of a specific value.

```python
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")

print(fruits)
```

Output:

```text
['apple', 'cherry', 'banana']
```

---

## `.pop()`

The `.pop()` method removes an item from a list and **returns the removed item**.

Without an index, `.pop()` removes the last item.

```python
fruits = ["apple", "banana", "cherry"]

last_fruit = fruits.pop()

print(last_fruit)
print(fruits)
```

Output:

```text
cherry
['apple', 'banana']
```

You can also provide an index:

```python
fruits.pop(0)
```

This removes the first item.

---

## `.clear()`

The `.clear()` method removes **all items** from a list.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

---

# 🔤 Sorting and Organising Lists

## `.sort()`

The `.sort()` method arranges items in ascending order by default.

```python
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

You can sort in descending order using:

```python
numbers.sort(reverse=True)
```

---

## `.reverse()`

The `.reverse()` method reverses the current order of the list.

```python
numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)
```

Output:

```text
[5, 4, 3, 2, 1]
```

---

# 🔍 Searching Lists

## `.index()`

The `.index()` method returns the index of the **first occurrence** of a value.

```python
fruits = ["apple", "banana", "cherry"]

position = fruits.index("banana")

print(position)
```

Output:

```text
1
```

---

## `.count()`

The `.count()` method tells you how many times a value appears in a list.

```python
numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))
```

Output:

```text
3
```

---

# 📋 List Methods Quick Reference

| Method | Purpose |
|---|---|
| `.append(item)` | Adds an item to the end |
| `.insert(index, item)` | Adds an item at a specific position |
| `.extend(iterable)` | Adds multiple items |
| `.remove(item)` | Removes the first matching item |
| `.pop()` | Removes and returns the last item |
| `.pop(index)` | Removes and returns an item at an index |
| `.clear()` | Removes all items |
| `.sort()` | Sorts the list |
| `.reverse()` | Reverses the list |
| `.index(item)` | Finds the index of an item |
| `.count(item)` | Counts occurrences of an item |

---

# 🚀 Mini Project - Student Marks Manager

Create a file named **`marks_manager.py`**.

### Requirements

Your program should:

- Allow the user to enter student marks.
- Continue accepting marks until the user enters `done`.
- Store the marks in a list.
- Sort the marks from highest to lowest.
- Calculate the class average.
- Display the highest mark.
- Display the lowest mark.

### Sample Input

```text
Enter a student mark (or 'done' to finish): 75
Enter a student mark (or 'done' to finish): 88
Enter a student mark (or 'done' to finish): 92
Enter a student mark (or 'done' to finish): 64
Enter a student mark (or 'done' to finish): 81
Enter a student mark (or 'done' to finish): done
```

### Expected Output

```text
Ranked Marks: [92.0, 88.0, 81.0, 75.0, 64.0]
Class Average: 80.00
Highest Mark: 92.0
Lowest Mark: 64.0
```

---

# 🏋️ Exercises

## Exercise 1

Create a list containing 5 animals.

Use `.insert()` to add a new animal at the second position and `.pop()` to remove the last animal.

### Expected Output

```text
['cat', 'elephant', 'dog', 'rabbit', 'lion']
```

> Your animal choices can be different.

---

## Exercise 2

Create the following list:

```python
numbers = [10, 20, 20, 30, 20, 40]
```

Use `.count()` to find how many times `20` appears.

### Expected Output

```text
20 appears 3 times.
```

---

## Exercise 3

Create a list of names and use `.sort()` to arrange them alphabetically.

### Sample Input

```text
["Charlie", "Alice", "David", "Bob"]
```

### Expected Output

```text
["Alice", "Bob", "Charlie", "David"]
```

---

# ❌ Common Mistakes

## Expecting `.sort()` to Return a New List

A common mistake is:

```python
new_list = old_list.sort()
```

`.sort()` modifies the original list **in place** and returns `None`.

If you need a new sorted list, you can use the `sorted()` function:

```python
new_list = sorted(old_list)
```

---

## `ValueError` with `.remove()`

This happens when you try to remove an item that does not exist.

For example:

```python
numbers = [10, 20, 30]

numbers.remove(50)
```

Python will raise a `ValueError`.

You can check first:

```python
if 50 in numbers:
    numbers.remove(50)
```

---

## Accessing a List After `.clear()`

After calling `.clear()`, the list becomes empty.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

Trying to access an item afterward can cause an `IndexError`.

---

## Confusing `append()` and `extend()`

Remember:

```python
list.append([4, 5])
```

adds the entire list as **one item**.

While:

```python
list.extend([4, 5])
```

adds `4` and `5` as separate items.

---

# 📝 Summary

Today you learned how to:

- ✅ Understand what **list methods** are.
- ✅ Add elements using `.append()`, `.insert()`, and `.extend()`.
- ✅ Remove elements using `.remove()`, `.pop()`, and `.clear()`.
- ✅ Organise lists using `.sort()` and `.reverse()`.
- ✅ Search lists using `.index()` and `.count()`.
- ✅ Build a **Student Marks Manager**.

---

# 🔑 Key Takeaways

- List methods make it easy to manage collections of data.
- `.append()` adds one item to the end of a list.
- `.extend()` adds multiple items to a list.
- `.pop()` removes an item and can return the removed value.
- `.sort()` and `.reverse()` modify the original list.
- Most list methods modify the list **in place**.
- Understanding list methods is important because lists are used frequently in real-world Python programs.

---

# 📖 What's Next?

## Day 017 - Tuples