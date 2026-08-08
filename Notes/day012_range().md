# Day 012 - `range()`

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand the purpose of the **`range()` function**.
- Use `range()` with one, two, or three parameters.
- Understand that the **stop value is exclusive**.
- Combine `range()` with `for` loops to automate repetitive tasks.
- Build a **Pattern Printer** project.

---

# 📚 What is the `range()` Function?

The **`range()`** function is a built-in Python function that generates a sequence of numbers.

It is commonly used with `for` loops when you need to repeat an action a specific number of times.

### Basic Syntax

```python
range(start, stop, step)
```

Where:

- **start** → The first number in the sequence.
- **stop** → The number where the sequence ends (**not included**).
- **step** → The amount to increase (or decrease) each time.

---

# 1️⃣ Using `range(stop)`

If only one argument is provided, Python starts from **0**.

### Example

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

# 2️⃣ Using `range(start, stop)`

You can specify both the starting and ending values.

### Example

```python
for i in range(5, 10):
    print(i)
```

Output:

```text
5
6
7
8
9
```

---

# 3️⃣ Using `range(start, stop, step)`

The **step** value determines how much the number changes after each iteration.

### Example

```python
for i in range(0, 10, 2):
    print(i)
```

Output:

```text
0
2
4
6
8
```

You can also count backwards.

### Example

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

---

# ⚠️ The Stop Value is Exclusive

One of the most important things to remember is that the **stop value is not included**.

### Example

```python
for i in range(1, 5):
    print(i)
```

Output:

```text
1
2
3
4
```

Notice that **5 is not printed**.

If you want to include 5, use:

```python
range(1, 6)
```

---

# 🚀 Mini Project - Pattern Printer

Create a file named **`pattern_printer.py`**.

### Requirements

Your program should:

- Ask the user for the number of rows.
- Print a triangle pattern using `*`.
- Use a `for` loop together with `range()`.

### Sample Input

```text
How many rows? 5
```

### Expected Output

```text
*
**
***
****
*****
```

---

# 🏋️ Exercises

## Exercise 1

Use `range()` to print the numbers from **10 down to 1**.

### Expected Output

```text
10
9
8
7
6
5
4
3
2
1
```

---

## Exercise 2

Use `range()` to print all multiples of **5** between **5 and 50** (inclusive).

### Expected Output

```text
5
10
15
20
25
30
35
40
45
50
```

---

## Exercise 3

Ask the user to enter a number.

Print the **sum of all numbers** from **1** to that number.

### Sample Input

```text
Enter a number: 10
```

### Expected Output

```text
55
```

---

# ❌ Common Mistakes

## Expecting the Stop Value to be Included

Incorrect expectation:

```python
range(1, 5)
```

Output:

```text
1
2
3
4
```

Remember: **5 is excluded**.

---

## Using Decimal Numbers

Incorrect:

```python
range(0, 1.5, 0.5)
```

`range()` only accepts **integers**.

---

## Using the Wrong Step Direction

Incorrect:

```python
range(1, 10, -1)
```

The loop will not run because the numbers cannot increase with a negative step.

Correct:

```python
range(10, 0, -1)
```

---

# 📝 Summary

Today you learned how to:

- ✅ Generate number sequences using `range()`.
- ✅ Use the `start`, `stop`, and `step` parameters.
- ✅ Understand that the stop value is excluded.
- ✅ Combine `range()` with `for` loops.
- ✅ Build a Pattern Printer project.

---

# 🔑 Key Takeaways

- `range()` is mainly used with `for` loops.
- The default values are:
  - **start = 0**
  - **step = 1**
- The **stop** value is **never included**.
- A negative step allows you to count backwards.
- `range()` is memory-efficient because it generates numbers only when needed.

---

# 📖 What's Next?

## Day 013 – Nested Loops