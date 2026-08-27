# Day 035 - Custom Exceptions

#### 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand when and why to define **custom exceptions** instead of using standard Python errors.
* Manually trigger exceptions using the **`raise`** keyword.
* Create custom exception classes by inheriting from Python's built-in **`Exception`** class.
* Handle custom exceptions using `try-except`.
* Separate application-specific validation rules from general Python errors.
* Build a **Login Validation** program using custom exceptions.

---

### Beyond Built-in Exceptions

In Day 034, you learned how to handle built-in Python exceptions such as:

* `ValueError`
* `ZeroDivisionError`
* `IndexError`
* `TypeError`
* `FileNotFoundError`

These exceptions are useful for handling common technical problems.

However, real applications often have their own **business rules**.

For example:

* A username must contain at least 5 characters.
* A password must contain a special character.
* An account balance cannot be negative.
* A temperature cannot be below absolute zero.
* A product quantity cannot be negative.

Python does not provide a separate built-in exception for every possible business rule.

This is where **custom exceptions** become useful.

---

### What is a Custom Exception?

A **custom exception** is an exception class that you create for a specific situation in your application.

For example, Python does not have a built-in `UsernameTooShortError`.

You can create one yourself:

```python id="m8z0kq"
class UsernameTooShortError(Exception):
    pass
```

Now your application has a meaningful exception specifically for invalid usernames.

---

### Why Use Custom Exceptions?

Custom exceptions can make your programs:

* Easier to understand.
* Easier to debug.
* Easier to maintain.
* More descriptive.
* Better organized.
* Better suited to application-specific rules.

Compare:

```python id="v4j7p2"
raise ValueError("Invalid username")
```

with:

```python id="v2q4ym"
raise UsernameTooShortError("Username must be at least 5 characters.")
```

The second version immediately tells another developer **what kind of problem occurred**.

---

### The `raise` Keyword

The **`raise`** keyword is used to manually trigger an exception.

**Basic Syntax:**

```python id="r8gq1n"
raise Exception("Error message")
```

You can also raise a specific built-in exception:

```python id="v4h6fp"
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

When Python reaches the `raise` statement, the exception is triggered.

---

### Why Use `raise`?

Normally, Python raises exceptions automatically when something goes wrong.

For example:

```python id="2fl7lc"
number = int("hello")
```

Python automatically raises a `ValueError`.

However, your application may need to raise an error when a **business rule** is violated.

For example:

```python id="7y3s8e"
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Here, Python's syntax is perfectly valid, but your application's rule says that a negative age is not allowed.

---

### Creating a Custom Exception

Custom exceptions are usually created by defining a class that inherits from `Exception`.

**Basic Syntax:**

```python id="w8h9q3"
class InvalidUsernameError(Exception):
    """Raised when a username does not meet system requirements."""
    pass
```

The `pass` statement means the class does not need any additional implementation for this simple example.

The new exception automatically inherits the behavior of Python's base `Exception` class.

---

### Naming Custom Exceptions

By convention, exception class names should:

* Use **PascalCase**.
* Describe the problem clearly.
* Usually end with **`Error`**.

Examples:

```python id="3i8l1w"
class InvalidUsernameError(Exception):
    pass

class PasswordTooWeakError(Exception):
    pass

class NegativeBalanceError(Exception):
    pass

class EmptyInputError(Exception):
    pass
```

Good names make your code easier to understand.

---

### Raising a Custom Exception

Once a custom exception has been defined, you can raise it using `raise`.

```python id="m6n5bc"
class InvalidUsernameError(Exception):
    pass


def check_username(name):
    if len(name) < 5:
        raise InvalidUsernameError(
            "Username must be at least 5 characters long."
        )
```

If an invalid username is provided, the custom exception is raised.

---

### Catching a Custom Exception

Custom exceptions can be handled using `try-except`, just like built-in exceptions.

```python id="4c2v9z"
try:
    check_username("abc")

except InvalidUsernameError as error:
    print(f"Registration failed: {error}")
```

The exception can be stored in a variable using:

```python id="j5m3v8"
except InvalidUsernameError as error:
```

The `error` variable contains the exception object and can be used to display its message.

---

### Complete Flow

The general process is:

```text id="5u8x5d"
Define Custom Exception
        ↓
Create Validation Rule
        ↓
Check User Input
        ↓
Rule Violated?
     ↙       ↘
   Yes        No
    ↓          ↓
  raise      Continue
    ↓
try-except
    ↓
Handle Error
```

This allows validation logic and error-handling logic to remain separate.

---

### Custom Exceptions vs Built-in Exceptions

Use **built-in exceptions** when the problem matches a standard Python situation.

Examples:

```text id="yq1r4b"
ValueError          → Invalid value
TypeError           → Incorrect data type
IndexError          → Invalid sequence index
FileNotFoundError   → File does not exist
ZeroDivisionError   → Division by zero
```

Use **custom exceptions** when the problem represents a specific rule in your application.

Examples:

```text id="3j1l2x"
UsernameTooShortError
PasswordTooWeakError
NegativeBalanceError
InvalidOrderError
EmptyInputError
```

### Simple Rule

> Use **built-in exceptions** for general Python problems.
> Use **custom exceptions** for application-specific rules.

---

### Multiple Custom Exceptions

A program can define and handle multiple custom exceptions.

For example:

```python id="q3c9hn"
class UsernameTooShortError(Exception):
    pass


class PasswordTooWeakError(Exception):
    pass
```

Different validation rules can then raise different exceptions.

```python id="q6n3bf"
try:
    # Validation logic
    ...

except UsernameTooShortError:
    print("Username is too short.")

except PasswordTooWeakError:
    print("Password is too weak.")
```

