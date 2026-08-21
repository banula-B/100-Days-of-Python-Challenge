# Day 029 - Modules

#### 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the concept of **modules** and how they keep code organised.
* Import standard library modules using `import`, `from ... import`, and `import ... as`.
* Create and use **custom modules** across different files.
* Build a multi-file **Math Toolkit** project.

---

### What is a Module?

A **module** is simply a Python file containing definitions and statements. Any Python file with a `.py` extension can be used as a module.

As programs grow, keeping all code in one file can become difficult to manage. Modules allow you to break a program into smaller, self-contained, reusable pieces.

---

### Importing Modules

Python provides several ways to import modules and their contents.

#### 1. Importing Entire Modules

You can import an entire module using the `import` keyword.

When you use a function or variable from the module, you access it using **dot notation**.

**Example concept:**

* Import the `math` module.
* Access mathematical functions using `math.function_name`.
* For example, the `math` module provides functions such as square root, trigonometry, logarithms, and more.

**Key idea:**

> `import module_name`

Then access its contents using:

> `module_name.item`

---

#### 2. Importing Specific Attributes

If you only need specific functions or variables from a module, you can import them directly.

For example, the `math` module contains:

* `pi`
* `sin`
* `cos`
* `sqrt`
* `factorial`

You can import only the attributes you need.

**Key idea:**

> `from module_name import item`

This allows you to use the imported item directly without writing the module name every time.

---

#### 3. Using Aliases

An **alias** allows you to give a shorter or alternative name to a module when importing it.

This can be useful when:

* A module has a long name.
* You frequently use a module.
* You want to avoid naming conflicts.
* You want your code to be easier to read.

**Key idea:**

> `import module_name as alias`

For example, the `random` module could be given a shorter alias such as `rand`.

---

### Creating a Custom Module

Creating your own module is as simple as creating a new Python file.

For example:

```text
project/
│
├── main.py
└── helpers.py
```

The `helpers.py` file can contain reusable functions.

The `main.py` file can then import those functions and use them.

This allows you to separate different parts of your program into different files.

### Benefits of Custom Modules

Custom modules help you:

* Organise large programs.
* Reuse code.
* Reduce duplication.
* Separate responsibilities.
* Make programs easier to maintain.
* Keep individual files smaller and easier to understand.

---

### Exercises

#### Exercise 1 - Random Dice

Use Python's built-in `random` module to create a program that simulates rolling a six-sided die.

**Requirements:**

* Import the `random` module.
* Generate a random number between 1 and 6.
* Display the result.

**Expected behaviour:**

```text
Rolling the dice...
You rolled: 4
```

The number should be different on different executions because it is randomly generated.

---

#### Exercise 2 - Greeting Module

Create a custom module named:

```text
helper.py
```

Inside the module, create a function named:

```text
greet(name)
```

The function should return a greeting containing the provided name.

Then create another Python file that:

* Imports the custom module.
* Calls the `greet()` function.
* Displays the returned greeting.

**Suggested structure:**

```text
project/
│
├── main.py
└── helper.py
```

---

#### Exercise 3 - Math Import

Use the `from ... import ...` syntax to import:

* `pi`
* `sin`

from Python's `math` module.

Use them to calculate:

```text
sin(pi / 2)
```

**Expected result:**

```text
1.0
```

---

### Mini Project: Math Toolkit

Build a small **Math Toolkit** application using multiple Python files.

The purpose of this project is to practise:

* Creating custom modules.
* Importing custom modules.
* Importing standard library modules.
* Using different import styles.
* Organising a project across multiple files.

### Project Structure

Your project should contain at least:

```text
math-toolkit/
│
├── my_math.py
└── toolkit.py
```

### File 1 - `my_math.py`

Create a custom module containing your own mathematical functions.

Your module should include:

#### `is_prime(n)`

Determine whether a number is a prime number.

The function should return:

* `True` if the number is prime.
* `False` otherwise.

#### `factorial(n)`

Calculate the factorial of a number.

For example:

```text
5! = 120
```

You should implement the logic yourself rather than importing a ready-made factorial function.

---

### File 2 - `toolkit.py`

Create the main application.

The application should:

1. Import Python's built-in `math` module.
2. Import your custom `my_math` module.
3. Ask the user to enter an integer.
4. Calculate the square root using the standard `math` module.
5. Check whether the number is prime using your custom module.
6. Calculate the factorial using your custom module.
7. Display all results clearly.

### Example Output

Your completed application should produce output similar to:

```text
--- Math Toolkit App ---

Enter an integer: 7

Standard Math -> Square root of 7 is: 2.65
Custom Math   -> 7 is a prime number!
Custom Math   -> The factorial of 7 is: 5040
```

**Do not copy an implementation for this project. Build the modules and functions yourself using what you learned today.**

---

### Common Mistakes

#### ❌ File Naming Collisions (Shadowing)

**Cause:** Naming your script the same as a built-in module.

Examples:

```text
math.py
random.py
```

If you create a file named `math.py` and then try to import `math`, Python may import your local file instead of the official standard library module.

This can lead to unexpected errors such as `AttributeError`.

**Solution:**

Use descriptive names for your own files and avoid names that conflict with Python modules.

---

#### ❌ Using Wildcard Imports

Avoid:

```text
from module import *
```

Wildcard imports bring everything from a module into the current namespace.

This can:

* Make code difficult to understand.
* Cause naming conflicts.
* Overwrite existing names.
* Make it unclear where functions came from.

**Better approach:**

Explicitly import the functions or variables you actually need.

---

#### ❌ Circular Imports

A circular import happens when:

* Module A imports Module B.
* Module B imports Module A.

This creates a circular dependency and can cause import errors or unexpected behaviour.

**Solution:**

Organise your modules carefully and avoid unnecessary dependencies between modules.

---

#### ❌ Running the Wrong File

When working with multiple modules, make sure you run the correct main application file.

For example:

```text
math-toolkit/
│
├── my_math.py
└── toolkit.py
```

You should normally run:

```text
toolkit.py
```

rather than the supporting module directly.

---

### Summary

Today you learned how to:

* ✅ **Organise code** into manageable, modular files.
* ✅ Use Python's built-in modules.
* ✅ Use different **import styles**.
* ✅ Create your own custom modules.
* ✅ Import custom modules into another Python file.
* ✅ Build a multi-file Python application.

---

### Key Takeaways

* Every Python file can act as a **module**.
* Modules help organise large programs.
* Modules allow you to **reuse code** across multiple programs.
* Python provides many useful **standard library modules**.
* You can create your own custom modules.
* `import` imports an entire module.
* `from ... import ...` imports specific attributes.
* `as` creates an alias.
* Avoid naming your files after standard library modules.
* Avoid unnecessary wildcard and circular imports.

---

### What's Next?

## Day 030 - Packages

Tomorrow you will learn how to organise **multiple modules into packages**.

You will move from:

```text
Individual Python files
        ↓
Modules
        ↓
Multiple modules
        ↓
Packages
```

This will introduce a more structured way to organise larger Python projects.
