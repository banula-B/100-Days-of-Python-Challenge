Day 041 - Classes & Objects# Day 041 - Classes & Objects

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand the fundamental paradigm of **Object-Oriented Programming (OOP)**.
* Define a **Class** as a blueprint and instantiate **Objects** from it.
* Understand the purpose of the constructor method **`__init__()`**.
* Master the use of the **`self`** parameter to access and store instance attributes.
* Build a foundational **Student Class** project to model real-world student entities.

---

# What is Object-Oriented Programming?

So far in this challenge, you have primarily written code using **procedural programming**, where code is structured around functions that perform actions on data.

While procedural programming is highly effective for small scripts, larger applications can become difficult to manage when data and functions are kept separate.

**Object-Oriented Programming (OOP)** is a programming paradigm that allows you to group related **data** and **behaviors** together into unified structures called **objects**.

OOP helps you model real-world entities such as:

* Bank accounts.
* Users.
* Cars.
* Products.
* Students.
* Employees.

Instead of keeping all related information in separate variables and functions, OOP allows you to organise them into a single structure.

---

# Classes vs. Objects

Two of the most important concepts in OOP are **classes** and **objects**.

## Class

A **class** is a user-defined **blueprint** or template for creating objects.

A class defines:

* What data an object should contain.
* What actions an object can perform.

A class itself is a blueprint. It describes what an object should look like and how it should behave.

---

## Object

An **object** is an **instance of a class**.

When you create an object from a class, the object receives its own data and can use the behaviors defined by the class.

### Real-World Analogy

Think about building a house.

```text
Class
  ↓
House Blueprint
  ↓
Objects
  ↓
House 1
House 2
House 3
```

The blueprint describes how a house should be constructed.

Each physical house created from that blueprint is an individual object.

Similarly:

```text
Class → Student
Objects → Alice, Bob, Charlie
```

Each student object can contain different information while following the same structure.

---

# Creating a Class

Python uses the `class` keyword to define a class.

Basic structure:

```python
class Student:
    pass
```

The `pass` statement is used when you want to create an empty class temporarily.

---

# The Constructor: `__init__()`

When creating an object, you often need to provide initial data.

For example, a student might need:

* Name.
* Student ID.
* Age.
* Grades.

Python provides a special method called:

```python
__init__()
```

This method is automatically called when a new object is created.

It is commonly used to initialise an object's attributes.

---

# Understanding `self`

The **`self`** parameter refers to the **current object instance**.

It allows an object to store and access its own data.

Consider:

```python
class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```

Here:

```text
name
```

is the value passed into the constructor.

While:

```text
self.name
```

is an attribute stored inside the particular object.

---

# Instance Attributes

An **instance attribute** is data that belongs to a specific object.

For example:

```python
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Bella", "Poodle")
```

The two objects contain different data:

```text
dog1
├── name → Buddy
└── breed → Golden Retriever

dog2
├── name → Bella
└── breed → Poodle
```

Changing one object does not automatically change the other.

---

# Accessing Attributes

You can access an object's attributes using **dot notation**.

Example:

```python
print(dog1.name)
print(dog2.breed)
```

The output would be:

```text
Buddy
Poodle
```

The general pattern is:

```text
object.attribute
```

---

# Basic Class Structure

A simple class can be organised like this:

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

You can then create objects:

```python
person1 = Person("Alice", 20)
person2 = Person("Bob", 25)
```

Each object maintains its own values.

---

# Understanding `self` Step by Step

Consider:

```python
class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
```

When you create:

```python
student1 = Student("Alice", "S101")
```

Python stores:

```text
student1.name
    ↓
"Alice"

student1.student_id
    ↓
"S101"
```

When you create another object:

```python
student2 = Student("Bob", "S102")
```

Python stores:

```text
student2.name
    ↓
"Bob"

student2.student_id
    ↓
"S102"
```

The `self` reference ensures that the data belongs to the correct object.

---

# Exercises

## Exercise 1

Create a class called `Book` that has three instance attributes:

* `title`
* `author`
* `pages`

Instantiate two different book objects and print their titles.

---

## Exercise 2

Create a class called `Car` with the attributes:

* `brand`
* `model`
* `mileage`

Instantiate a car and then manually update its `mileage` attribute from `0` to `150`.

---

## Exercise 3

Define a class called `Coordinate` with the attributes:

* `x`
* `y`

Write a function outside the class called:

```python
distance_from_origin(coord)
```

The function should accept a `Coordinate` object and return its mathematical distance from `(0, 0)` using:

```text
√(x² + y²)
```

---

# Mini Project: Student Class

## Project Overview

Create a file named:

```text
student_class.py
```

The goal of this project is to demonstrate how OOP can be used to model students as structured objects rather than tracking their names, grades, and subjects inside loose dictionaries.

