# Day 039 - Random Module

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the purpose of Python's built-in **`random`** module.
* Generate random integers, floats, and selections from lists.
* Understand **pseudorandomness** and the importance of seed values.
* Manipulate collections randomly using shuffling and sampling.
* Build a **Dice Simulator** project.

---

# What is the `random` Module?

The **`random`** module is a built-in Python library used to generate pseudorandom numbers and make random selections.

It is useful when building:

* Games.
* Simulations.
* Random selection tools.
* Testing programs.
* Randomised algorithms.
* Simple data sampling applications.

Import the module using:

```python
import random
```

---

# Pseudorandomness

Computers are deterministic machines, so standard algorithms do not normally generate truly random numbers.

Instead, Python's `random` module generates **pseudorandom numbers**.

Pseudorandom numbers:

* Are generated using mathematical algorithms.
* Appear random.
* Are deterministic internally.
* Can be reproduced when the same seed is used.

Python's default pseudorandom number generator uses the **Mersenne Twister** algorithm.

> **Important:** The `random` module is designed for simulations, games, testing, and general-purpose randomness. It should **not** be used for security-sensitive tasks.

---

# Random Seeds

A **seed** is the starting value used by a pseudorandom number generator.

If you use the same seed, Python produces the same sequence of pseudorandom values.

### Example

```python
import random

random.seed(42)

print(random.randint(1, 100))
```

The sequence generated after setting the seed can be reproduced.

This is useful for:

* Testing.
* Debugging.
* Reproducing experiments.
* Machine learning experiments.
* Simulations.

---

# Generating Random Numbers

The `random` module provides several functions for generating numbers.

---

## 1. `random.random()`

`random.random()` returns a random floating-point number between:

```text
0.0 <= number < 1.0
```

Example:

```python
import random

number = random.random()

print(number)
```

Possible output:

```text
0.728491
```

The exact value will be different each time unless a seed is used.

---

## 2. `random.randint(a, b)`

`random.randint(a, b)` returns a random integer between `a` and `b`.

**Both endpoints are included.**

Example:

```python
import random

number = random.randint(1, 10)

print(number)
```

Possible results include:

```text
1
2
3
...
10
```

Unlike `range()`, the upper value is included.

---

## 3. `random.uniform(a, b)`

`random.uniform(a, b)` returns a random floating-point number between `a` and `b`.

Example:

```python
import random

number = random.uniform(1.5, 5.5)

print(number)
```

Possible output:

```text
3.74281
```

---

# Working with Sequences

The `random` module can also work with lists, tuples, and other sequences.

Three important functions are:

* `random.choice()`
* `random.shuffle()`
* `random.sample()`

---

# 1. `random.choice()`

`random.choice()` selects **one random element** from a non-empty sequence.

Example:

```python
import random

colors = ["red", "blue", "green", "yellow", "purple"]

selected_color = random.choice(colors)

print(selected_color)
```

Possible output:

```text
green
```

Each execution can select a different color.

---

# 2. `random.shuffle()`

`random.shuffle()` randomly rearranges the elements of a list.

It modifies the original list **in-place**.

Example:

```python
import random

colors = ["red", "blue", "green", "yellow", "purple"]

random.shuffle(colors)

print(colors)
```

Possible output:

```text
['green', 'purple', 'red', 'yellow', 'blue']
```

### Important

`shuffle()` changes the original list.

It does **not** return a new shuffled list.

---

# 3. `random.sample()`

`random.sample()` selects multiple **unique elements** from a sequence.

It performs sampling **without replacement**.

Example:

```python
import random

colors = ["red", "blue", "green", "yellow", "purple"]

selected_colors = random.sample(colors, 3)

print(selected_colors)
```

Possible output:

```text
['yellow', 'red', 'purple']
```

The original list remains unchanged.

---

# `choice()` vs `sample()` vs `shuffle()`

| Function    | Purpose                         | Changes Original? |
| ----------- | ------------------------------- | ----------------- |
| `choice()`  | Select one element              | No                |
| `sample()`  | Select multiple unique elements | No                |
| `shuffle()` | Randomly rearrange a list       | Yes               |

### Easy way to remember

```text
choice()  → Pick one
sample()  → Pick several
shuffle()  → Rearrange everything
```

---

# `random` Module Quick Reference

| Function                     | Purpose                                    |
| ---------------------------- | ------------------------------------------ |
| `random.random()`            | Random float from `0.0` to less than `1.0` |
| `random.randint(a, b)`       | Random integer including both `a` and `b`  |
| `random.uniform(a, b)`       | Random floating-point number               |
| `random.choice(sequence)`    | Select one random element                  |
| `random.shuffle(list)`       | Shuffle a list in-place                    |
| `random.sample(sequence, k)` | Select `k` unique elements                 |
| `random.seed(value)`         | Set the pseudorandom generator seed        |

---

# Exercises

## Exercise 1

Write a program that simulates a **coin toss**.

The program should randomly print either:

```text
Heads
```

or:

```text
Tails
```

---

## Exercise 2

Create a list containing **8 student names**.

Use:

* `random.choice()` to select a random **Student of the Day**.
* `random.sample()` to select **3 students** for a presentation group.

Display both results.

