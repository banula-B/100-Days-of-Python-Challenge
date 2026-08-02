# Day 010 - `while` Loop

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand the purpose and syntax of the **`while` loop`.
- Identify the difference between **definite** and **indefinite** iteration.
- Use loop control variables to avoid **infinite loops**.
- Build a **Countdown Timer** project using a `while` loop.

---

# 📚 What is a `while` Loop?

A **`while` loop** repeatedly executes a block of code **as long as a condition is `True`**.

It is commonly used when you **don't know in advance how many times** the loop should run.

### Basic Syntax

```python
while condition:
    # Code to repeat
```

Before every iteration, Python checks the condition.

- If the condition is **True**, the loop continues.
- If the condition is **False**, the loop stops.

---

# 🔄 Loop Control Variables

A **control variable** is a variable that changes during each iteration of the loop.

Without updating the control variable, the loop may never end.

### Example

```python
count = 1

while count <= 5:
    print("Number:", count)
    count += 1
```

Output:

```text
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

---

# 🔁 Definite vs. Indefinite Iteration

### Definite Iteration

You know exactly how many times the loop should run.

Example:

```text
Print numbers from 1 to 10.
```

This is usually done with a `for` loop (coming in the next lesson).

---

### Indefinite Iteration

You **don't know** how many times the loop should run.

The loop continues until a condition becomes `False`.

Example:

```python
user_input = ""

while user_input.lower() != "quit":
    user_input = input("Type 'quit' to exit: ")
```

The program keeps asking for input until the user types **quit**.

---

# 🚀 Mini Project - Countdown Timer

Create a file named **`countdown.py`**.

### Requirements

Your program should:

- Ask the user to enter a starting number.
- Count down from that number to **0**.
- Display each number on a new line.
- Display **"Blast off!"** after reaching zero.

> **Optional:** Add a one-second delay between each number using the `time` module.

### Sample Input

```text
Enter the starting number: 5
```

### Expected Output

```text
5
4
3
2
1
0
Blast off!
```

---

# 🏋️ Exercises

## Exercise 1

Write a program that prints all **even numbers** from **2 to 20** using a `while` loop.

### Expected Output

```text
2
4
6
8
10
12
14
16
18
20
```

---

## Exercise 2

Create a **Secret Word Game**.

Keep asking the user to enter a word until they correctly guess the secret word:

```
python
```

### Sample Input

```text
Enter the secret word: java
Enter the secret word: html
Enter the secret word: python
```

### Expected Output

```text
Correct! You guessed the secret word.
```

---

## Exercise 3

Write a program that calculates the **sum of all numbers from 1 to 100** using a `while` loop.

### Expected Output

```text
5050
```

---

# ❌ Common Mistakes

## Infinite Loops

Incorrect:

```python
count = 1

while count <= 5:
    print(count)
```

The value of `count` never changes, so the condition always remains `True`.

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Off-by-One Errors

Incorrect:

```python
count = 1

while count < 5:
    print(count)
    count += 1
```

This prints:

```text
1
2
3
4
```

Use `<=` if you want to include **5**.

---

## Incorrect Indentation

Incorrect:

```python
count = 1

while count <= 5:
    print(count)

count += 1
```

The control variable is updated **outside** the loop, causing an infinite loop.

---

# 📝 Summary

Today you learned how to:

- ✅ Use the **`while` loop** for repetitive tasks.
- ✅ Control loops using a **control variable**.
- ✅ Understand the difference between definite and indefinite iteration.
- ✅ Build a Countdown Timer using a `while` loop.

---

# 🔑 Key Takeaways

- A `while` loop continues running **while its condition is `True`**.
- Always update the control variable so the loop can eventually stop.
- `while` loops are ideal when the number of repetitions is unknown.
- Be careful of **infinite loops** caused by conditions that never become `False`.

---

# 📖 What's Next?

## Day 011 – `for` Loop