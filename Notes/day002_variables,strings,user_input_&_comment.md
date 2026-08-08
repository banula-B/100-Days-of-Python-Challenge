# Day 002 - Variables, Strings, User Input, and Comments

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand how to use variables to store data.
- Work with strings and basic string manipulation.
- Use the `input()` function to make your programs interactive.
- Write comments to explain your code to others (and yourself).
- Create a program that introduces a user based on their input.

---

# 📚 Variables and Strings

A **variable** is a name that refers to a value. In Python, you create a variable by assigning a value using the `=` operator.

A **string** is a sequence of characters enclosed in either single quotes (`'`) or double quotes (`"`).

### Example

```python
name = "Alice"  # 'name' is the variable, "Alice" is the string

print(name)
```

**Output**

```text
Alice
```

---

# 💬 Getting User Input

To make your programs interactive, Python provides the `input()` function.

`input()` displays a message (called a prompt), waits for the user to type something, and returns the value as a **string**.

### Example

```python
user_name = input("What is your name? ")

print("Hello, " + user_name + "!")
```

### Sample Output

```text
What is your name? Bob
Hello, Bob!
```

---

# 📝 Using Comments

Comments are notes inside your code that Python ignores during execution.

They help explain what your code does for yourself and other programmers.

## Single-Line Comment

Single-line comments begin with the `#` symbol.

```python
# This line prints a greeting
print("Hi there!")
```

## Multi-Line Comment

Python doesn't have a special multi-line comment syntax, but programmers commonly use multiple `#` symbols.

```python
# This program introduces the user.
# It asks for personal information.
# Then it prints a complete introduction.
```

You may also see triple quotes (`""" """`) used for documentation.

```python
"""
This is a multi-line
documentation string.
"""
```

---

# 🏋️ Exercises

## Exercise 1

Create a variable for your favourite city and print it.

Example:

```python
city = "Tokyo"

print(city)
```

---

## Exercise 2

Ask the user:

> What did you eat for breakfast?

Then print their response.

Example:

```python
breakfast = input("What did you eat for breakfast? ")

print("You ate " + breakfast + " for breakfast.")
```

---

## Exercise 3

Write a multi-line comment explaining why you want to learn Python.

Example:

```python
# I want to learn Python because it is beginner-friendly.
# I also want to build projects and become a software developer.
# Learning Python will help me automate tasks and solve problems.
```

---

# 🚀 Mini Project: Personal Introduction Program

Create a file named **`introduction.py`**.

The program should:

1. Ask the user for their name.
2. Ask for their favourite hobby.
3. Ask for their dream job.
4. Print a complete introduction.

### Example Code

```python
name = input("What is your name? ")
hobby = input("What is your favourite hobby? ")
job = input("What is your dream job? ")

print("My name is " + name + ". I love " + hobby + " and I want to be a " + job + ".")
```

### Sample Output

```text
What is your name? Bob
What is your favourite hobby? Coding
What is your dream job? Software Engineer

My name is Bob. I love Coding and I want to be a Software Engineer.
```

---

# ❌ Common Mistakes

## 1. Forgetting Quotes Around Strings

Incorrect:

```python
name = Alice
```

Python thinks `Alice` is another variable.

Correct:

```python
name = "Alice"
```

---

## 2. Confusing `input()` and `print()`

Remember:

- `input()` → Gets information from the user.
- `print()` → Displays information to the user.

Example:

```python
name = input("Enter your name: ")
print(name)
```

---

## 3. Forgetting Parentheses

Incorrect:

```python
print
```

Correct:

```python
print("Hello")
```

---

# 📝 Summary

Today you learned how to:

- ✅ Use variables to store information.
- ✅ Create and print strings.
- ✅ Capture user input using `input()`.
- ✅ Document your code using comments.

---

# 🔑 Key Takeaways

- Variables make your programs dynamic by storing reusable information.
- Strings represent text in Python.
- `input()` always returns a **string**.
- Comments improve code readability and maintainability.
- Interactive programs are more useful and engaging.

---

# 💻 Challenge (Optional)

Improve your introduction program by also asking:

- Your age
- Your country
- Your favourite programming language

Then display everything in a neat introduction.

Example:

```text
Hello!

My name is Bob.
I am 20 years old.
I live in Sri Lanka.
My favourite hobby is Coding.
I want to become a Software Engineer.
My favourite programming language is Python.
```

---

# 📖 What's Next?

## Day 003 – Numbers and Operators

In the next lesson, you'll learn about:

- Integers
- Floats
- Arithmetic Operators (`+`, `-`, `*`, `/`)
- Modulus (`%`)
- Exponents (`**`)
- Floor Division (`//`)
- Building a Simple Calculator