---

## Exercise 3

Create a number guessing game.

The computer should:

1. Generate a random number between **1 and 50**.
2. Give the user **5 attempts** to guess it.
3. Tell the user whether their guess is too high or too low.
4. Display a success message when the user guesses correctly.
5. Display the correct answer if all attempts are used.
6. Use `try-except` to handle non-numeric input safely.

---

# Mini Project: Dice Simulator

## Project Overview

Build a **Dice Simulator** that simulates rolling one or more dice.

The application should allow the user to specify:

* How many dice they want to roll.
* How many sides each die has.

For example:

```text
2 × d6
```

represents two six-sided dice.

The program should generate individual results and calculate their total.

---

## Project Requirements

Your program should:

1. Ask the user how many dice they want to roll.
2. Ask how many sides each die should have.
3. Validate that the number of dice is positive.
4. Validate that each die has at least two sides.
5. Generate random values using `random.randint()`.
6. Display the result of each individual die.
7. Calculate the total of all dice.
8. Allow the user to perform multiple rolls.
9. Provide an option to quit.
10. Handle invalid numerical input using `try-except`.

---

## Suggested Program Structure

Consider creating a function such as:

```python
roll_dice(num_dice, sides)
```

The function can:

1. Create a list for the results.
2. Generate a random number for each die.
3. Add each result to the list.
4. Return the completed list.

The main program can then calculate the total using:

```python
sum(results)
```

---

## Example Interaction

```text
--- Interactive Dice Simulator ---

How many dice would you like to roll? 3
How many sides does each die have? 6
```

Example output:

```text
Rolling 3 × d6...

Individual Rolls: [4, 2, 6]
Total Sum: 12
```

> The results will be different each time because the dice rolls are random.

---

## Skills Practiced

This project gives you practice with:

* `random`
* `random.randint()`
* Functions
* Lists
* `for` loops
* `range()`
* `sum()`
* User input
* Input validation
* `try-except`
* `while` loops
* Conditional statements
* Pseudorandom number generation

---

# Common Mistakes

## ❌ Expecting `random.shuffle()` to Return a New List

### Cause

Writing:

```python
shuffled_list = random.shuffle(my_list)
```

This does not work as expected because `shuffle()` modifies the original list **in-place** and returns `None`.

### Solution

Call `shuffle()` directly:

```python
random.shuffle(my_list)

print(my_list)
```

---

## ❌ Confusing `randint()` with `range()`

### Cause

Assuming the upper value of `randint()` is excluded because `range()` excludes its stop value.

For example:

```python
range(1, 10)
```

does not include `10`.

But:

```python
random.randint(1, 10)
```

**does include `10`.**

### Solution

Remember:

```text
range(1, 10)       → 1 through 9
randint(1, 10)     → 1 through 10
```

---

## ❌ Using `random.sample()` with Too Large a Sample

`random.sample()` selects unique elements.

Therefore, you cannot request more elements than are available in the original sequence.

For example, this will raise an error:

```python
random.sample([1, 2, 3], 5)
```

because there are only three elements available.

### Solution

Make sure:

```text
k <= number of available elements
```

---

## ❌ Using `random` for Cryptography or Security

### Cause

Using the standard `random` module to generate:

* Passwords.
* Authentication tokens.
* Encryption keys.
* Security codes.
* Other security-sensitive values.

The pseudorandom sequence can potentially be predicted.

### Solution

For security-sensitive randomness, use Python's built-in **`secrets`** module instead.

---

## ❌ Forgetting That `shuffle()` Modifies the Original List

Consider:

```python
colors = ["red", "blue", "green"]

random.shuffle(colors)
```

The `colors` list itself has now been changed.

If you need to preserve the original order, create a copy before shuffling.

---

# Summary

Today you learned how to:

* ✅ Import and use Python's built-in **`random`** module.
* ✅ Understand **pseudorandomness**.
* ✅ Understand how **seed values** affect reproducibility.
* ✅ Generate random floating-point numbers using `random()`.
* ✅ Generate random integers using `randint()`.
* ✅ Generate random floating-point values using `uniform()`.
* ✅ Select random elements using `choice()`.
* ✅ Select unique random elements using `sample()`.
* ✅ Randomly rearrange lists using `shuffle()`.
* ✅ Build a **Dice Simulator** project.

---

# Key Takeaways

* The `random` module provides tools for generating **pseudorandom** values.
* Pseudorandom numbers are generated using deterministic algorithms.
* A seed can make a random sequence reproducible.
* `random.randint(a, b)` includes **both** `a` and `b`.
* `random.choice()` selects one random element.
* `random.sample()` selects multiple unique elements without modifying the original sequence.
* `random.shuffle()` modifies a list **in-place**.
* The standard `random` module should not be used for security-sensitive randomness.
* Use the **`secrets`** module when secure random values are required.

---

# What's Next?

## Day 040 - Review: CLI Contact Book

In the next lesson, you will review the concepts you've learned throughout this section by building a **Command-Line Contact Book**.

You will combine several Python concepts, including:

* Functions
* Dictionaries
* Lists
* File handling
* JSON/CSV
* User input
* Loops
* Conditional statements
* Exception handling
* Modular program organisation
