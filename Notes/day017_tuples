# Day 017 - Tuples

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand what **Tuples** are and how they differ from Lists.
- Understand the concept of **immutability**.
- Perform **tuple packing and unpacking**.
- Access tuple elements using indexing.
- Build a **Coordinate Calculator** using fixed data points.

---

# 📚 What is a Tuple?

A **tuple** is a collection that is:

- **Ordered** - Items have a defined order.
- **Immutable** - Items cannot be changed after the tuple is created.
- **Allow duplicates** - The same value can appear multiple times.

Tuples are commonly used when you want to store data that should remain unchanged.

### Basic Syntax

Tuples are usually written using round brackets `()`.

```python
dimensions = (1920, 1080)

colors = ("red", "green", "blue")
```

### Single-Item Tuple

A tuple containing only one item requires a **trailing comma**.

```python
single_item = ("Apple",)
```

Without the comma:

```python
single_item = ("Apple")
```

Python treats this as a string, not a tuple.

---

# 🔒 Immutability

The main difference between a list and a tuple is that a tuple is **immutable**.

Once a tuple is created, you cannot:

- Add items.
- Remove items.
- Change existing items.

### Example

```python
my_tuple = (1, 2, 3)
```

Trying to change an item:

```python
my_tuple[0] = 10
```

will result in a `TypeError`.

---

# 📋 List vs Tuple

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[]` | `()` |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Can contain duplicates | Yes | Yes |
| Can change elements | Yes | No |
| Common use | Data that changes | Fixed data |

### When should you use a Tuple?

Use a tuple when the data should remain constant.

Examples include:

```python
screen_size = (1920, 1080)
rgb_color = (255, 0, 0)
coordinates = (10, 20)
```

---

# 🔢 Accessing Tuple Items

Tuples use indexing just like lists.

```python
colors = ("red", "green", "blue")

print(colors[0])
print(colors[2])
```

Output:

```text
red
blue
```

Negative indexing can also be used:

```python
colors[-1]
```

Output:

```text
blue
```

---

# 📦 Tuple Packing

**Tuple packing** happens when multiple values are grouped together into a tuple.

```python
point = 10, 20
```

Python automatically creates:

```python
point = (10, 20)
```

---

# 📤 Tuple Unpacking

**Tuple unpacking** allows you to assign the values of a tuple to separate variables.

```python
point = (10, 20)

x, y = point

print(x)
print(y)
```

Output:

```text
10
20
```

The number of variables must match the number of values being unpacked.

---

# 🏋️ Exercises

## Exercise 1

Create a tuple called `my_info` containing your:

- Name
- Age
- Favorite color

Print the entire tuple.

### Expected Output

```text
('Bob', 21, 'Blue')
```

> Your information can be different.

---

## Exercise 2

Create a tuple containing three values.

Try to change the second item and observe the error Python produces.

### Expected Output

```text
TypeError
```

---

## Exercise 3

Create a tuple representing an RGB color:

```text
(255, 0, 0)
```

Unpack the values into:

- `red`
- `green`
- `blue`

Then print the three values.

### Expected Output

```text
Red: 255
Green: 0
Blue: 0
```

---

# 🚀 Mini Project - Coordinate Calculator

Create a file named **`coordinate_calc.py`**.

### Requirements

Your program should:

- Store two coordinate points as tuples.
- Unpack the coordinates into separate variables.
- Calculate the **Manhattan Distance** between the two points.
- Display both points and the calculated distance.

### Manhattan Distance

The formula is:

```text
Distance = |x1 - x2| + |y1 - y2|
```

### Sample Input

The program uses the following fixed coordinates:

```text
Point A: (5, 10)
Point B: (15, 2)
```

### Expected Output

```text
Point A: (5, 10)
Point B: (15, 2)
The Manhattan Distance between the points is: 18
```

---

# ❌ Common Mistakes

## Forgetting the Comma for a Single-Item Tuple

Incorrect:

```python
item = ("Apple")
```

This creates a string.

Correct:

```python
item = ("Apple",)
```

The comma tells Python that it is a tuple.

---

## Trying to Modify a Tuple

This will cause an error:

```python
my_tuple = (1, 2, 3)

my_tuple[0] = 10
```

Tuples are immutable, so their values cannot be changed after creation.

---

## Trying to Use List Methods on Tuples

Tuples do not support list methods such as:

```python
.append()
.remove()
.pop()
```

because tuples cannot be modified.

---

## Unpacking the Wrong Number of Values

If a tuple contains three values:

```python
rgb = (255, 0, 0)
```

you need three variables:

```python
red, green, blue = rgb
```

Trying to use only two variables will result in a `ValueError`.

---

# 📝 Summary

Today you learned how to:

- ✅ Create and use **Tuples**.
- ✅ Access tuple elements using indexing.
- ✅ Understand **immutability**.
- ✅ Perform **tuple packing and unpacking**.
- ✅ Understand the differences between Lists and Tuples.
- ✅ Build a **Coordinate Calculator**.

---

# 🔑 Key Takeaways

- Tuples are **ordered and immutable** collections.
- Use a **List** when your data needs to change.
- Use a **Tuple** when your data should remain constant.
- Tuple indexing works the same way as list indexing.
- A single-item tuple requires a trailing comma.
- Tuple unpacking allows you to easily assign tuple values to variables.
- Immutability can help protect important data from accidental modification.

---

# 📖 What's Next?

## Day 018 - Dictionaries