# Day 015 - Lists

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand what **Lists** are and why they are used.
- Create and access elements in a list using **indexing**.
- Understand **mutability** and how to modify list items.
- Use **list slicing** to access portions of a list.
- Build a **Shopping List** project to manage a collection of items.

---

# 📚 What is a List?

In Python, a **list** is a built-in data type used to store multiple items in a single variable.

Lists are:

- **Ordered** - Items have a defined order.
- **Changeable (Mutable)** - Items can be modified after the list is created.
- **Allow duplicates** - The same value can appear multiple times.

### Basic Syntax

Lists are created using square brackets `[]`.

```python
# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list of integers
numbers = [10, 20, 30, 40]

# A list containing different data types
mixed_list = ["Python", 100, True, 3.14]
```

---

# 🔢 Accessing Items - Indexing

List items are accessed using their **index**.

Python uses **zero-based indexing**, meaning:

- First item → index `0`
- Second item → index `1`
- Third item → index `2`

### Example

```python
colors = ["red", "green", "blue"]

print(colors[0])
print(colors[2])
```

Output:

```text
red
blue
```

---

# 🔙 Negative Indexing

Python also supports **negative indexing**.

Negative indexes start from the end of the list:

- Last item → `-1`
- Second-to-last item → `-2`
- Third-to-last item → `-3`

### Example

```python
colors = ["red", "green", "blue"]

print(colors[-1])
```

Output:

```text
blue
```

---

# 🔄 Modifying Lists - Mutability

Lists are **mutable**, which means you can change their items after creating the list.

### Example

```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "blueberry"

print(fruits)
```

Output:

```text
['apple', 'blueberry', 'cherry']
```

The item at index `1` was changed from `"banana"` to `"blueberry"`.

---

# ✂️ List Slicing

**Slicing** allows you to access a portion of a list.

### Basic Syntax

```python
list[start:stop]
```

The `stop` index is **not included**.

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

You can also omit the start or stop value:

```python
numbers[:3]
```

```text
[10, 20, 30]
```

And:

```python
numbers[2:]
```

```text
[30, 40, 50]
```

---

# 🚀 Mini Project - Shopping List

Create a file named **`shopping_list.py`**.

### Requirements

Your program should:

- Start with an empty shopping list.
- Ask the user to enter items one by one.
- Add each item to the list.
- Stop asking for items when the user types **`done`**.
- Display the final shopping list.

### Sample Input

```text
Add item: Rice
Add item: Milk
Add item: Eggs
Add item: Bread
Add item: done
```

### Expected Output

```text
Your Final Shopping List:
- Rice
- Milk
- Eggs
- Bread
```

---

# 🏋️ Exercises

## Exercise 1

Create a list containing your **top 3 favorite movies**.

Print the second movie in the list.

### Expected Output

```text
Your second favorite movie is: Inception
```

> Your movie choice can be different.

---

## Exercise 2

Create the following list:

```python
numbers = [10, 20, 30, 40, 50]
```

Change the value `30` to `35`.

### Expected Output

```text
[10, 20, 35, 40, 50]
```

---

## Exercise 3

Create a program that asks the user for **5 numbers**, stores them in a list, and calculates their sum.

### Sample Input

```text
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter number 4: 40
Enter number 5: 50
```

### Expected Output

```text
The sum is: 150
```

---

# ❌ Common Mistakes

## IndexError: List Index Out of Range

This happens when you try to access an index that doesn't exist.

For example:

```python
numbers = [10, 20, 30]

print(numbers[3])
```

The list only has indexes:

```text
0
1
2
```

Remember:

> List indexing starts at `0` and ends at `length - 1`.

---

## Confusing `append()` with Assignment

To add an item to the end of a list, use:

```python
my_list.append("item")
```

Do not replace the entire list with:

```python
my_list = "item"
```

The second example replaces the list with a string.

---

## Forgetting Square Brackets

Correct:

```python
fruits = ["apple", "banana", "cherry"]
```

Be careful with:

```python
fruits = "apple", "banana", "cherry"
```

The second example creates a **tuple**, not a list.

---

# 📝 Summary

Today you learned how to:

- ✅ Create and use **Lists**.
- ✅ Access list items using **indexing**.
- ✅ Use **negative indexing**.
- ✅ Modify list items because lists are mutable.
- ✅ Use **list slicing** to access portions of a list.
- ✅ Build a dynamic **Shopping List** application.

---

# 🔑 Key Takeaways

- Lists are one of Python's most commonly used data structures.
- Lists are **ordered and mutable**.
- Python uses **zero-based indexing**.
- Negative indexes allow you to access items from the end of a list.
- List slicing allows you to retrieve a portion of a list.
- Lists can contain different data types and duplicate values.

---

# 📖 What's Next?

## Day 016 - List Methods