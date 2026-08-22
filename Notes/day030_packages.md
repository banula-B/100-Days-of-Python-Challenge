# Day 030 - Packages

#### 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand what a **package** is and how it differs from a module.
* Create a **directory structure** for a Python package.
* Understand the purpose of the **`__init__.py`** file.
* Import modules from nested directories using **dot notation**.
* Build a **Utility Package** project to group related tools.

---

### What is a Package?

While a **module** is a single Python file, a **package** is a collection of modules organized in a **directory (folder)** structure.

Packages allow you to group multiple related modules together under a common namespace, making larger codebases easier to navigate, maintain, and scale.

A package traditionally contains a special file named **`__init__.py`**.

**Typical Package Directory Structure:**

```text
my_package/
│
├── __init__.py
├── string_utils.py
└── math_utils.py
```

* `__init__.py` → Initializes the package.
* `string_utils.py` → Contains string-related functions.
* `math_utils.py` → Contains mathematical functions.

---

### Module vs Package

| Module                                           | Package                                   |
| ------------------------------------------------ | ----------------------------------------- |
| A single `.py` file                              | A directory containing related modules    |
| Contains functions, classes, and variables       | Organizes multiple modules                |
| Example: `math_utils.py`                         | Example: `my_package/`                    |
| Suitable for smaller collections of related code | Useful for larger, organized applications |

**Simple way to remember:**

> A **module** is a file.
> A **package** is a folder that organizes modules.

---

### The Role of `__init__.py`

The `__init__.py` file is associated with package initialization.

It can be:

* Completely **empty**.
* Used to expose selected functions or classes at the package level.
* Used with the `__all__` list to control exported names.
* Used to import selected functions from sub-modules.

For example:

```text
my_package/
│
├── __init__.py
├── string_utils.py
└── math_utils.py
```

An empty `__init__.py` is perfectly valid.

> **Note:** Python 3.3+ also supports namespace packages that do not require `__init__.py`, but including `__init__.py` remains common and useful for regular Python packages.

---

### Importing from a Package

There are several ways to import modules and functions from a package.

#### 1. Importing the Entire Module

```python
import my_package.string_utils

# Usage
shouted = my_package.string_utils.shout("hello")
```

This imports the complete module and accesses its functions through the package path.

---

#### 2. Importing a Module with an Alias

```python
import my_package.string_utils as s_utils

# Usage
shouted = s_utils.shout("hello")
```

An alias can make long module names easier to use.

---

#### 3. Importing Specific Functions Directly

```python
from my_package.string_utils import shout

# Usage
shouted = shout("hello")
```

This allows you to use the function directly without repeatedly writing the module name.

---

### Dot Notation

When working with packages, **dot notation** represents the relationship between directories, packages, modules, and objects.

For example:

```python
my_package.string_utils.shout()
```

Here:

* `my_package` → Package
* `string_utils` → Module
* `shout` → Function

This hierarchical structure becomes especially useful when working with large applications containing many packages and modules.

---

### Nested Packages

Packages can also contain other packages.

Example:

```text
project/
│
├── main.py
└── utilities/
    ├── __init__.py
    ├── text/
    │   ├── __init__.py
    │   └── string_utils.py
    └── math/
        ├── __init__.py
        └── number_utils.py
```

A function inside `string_utils.py` could be imported using:

```python
from utilities.text.string_utils import some_function
```

The dots represent the hierarchy of the package structure.

---

### Exercises

#### Exercise 1

Draw or describe a folder structure for a package called `games` that has two modules:

* `chess.py`
* `tic_tac_toe.py`

Include the appropriate initialization file.

---

#### Exercise 2

Explain the difference between a **module** and a **package** in your own words.

---

#### Exercise 3

Assume you have a package called `weather` containing a module called `forecast.py`, which has a function called `get_temp()`.

Write three different import statements that could be used to access `get_temp()`.

---

### Mini Project: Utility Package

Create a folder structure for a package named `my_utilities`.

The package should contain two helper modules:

* One for processing strings.
* One for basic calculations.

**Directory Setup:**

```text
project/
│
├── main.py
└── my_utilities/
    ├── __init__.py
    ├── strings.py
    └── numbers.py
```

#### Project Requirements

Your package should provide:

**String utilities:**

* Reverse a string.
* Convert a string into alternating uppercase and lowercase characters.

**Number utilities:**

* Check whether a number is even.
* Calculate the percentage of one value relative to another.

The `main.py` file should import functions from the custom package and demonstrate that they work correctly.

> **Note:** The project implementation is intentionally left for you to complete as practice.

---

### Common Mistakes

#### ❌ `ModuleNotFoundError`

**Cause:** Running `main.py` while the terminal's working directory is inside the package folder instead of the outer project folder.

**Solution:** Run Python commands from the parent directory containing both `main.py` and the package directory.

For example:

```text
project/
│
├── main.py
└── my_utilities/
```

Run the application from inside `project/`.

---

#### ❌ Confusing Local Folders with Packages

**Cause:** Assuming every directory automatically behaves like a traditional Python package.

**Solution:** For regular packages, include an `__init__.py` file. Python 3.3+ supports namespace packages without one, but explicitly including it can make the package structure clearer.

---

#### ❌ Circular Package Imports

**Cause:** Two modules or packages depend on each other.

For example:

```text
package_a → package_b
package_b → package_a
```

This can create import problems and make the application difficult to maintain.

**Solution:**

* Avoid unnecessary circular dependencies.
* Keep modules focused on specific responsibilities.
* Move shared functionality into a separate module when appropriate.

---

#### ❌ Running Python from the Wrong Directory

Python resolves imports based partly on the current environment and module search path.

A structure such as:

```text
project/
│
├── main.py
└── my_utilities/
    ├── __init__.py
    └── strings.py
```

should normally be executed from the `project/` directory:

```bash
python main.py
```

---

### Summary

Today you learned how to:

* ✅ Define and structure a **Python Package**.
* ✅ Understand the difference between a **module** and a **package**.
* ✅ Understand the purpose of **`__init__.py`**.
* ✅ Import modules and functions from packages.
* ✅ Use **dot notation** when navigating package hierarchies.
* ✅ Understand nested packages.
* ✅ Organize related utilities into separate modules.

---

### Key Takeaways

* A **module** is generally a single Python file.
* A **package** organizes related modules into a directory structure.
* `__init__.py` is commonly used to define and initialize regular Python packages.
* Packages help keep large Python projects organized.
* Dot notation represents relationships within package structures.
* Running your main application from the appropriate project root helps avoid import problems.
* Good package organization makes code easier to maintain, reuse, and scale.

---

### What's Next?

**Day 031 - File Reading**
