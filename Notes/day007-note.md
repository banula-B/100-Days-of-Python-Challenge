# Day 007 - `elif` Statements

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand the purpose of the **`elif` statement** for handling multiple conditions.
- Master the **order of execution** in conditional chains.
- Combine `if`, `elif`, and `else` to create more complex decision-making logic.
- Build a **Grade Calculator** project.

---

# 📚 The `elif` Statement

The **`elif`** keyword stands for **"else if."**

It allows your program to check multiple conditions one after another.

If the first `if` condition is **False**, Python checks the first `elif`.

If that condition is also **False**, Python continues checking the next `elif`.

If none of the conditions are **True**, the `else` block (if provided) is executed.

### Basic Syntax

```python
if condition1:
    # Runs if condition1 is True
elif condition2:
    # Runs if condition1 is False and condition2 is True
else:
    # Runs if all previous conditions are False
```

---

# 🔄 Order of Execution

Python checks conditions from **top to bottom**.

As soon as it finds a condition that is **True**, it executes that block and ignores the rest of the `elif` and `else` statements.

### Example

```python
weather = "sunny"

if weather == "rainy":
    print("Wear boots.")
elif weather == "sunny":
    print("Wear sunglasses.")
else:
    print("Check the forecast.")
```

Output:

```text
Wear sunglasses.
```

Python stops checking after the second condition becomes **True**.

---

# ❓ Why Use `elif` Instead of Multiple `if` Statements?

When you use multiple `if` statements, Python checks **every** condition.

When you use an `if-elif-else` chain, Python stops checking after finding the first **True** condition.

### Example Using `if-elif-else`

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C")
```

Output:

```text
Grade B
```

Only one message is printed because Python stops after the matching condition.

---

# 🚀 Mini Project - Grade Calculator

Create a file named **`grade_calculator.py`**.

### Requirements

Your program should:

- Ask the user to enter a score between **0 and 100**.
- Convert the input into a number.
- Display the correct grade using the following rules:
  - **90 and above** → Grade A
  - **80–89** → Grade B
  - **70–79** → Grade C
  - **60–69** → Grade D
  - **Below 60** → Grade F

### Sample Input

```text
Enter your score: 87
```

### Expected Output

```text
Grade: B
```

---

# 🏋️ Exercises

## Exercise 1

Ask the user to enter a temperature in Celsius.

- If it is **above 30**, print:

```
Hot
```

- If it is **between 20 and 30**, print:

```
Warm
```

- Otherwise, print:

```
Cold
```

### Sample Input

```text
Enter temperature: 25
```

### Expected Output

```text
Warm
```

---

## Exercise 2

Ask the user to enter their age.

Display:

- **Child** if the age is under 13.
- **Teen** if the age is between 13 and 19.
- **Adult** if the age is 20 or above.

### Sample Input

```text
Enter your age: 16
```

### Expected Output

```text
Teen
```

---

## Exercise 3

Ask the user to enter a number.

Display:

- **Small** if the number is less than 10.
- **Medium** if the number is between 10 and 50.
- **Large** if the number is greater than 50.

### Sample Input

```text
Enter a number: 65
```

### Expected Output

```text
Large
```

---

# ❌ Common Mistakes

## Putting the Broad Condition First

Incorrect:

```python
if score >= 60:
    print("Grade D")
elif score >= 90:
    print("Grade A")
```

A score of **95** would incorrectly print **Grade D** because Python stops at the first matching condition.

Always check the **highest or most specific** conditions first.

---

## Using Multiple `if` Statements

Incorrect:

```python
if score >= 60:
    print("Pass")

if score >= 80:
    print("Good")
```

Both messages may be printed.

Use `elif` when only **one** result should be displayed.

---

## Forgetting the Final `else`

Although optional, an `else` statement is useful for handling values that don't match any previous condition.

---

# 📝 Summary

Today you learned how to:

- ✅ Use **`elif`** to handle multiple conditions.
- ✅ Build logical conditional chains.
- ✅ Understand how Python evaluates conditions from top to bottom.
- ✅ Create a Grade Calculator using `if`, `elif`, and `else`.

---

# 🔑 Key Takeaways

- An `elif` statement always follows an `if` statement.
- Python checks conditions in order and stops at the **first** condition that is `True`.
- The `else` block is optional and acts as a default case.
- Arrange conditions from the most specific or highest priority to the most general.

---

# 📖 What's Next?

## Day 008 – Comparison Operators