This makes it possible to provide a more specific response for each problem.

---

### Custom Exceptions with Messages

Custom exceptions can receive descriptive messages.

```python id="1lj6w2"
raise UsernameTooShortError(
    "Username must be at least 5 characters long."
)
```

The message can then be accessed when catching the exception:

```python id="1kv0l3"
except UsernameTooShortError as error:
    print(error)
```

This is useful for giving users or developers meaningful information about what went wrong.

---

### Exercises

#### Exercise 1

Create a custom exception called `NegativeTemperatureError`.

Write a function called `check_temp(celsius)`.

The function should:

* Accept a temperature in Celsius.
* Raise `NegativeTemperatureError` if the temperature is below absolute zero (`-273.15°C`).
* Otherwise, indicate that the temperature is valid.

---

#### Exercise 2

Write a program that asks the user to enter a number.

The number must be a **multiple of 10**.

If it is not a multiple of 10:

* Raise a standard `ValueError`.
* Catch the exception using `try-except`.
* Display an appropriate error message.

---

#### Exercise 3

Define a custom exception called `EmptyInputError`.

Create a program that repeatedly asks the user for text.

If the user presses Enter without entering anything:

* Raise `EmptyInputError`.
* Catch it using `try-except`.
* Display a message asking the user to provide some text.

---

### Mini Project: Login Validation

Create a file named `login_validation.py`.

Build a simple **User Registration and Login Validation** application that uses custom exceptions to enforce application-specific rules.

### Project Requirements

Your application should validate:

#### Username

* Must contain at least **5 characters**.
* Raise `UsernameTooShortError` if the requirement is not met.

#### Password

* Must contain at least **8 characters**.
* Must contain at least one special character.
* Raise `PasswordTooWeakError` if the requirements are not met.

Suggested special characters include:

```text
! @ # $ % & *
```

### Suggested Project Structure

```text id="i0l4k7"
login-validation/
│
└── login_validation.py
```

### Expected Program Flow

```text id="c4x6y1"
--- User Registration System ---

Choose a username: ...
Choose a password: ...

Credentials valid!
Account successfully created.
```

For an invalid username:

```text id="h8y0m2"
Registration Error:
Username must be at least 5 characters long.
```

For an invalid password:

```text id="d1w7p3"
Security Error:
Password must be at least 8 characters long
and contain at least one special character.
```

### Concepts to Practice

Your implementation should demonstrate:

* Custom exception classes.
* Inheritance from `Exception`.
* The `raise` keyword.
* Functions for validation.
* Multiple `except` blocks.
* Exception messages.
* Separation of validation logic from program execution.

> **Practice Requirement:** Implement the project yourself using today's custom-exception concepts. The project solution code is intentionally not included in this note.

---

### Common Mistakes

#### ❌ Forgetting to Inherit from `Exception`

**Cause:**

Defining an exception without inheriting from `Exception`.

```python id="7q4znp"
class MyError:
    pass
```

This is not a proper exception class that can be raised normally.

**Solution:**

Inherit from `Exception`:

```python id="p8c4v2"
class MyError(Exception):
    pass
```

---

#### ❌ Raising the Wrong Object

A custom exception should be raised as an exception class or instance.

Preferred:

```python id="5b2n9k"
raise MyError("Something went wrong.")
```

This provides a useful error message.

---

#### ❌ Overusing Custom Exceptions

**Cause:** Creating a custom exception for every possible error.

For example, creating a custom exception for a standard `ValueError` situation is usually unnecessary.

**Solution:**

Use built-in exceptions when they already accurately describe the problem.

Use custom exceptions when you need to represent **application-specific rules or domain-specific failures**.

---

#### ❌ Catching the Wrong Exception

If a function raises:

```python id="9f0z5y"
UsernameTooShortError
```

but you only catch:

```python id="j4p8w1"
except PasswordTooWeakError:
```

the username exception will not be handled by that block.

**Solution:**

Make sure the `except` block matches the exception you expect.

---

#### ❌ Putting Validation and Error Handling Everywhere

Scattering `raise` and `try-except` logic throughout your program can make the code difficult to maintain.

A cleaner approach is:

```text id="y0m4r8"
Validation Function
       ↓
raise Exception
       ↓
Main Program
       ↓
try-except
```

Keep validation logic focused in functions and handle the exceptions at an appropriate higher level.

---

### Summary

Today you learned how to:

* ✅ Understand why custom exceptions are useful.
* ✅ Manually trigger exceptions using **`raise`**.
* ✅ Create custom exception classes.
* ✅ Inherit custom exceptions from **`Exception`**.
* ✅ Add meaningful error messages.
* ✅ Catch custom exceptions using `try-except`.
* ✅ Use multiple custom exceptions for different validation rules.
* ✅ Separate application business logic from general Python errors.
* ✅ Build a **Login Validation** system.

---

### Key Takeaways

* Custom exceptions allow you to represent **application-specific errors** clearly.
* The `raise` keyword manually triggers an exception.
* Custom exceptions should normally inherit from Python's built-in `Exception` class.
* Meaningful exception names make programs easier to understand and debug.
* Built-in exceptions should be preferred when they already describe the problem.
* Custom exceptions are especially useful for validation and business rules.
* Validation functions can raise exceptions while higher-level code handles them using `try-except`.
* Good exception design keeps error handling predictable, readable, and maintainable.

---

### What's Next?

**Day 036 - JSON (Settings Manager)**

Tomorrow, you will learn how to work with **JSON**, a popular format for storing and exchanging structured data. You will use JSON to build a **Settings Manager** that can save and load application preferences.
