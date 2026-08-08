# Day 001 - Setting Up Python Development Environment & Hello World

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand what Python is.
* Install Python on your computer.
* Install Visual Studio Code (VS Code).
* Configure VS Code for Python development.
* Understand the purpose of Git and GitHub.
* Create your first Python project.
* Write and run your first Python program.
* Understand the `print()` function.

---

# What is Python?

Python is a **high-level, interpreted, and general-purpose programming language** created by **Guido van Rossum** and first released in **1991**.

Python is designed to be simple, readable, and easy to learn, making it one of the most popular programming languages in the world.

Python is widely used in:

* 🌐 Web Development
* 🤖 Artificial Intelligence & Machine Learning
* 📊 Data Science
* 🔄 Automation & Scripting
* 🛠 Desktop Applications
* 🎮 Game Development
* 🔐 Cybersecurity
* ☁ Cloud Computing

---

# Installing Python

Visit the official Python website:

> https://www.python.org/downloads/

Download the latest stable version for your operating system.

### Windows Users

During installation, **make sure to check**:

```
✅ Add Python to PATH
```

Then click **Install Now**.

---

# Verify the Installation

Open your terminal.

### Windows

* Command Prompt
* PowerShell

### Linux/macOS

* Terminal

Run:

```bash
python --version
```

If that doesn't work:

```bash
python3 --version
```

Example output:

```text
Python 3.13.7
```

---

# Installing Visual Studio Code

Download VS Code from:

> https://code.visualstudio.com/

Install it using the default settings.

VS Code is one of the most popular code editors for Python development because it is lightweight, fast, and highly customizable.

---

# Install the Python Extension

Open VS Code.

Go to:

```
Extensions (Ctrl + Shift + X)
```

Search for:

```
Python
```

Install the extension published by **Microsoft**.

It provides:

* Syntax Highlighting
* IntelliSense (Code Completion)
* Debugging
* Formatting
* Linting
* Integrated Terminal Support

---

# Configure the Python Interpreter

Open the Command Palette:

```
Ctrl + Shift + P
```

Search for:

```
Python: Select Interpreter
```

Select the Python version you installed.

Example:

```
Python 3.13
```

---

# Install Git (Recommended)

Git is a version control system that helps you track changes in your code.

Download Git from:

> https://git-scm.com/downloads

Verify the installation:

```bash
git --version
```

Example:

```text
git version 2.xx.x
```

---

# Create Your Project Structure

Create the following folders:

```text
python-100-days/
│
├── README.md
├── notes/
│   └── day001.md
│
├── projects/
│   └── day001-hello_world.py
│
├── exercises/
│
└── resources/
```

Open the **python-100-days** folder using VS Code.

---

# Understanding the Terminal

You will frequently use the integrated terminal in VS Code.

Open it using:

```
Terminal → New Terminal
```

or

```
Ctrl + `
```

Useful commands:

Check Python version:

```bash
python --version
```

Check Git version:

```bash
git --version
```

---

# Your First Python Program

Create a file named:

```
hello.py
```

Add the following code:

```python
print("Hello, World!")
```

Save the file.

---

# Running a Python Program

Open the terminal.

Navigate to your project folder if necessary.

Run:

```bash
python hello.py
```

or

```bash
python3 hello.py
```

Output:

```text
Hello, World!
```

🎉 Congratulations! You have successfully written and executed your first Python program.

---

# Understanding the Code

```python
print("Hello, World!")
```

### `print()`

`print()` is a built-in Python function used to display output on the screen.

### `"Hello, World!"`

The text inside quotation marks is called a **string**.

Strings are used to represent text in Python.

---

# Why Does Every Programming Language Start with "Hello, World!"?

The **"Hello, World!"** program is a long-standing tradition in programming.

Its purpose is to verify that:

* Your programming environment is installed correctly.
* Your code can be compiled or interpreted successfully.
* You understand the basic workflow of writing and running a program.

---

# GitHub Workflow for This Challenge

For each day of this challenge, aim to make at least three commits:

1. Add or update the lesson notes.
2. Complete the exercises.
3. Finish the mini project.

This habit will help you build consistency and maintain an active GitHub contribution history.

---

# Mini Project

## Hello World

Create a file named `hello.py` and print a welcome message.

Example:

```python
print("Hello, World!")
print("Welcome to my 100 Days of Python Challenge!")
```

Expected output:

```text
Hello, World!
Welcome to my 100 Days of Python Challenge!
```

---

# Exercises

## Exercise 1

Print your name.

Example output:

```text
John Doe
```

---

## Exercise 2

Print your country.

Example output:

```text
Sri Lanka
```

---

## Exercise 3

Print your learning goal.

Example:

```text
I will complete the 100 Days of Python Challenge.
```

---

# Common Mistakes

### ❌ Python is not recognized as an internal or external command

Cause:

Python was not added to the system PATH.

Solution:

* Reinstall Python.
* Enable **"Add Python to PATH"** during installation.

---

### ❌ No Python interpreter selected in VS Code

Solution:

Open the Command Palette and choose **Python: Select Interpreter**.

---

### ❌ File not found

Ensure you're running the command from the correct directory or provide the correct path to the Python file.

---

# Summary

Today you learned how to:

* ✅ Install Python
* ✅ Verify the installation
* ✅ Install Visual Studio Code
* ✅ Configure VS Code for Python development
* ✅ Install Git
* ✅ Create a Python project structure
* ✅ Use the terminal
* ✅ Write your first Python program
* ✅ Use the `print()` function

---

# Key Takeaways

* Python is beginner-friendly and widely used across many domains.
* VS Code provides a powerful environment for Python development.
* Git helps track your progress and manage your code.
* The `print()` function displays output to the console.
* "Hello, World!" is the traditional first program in almost every programming language.

---

# What's Next?

**Day 002 - Variables, Strings, User Input, and Comments**
