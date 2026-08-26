# Day 034 - Exceptions

#### 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand what **exceptions** are and why they occur.
* Understand the difference between **syntax errors** and **exceptions**.
* Use **`try-except`** blocks to prevent programs from crashing.
* Catch specific exceptions such as **`ValueError`**, **`ZeroDivisionError`**, **`IndexError`**, and **`TypeError`**.
* Use **`else`** and **`finally`** blocks for complete error management.
* Build a robust **Safe Calculator**.

---

### What is an Exception?

An **exception** is an error that occurs while a Python program is running.

When Python encounters an unexpected situation, it **raises an exception**. If the exception is not handled, the program stops running and Python displays a traceback.

For example, attempting to divide a number by zero causes a `ZeroDivisionError`.

```python
result = 10 / 0
```

Python raises:

```text
ZeroDivisionError
```

Exceptions commonly occur because of:

* Invalid user input.
* Mathematical errors.
* Missing files.
* Invalid indexes.
* Incorrect data types.
* Unexpected conditions during program execution.

---

### Syntax Errors vs Exceptions

It is important to understand the difference between a **syntax error** and an **exception**.

#### Syntax Error

A syntax error occurs when Python cannot understand the structure of your code.

Example:

```python
if True
    print("Hello")
```

The missing `:` prevents Python from running the program correctly.

Syntax errors are detected **before normal program execution**.

---

#### Exception

An exception occurs **while the program is running**.

Example:

```python
number = int("hello")
```

The syntax is valid, but the value `"hello"` cannot be converted into an integer.

Python raises:

```text
ValueError
```

### Simple Rule

> **Syntax Error** → Python cannot understand your code.
> **Exception** → Python understands your code but encounters a problem while running it.

---

### Common Exception Types

Python provides many built-in exception types.

#### `ValueError`

Raised when a function receives a value of the correct general type but an inappropriate value.

Example:

```python
number = int("abc")
```

The string cannot be converted into an integer, so Python raises a `ValueError`.

---

#### `ZeroDivisionError`

Raised when attempting to divide by zero.

Example:

```python
result = 10 / 0
```

---

#### `IndexError`

Raised when trying to access an index that does not exist.

Example:

```python
numbers = [10, 20, 30]
print(numbers[5])
```

Valid indexes are:

```text
0, 1, 2
```

Therefore, index `5` causes an `IndexError`.

---

#### `TypeError`

Raised when an operation is performed on an inappropriate data type.

Example:

```python
result = "10" + 5
```

Python cannot directly add a string and an integer, so it raises a `TypeError`.

---

#### `FileNotFoundError`

Raised when Python tries to open a file that does not exist.

Example:

```python
with open("missing.txt", "r") as file:
    content = file.read()
```

If `missing.txt` does not exist, Python raises `FileNotFoundError`.

---

### Handling Exceptions with `try-except`

Python provides the **`try-except`** structure to handle exceptions.

**Basic Syntax:**

```python
try:
    # Code that might cause an exception
except SomeException:
    # Code that runs if the exception occurs
```

Example:

```python
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not a valid integer!")
```

If the user enters:

```text
25
```

the conversion succeeds.

If the user enters:

```text
hello
```

the `ValueError` is caught and the program displays the error message instead of crashing.

---

### How `try-except` Works

Consider:

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid number.")
```

Python follows this process:

1. Enter the `try` block.
2. Execute the statements inside it.
3. If no exception occurs, skip the `except` block.
4. If a `ValueError` occurs, immediately leave the `try` block.
5. Execute the matching `except` block.
6. Continue with the rest of the program.

---

### Handling Multiple Exceptions

A program may encounter different types of exceptions.

You can use multiple `except` blocks to handle them separately.

```python
try:
    num = int(input("Divide 100 by: "))
    result = 100 / num

