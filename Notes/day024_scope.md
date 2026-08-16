# Day 024 - Scope

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the difference between **Local Scope** and **Global Scope**.
* Learn how Python searches for variables using the **LEGB rule**.
* Use the **`global`** keyword to modify global variables from within a function.
* Recognize the importance of scope in maintaining clean and bug-free code.
* Build a **Password Validator** project.

---

## What is Scope?

**Scope** refers to the region of a program where a specific variable is accessible.

Not every variable can be accessed from every part of your code. Whether a variable can be used depends on where it was created.

Understanding scope helps you write cleaner programs and avoid unexpected behavior.

---

## 1. Local Scope

A variable created **inside** a function belongs to the **local scope** of that function.

It can only be accessed within that function.

### Example

```python
def my_function():
    x = 300  # Local variable
    print(x)

my_function()

# print(x)
# ❌ This would cause a NameError because x does not exist here
```

Here, `x` belongs only to `my_function()`.

Once the function finishes executing, the local variable is no longer accessible from outside the function.

---

## 2. Global Scope

A variable created in the **main body** of a Python script belongs to the **global scope**.

A global variable can be accessed from different parts of the program, including inside functions.

### Example

```python
x = 300  # Global variable

def my_function():
    print(x)  # Accessing the global x

my_function()

print(x)  # Also accessing the global x
```

Output:

```text
300
300
```

The function can read the global variable because `x` exists in the global scope.

---

## Local vs. Global Scope

| Scope  | Where Created     | Where Accessible       |
| ------ | ----------------- | ---------------------- |
| Local  | Inside a function | Inside that function   |
| Global | Outside functions | Throughout the program |

### General Rule

Prefer **local variables** whenever possible.

Local variables make functions more independent and reduce unexpected changes to shared program state.

---

## The `global` Keyword

Normally, a function can **read** a global variable, but assigning a new value to that variable inside the function creates a local variable instead.

If you need to **modify** a global variable from inside a function, use the `global` keyword.

### Example

```python
count = 0

def increment():
    global count
    count += 1

increment()

print(count)
```

Output:

```text
1
```

The `global` keyword tells Python that `count` refers to the variable defined in the global scope.

---

## The LEGB Rule

When Python encounters a variable name, it searches for that variable using the **LEGB** rule.

LEGB stands for:

### 1. L — Local

Python first searches inside the current function.

### 2. E — Enclosing

If the function is nested inside another function, Python searches the enclosing function's scope.

### 3. G — Global

Python then searches the global scope of the current script.

### 4. B — Built-in

Finally, Python searches the built-in namespace for names such as:

```python
print
len
range
sum
```

### LEGB Search Order

```text
Local
  ↓
Enclosing
  ↓
Global
  ↓
Built-in
```

Understanding this order helps explain why Python chooses a particular variable when multiple variables have the same name.

---

## Exercises

### Exercise 1

Create a global variable called `total`.

Write a function that adds `10` to `total` using the `global` keyword.

### Exercise 2

Define a global variable:

```python
name = "Global"
```

Inside a function, create a local variable:

```python
name = "Local"
```

Print the variable inside the function and then outside the function to observe how the two variables coexist.

### Exercise 3

Write a function that contains another function.

Create a variable in the outer function and try to access it from the inner function.

Observe how Python searches for the variable using the LEGB rule.

---

## Mini Project: Password Validator

Create a file named:

```text
password_validator.py
```

This project will use functions to verify whether a user's password meets basic security requirements.

The password should:

* Contain at least 8 characters.
* Contain at least one number.

The project also provides practice with variable scope and the `global` keyword.

### Project Requirements

Your program should:

1. Ask the user to enter a password.
2. Check whether the password contains at least 8 characters.
3. Check whether the password contains at least one digit.
4. Accept the password only when both requirements are satisfied.
5. Track whether the system has been unlocked.
6. Display an appropriate message based on the validation result.
7. Use separate functions for the validation checks.

### Suggested Functions

Create a function to check password length:

```text
check_length(password)
```

Create a function to check whether the password contains a digit:

```text
check_digit(password)
```

Create a function to perform the complete validation:

```text
validate_password()
```

> **Challenge:** Build the project yourself using functions, scope, conditions, loops, string methods, and return values. Try to avoid copying a complete solution.

---

## Common Mistakes

### ❌ `UnboundLocalError`

**Cause:** Trying to modify a global variable inside a function without declaring it as global.

For example:

```python
x = 10

def update():
    x = x + 1
```

Python treats `x` as a local variable because it is being assigned inside the function.

If you intentionally need to modify the global variable, use:

```python
x = 10

def update():
    global x
    x = x + 1
```

---

### ❌ Global Variable Overuse

**Cause:** Making too many variables global to avoid passing parameters.

This can make programs difficult to understand, test, and debug.

### Better Approach

Whenever possible, use:

* Function parameters
* Return values
* Local variables

For example:

```python
def calculate_total(price, quantity):
    return price * quantity
```

This is generally cleaner than modifying a global variable.

---

### ❌ Shadowing

**Cause:** Creating a local variable with the same name as a global variable.

Example:

```python
name = "Global"

def show_name():
    name = "Local"
    print(name)
```

Inside the function, the local `name` takes precedence over the global `name`.

This is known as **variable shadowing**.

---

## Summary

Today you learned how to:

* ✅ Distinguish between **Local** and **Global** scope.
* ✅ Understand how Python searches for variables using the **LEGB rule**.
* ✅ Use the **`global`** keyword to modify a global variable.
* ✅ Understand variable shadowing.
* ✅ Recognize why excessive global variables can make code difficult to maintain.
* ✅ Build a functional **Password Validator**.

---

## Key Takeaways

* Variables have a **scope** that determines where they can be accessed.
* Local variables belong to the function where they are created.
* Global variables are created outside functions and can be accessed from different scopes.
* Python searches for variables using the **LEGB** order: Local → Enclosing → Global → Built-in.
* The `global` keyword allows a function to modify a global variable.
* Avoid excessive use of global variables.
* Passing data through **parameters** and receiving results through **return values** is generally a cleaner approach.

---

## What's Next?

### Day 025 - Lambda

Next, you will learn about **lambda functions**, anonymous functions, and how they can be used to write small, simple functions in a concise way.