You will create a `Student` class that stores basic student information and calculates the student's overall average score.

---

## Project Requirements

Your `Student` class should contain:

* Student name.
* Student ID.
* A list of grades.

The class should also contain a method that:

1. Checks whether the student has any grades.
2. Calculates the average grade.
3. Returns the calculated average.

---

## Suggested Class Structure

Your class should conceptually contain:

```text
Student
│
├── Attributes
│   ├── name
│   ├── student_id
│   └── grades
│
└── Methods
    └── calculate_average()
```

---

## Project Tasks

### Task 1 — Create the Class

Create a class called:

```python
Student
```

---

### Task 2 — Create the Constructor

Use:

```python
__init__()
```

to initialise:

* `name`
* `student_id`
* `grades`

---

### Task 3 — Store Student Information

Use `self` to store the values as instance attributes.

Each student object should maintain its own information.

---

### Task 4 — Create the Average Method

Create a method called:

```python
calculate_average()
```

The method should:

* Return `0.0` if there are no grades.
* Otherwise calculate the average using the grades list.

---

### Task 5 — Create Multiple Student Objects

Create at least two different student objects.

For example:

```text
Student 1
Name: Alice Smith
ID: S101

Student 2
Name: Bob Jones
ID: S102
```

Each student should have their own grades.

---

### Task 6 — Display Student Information

Display:

* Student name.
* Student ID.
* Grades.
* Average grade.

Format the average so that it displays **two decimal places**.

Example:

```text
Student: Alice Smith (S101)
Grades: [85, 90, 78]
Average: 84.33%
```

---

## Skills Practiced

This project gives you practice with:

* Classes.
* Objects.
* Constructors.
* `__init__()`.
* `self`.
* Instance attributes.
* Instance methods.
* Lists.
* Functions.
* Basic calculations.
* Object instantiation.
* Dot notation.

---

# Common Mistakes

## ❌ Forgetting `self` in Method Definitions

### Cause

Defining the constructor like:

```python
def __init__(name, age):
```

or defining an instance method without `self`.

Python will raise a `TypeError` when you attempt to use the method or create the object.

### Solution

Always include `self` as the first parameter of an instance method:

```python
def __init__(self, name, age):
```

---

## ❌ Forgetting `self` When Accessing Attributes

### Cause

Inside a class method, writing:

```python
print(name)
```

instead of:

```python
print(self.name)
```

Python will search for a local or global variable named `name`.

If one does not exist, a `NameError` may occur.

### Solution

Use:

```python
self.name
```

when accessing the object's instance attribute.

---

## ❌ Confusing Parameters with Instance Attributes

Consider:

```python
def __init__(self, name):
    self.name = name
```

The two `name` references have different roles:

```text
name
↓
Parameter

self.name
↓
Instance attribute
```

The assignment connects the constructor parameter to the object's stored attribute.

---

## ❌ Using `name = name` Instead of `self.name = name`

### Cause

Writing:

```python
name = name
```

does not create an instance attribute.

It simply assigns the parameter back to itself.

### Solution

Use:

```python
self.name = name
```

This stores the value inside the object.

---

## ❌ Thinking Every Object Shares the Same Instance Data

When you create:

```python
student1 = Student(...)
student2 = Student(...)
```

each object has its own instance attributes.

For example:

```text
student1.name → Alice
student2.name → Bob
```

Changing:

```python
student1.name
```

does not automatically change:

```python
student2.name
```

---

# Summary

Today you started **Phase 3: Object-Oriented Programming**.

You learned how to:

* ✅ Understand the basic concept of **Object-Oriented Programming**.
* ✅ Define a class using the `class` keyword.
* ✅ Understand classes as blueprints.
* ✅ Create objects from classes.
* ✅ Understand the purpose of `__init__()`.
* ✅ Use `self` to reference the current object.
* ✅ Create and store instance attributes.
* ✅ Access attributes using dot notation.
* ✅ Understand the difference between constructor parameters and instance attributes.
* ✅ Build a foundational **Student Class** project.

---

# Key Takeaways

* A **class** is a blueprint for creating objects.
* An **object** is an instance of a class.
* `__init__()` is used to initialise an object's data when the object is created.
* `self` refers to the current instance.
* Instance attributes belong to individual objects.
* Different objects created from the same class can contain different data.
* Dot notation is used to access object attributes.
* OOP allows related **data and behaviour** to be organised together.
* Classes make it easier to model real-world entities in code.

---

# What's Next?

## Day 042 - Instance Methods & String Representation (`__str__`)

Tomorrow you will continue learning OOP by exploring:

* Instance methods.
* How methods interact with object attributes.
* Returning values from methods.
* The `__str__()` special method.
* Customising how objects are displayed.
* Improving the readability of your classes.