except ValueError:
    print("Invalid input! You must enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
```

Each exception gets its own appropriate response.

This is better than treating every error as the same problem.

---

### Why Catch Specific Exceptions?

You should generally catch the **specific exceptions** you expect.

Good:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")
```

Less desirable:

```python
try:
    number = int(input("Enter a number: "))
except:
    print("Something went wrong.")
```

Specific exception handling:

* Makes your code easier to understand.
* Makes debugging easier.
* Prevents unexpected errors from being hidden.
* Allows different errors to receive different responses.

---

### The `else` Block

The `else` block runs **only when no exception occurs** inside the `try` block.

**Syntax:**

```python
try:
    # Code that might fail
except SomeException:
    # Runs if an exception occurs
else:
    # Runs if no exception occurs
```

Example:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print(f"You entered {number}.")
```

If the user enters a valid number, the `else` block runs.

If a `ValueError` occurs, the `except` block runs instead.

---

### The `finally` Block

The `finally` block runs **regardless of whether an exception occurs**.

**Syntax:**

```python
try:
    # Code that might fail
except SomeException:
    # Handle error
finally:
    # Always runs
```

Example:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
finally:
    print("Program finished.")
```

The `finally` block runs whether the conversion succeeds or fails.

---

### When Should You Use `finally`?

The `finally` block is commonly used for **cleanup operations**.

Examples include:

* Closing resources.
* Releasing connections.
* Cleaning temporary resources.
* Performing actions that must happen regardless of success or failure.

When using `with` for files, Python already handles file closing automatically, so you often do not need `finally` just to close a file.

---

### Complete Exception Structure

Python allows you to combine all the major components:

```python
try:
    # Code that might cause an exception

except SomeException:
    # Handle the exception

else:
    # Runs when no exception occurs

finally:
    # Always runs
```

The execution flow can be visualized as:

```text
             try
              │
       ┌──────┴──────┐
       │             │
   Exception      No Error
       │             │
     except         else
       │             │
       └──────┬──────┘
              │
           finally
              │
            Done
```

---

### Exercises

#### Exercise 1

Write a program that asks the user for their age.

Requirements:

* Convert the input into an integer.
* Catch `ValueError`.
* Display:

```text
Please enter a numerical value.
```

when invalid input is provided.

---

#### Exercise 2

Create a list containing three items.

Ask the user to enter an index number and print the corresponding item.

Handle both:

* `ValueError` if the user enters something that is not a number.
* `IndexError` if the user enters a number outside the valid range.

---

#### Exercise 3

Write a function called `safe_divide(a, b)`.

Requirements:

* Return the result of `a / b`.
* Catch `ZeroDivisionError`.
* Return `None` when `b` is zero.

---

### Mini Project: Safe Calculator

Create a file named `safe_calculator.py`.

Build a calculator that can handle invalid user input without crashing.

### Project Requirements

The calculator should:

1. Display a welcome message.
2. Ask the user for the first number.
3. Ask the user for an operator.
4. Ask the user for the second number.
5. Support:

   * `+`
   * `-`
   * `*`
   * `/`
6. Handle invalid numeric input using `ValueError`.
7. Handle division by zero using `ZeroDivisionError`.
8. Handle invalid mathematical operators.
9. Allow the user to exit the application.
10. Display the result only when the calculation succeeds.
11. Continue running after recoverable errors.

### Suggested Program Flow

```text
--- Safe Calculator App ---

Enter first number:
Enter operator (+, -, *, /):
Enter second number:

Result: ...
```

If the user enters invalid input:

```text
Error: Please enter a valid numeric value.
```

If the user attempts to divide by zero:

```text
Error: Cannot divide by zero.
```

If the user enters an invalid operator:

```text
Error: Invalid operator.
```

> **Practice Requirement:** Implement the project yourself using today's exception-handling concepts. The project solution code is intentionally not included in this note.

---

### Common Mistakes

#### ❌ Using a Bare `except:`

**Cause:** Catching every possible exception without specifying a type.

```python
try:
    # Code
except:
    print("Something went wrong.")
```

This can hide unexpected programming errors and make debugging difficult.

**Solution:**

Catch specific exceptions whenever possible.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
```

---

#### ❌ Catching the Wrong Exception

Different problems produce different exceptions.

For example:

```python
int("hello")
```

produces:

```text
ValueError
```

while:

```python
10 / 0
```

produces:

```text
ZeroDivisionError
```

Make sure you catch the exception that can actually occur.

---

#### ❌ Making the `try` Block Too Large

A common mistake is putting a large amount of unrelated code inside one `try` block.

For example:

```python
try:
    # Dozens of unrelated operations
```

This makes it difficult to determine which operation caused the exception.

**Solution:**

Keep `try` blocks focused on operations that are expected to potentially raise the exception you want to handle.

---

#### ❌ Confusing Exceptions with Syntax Errors

A `try-except` block cannot be used to fix invalid Python syntax.

For example:

```python
if True
    print("Hello")
```

The missing colon is a syntax error and must be fixed before the program can run.

---

#### ❌ Using Exceptions for Normal Program Flow

Exceptions should generally handle **unexpected or exceptional situations**, not ordinary decisions.

For example, if you can validate user input normally before performing an operation, that may be clearer than deliberately triggering an exception.

---

### Summary

Today you learned how to:

* ✅ Understand what **exceptions** are.
* ✅ Differentiate **syntax errors** from runtime exceptions.
* ✅ Use **`try-except`** to handle errors gracefully.
* ✅ Catch specific exceptions such as `ValueError`.
* ✅ Handle mathematical errors such as `ZeroDivisionError`.
* ✅ Handle invalid indexes using `IndexError`.
* ✅ Understand `TypeError` and `FileNotFoundError`.
* ✅ Use multiple `except` blocks.
* ✅ Use the **`else`** block when no exception occurs.
* ✅ Use the **`finally`** block for operations that must always run.
* ✅ Build a robust **Safe Calculator**.

---

### Key Takeaways

* Exceptions are signals that something went wrong during program execution.
* `try-except` allows your program to handle expected runtime problems without crashing.
* Catch **specific exceptions** instead of using a broad bare `except`.
* `ValueError` commonly occurs when a value cannot be converted into the expected form.
* `ZeroDivisionError` occurs when dividing by zero.
* `IndexError` occurs when accessing an invalid sequence index.
* `TypeError` occurs when an operation is performed on an inappropriate data type.
* `else` runs when the `try` block completes successfully.
* `finally` runs regardless of whether an exception occurred.
* Syntax errors must be fixed before the program can execute; they are not normally handled with `try-except`.

---

### What's Next?

**Day 035 - Custom Exceptions**
