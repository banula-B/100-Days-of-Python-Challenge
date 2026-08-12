# Day 020 - Review Week

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Consolidate your knowledge of **Phase 1: Python Basics**.
* Apply variables, data types, and operators in complex scenarios.
* Utilize **control flow** (`if-else`, `elif`) and **loops** (`for`, `while`) together.
* Integrate various **data structures** (lists, tuples, dictionaries, and sets) into a single application.
* Build a **Mini Student Management System** to manage student data.

---

## Phase 1 Recap: The Foundations

Over the past 19 days, you have built the essential foundation for Python programming. Here is a quick recap of the core concepts.

### 1. Basic Data Handling (Days 1–4)

You learned how to store information in **variables**, take **user input**, and convert between data types such as integers, floats, and strings.

Example:

```python
age = int(input("Enter age: "))
```

### 2. Logic and Decision Making (Days 5–9)

You mastered `if-elif-else` structures and used **comparison operators** (`==`, `>`, etc.) and **logical operators** (`and`, `or`, `not`) to make programs smarter.

### 3. Iteration and Control (Days 10–14)

You used **while loops** for indefinite tasks and **for loops** with `range()` for definite sequences.

You also learned to control loops using:

* `break`
* `continue`

### 4. Data Structures (Days 15–19)

* **Lists:** Ordered, mutable collections (`append`, `pop`, `sort`).
* **Tuples:** Ordered, immutable collections.
* **Dictionaries:** Key-value pairs for structured data lookup.
* **Sets:** Unordered collections of unique items.

---

## Exercises

### Exercise 1

Create a list of 5 numbers. Use a `for` loop to calculate the sum and the average of these numbers.

### Exercise 2

Write a program that takes a string and returns a **set** of all unique characters in that string.

### Exercise 3

Create a dictionary representing a book with a title, author, and year. Ask the user for a new `year` and update the dictionary only if the input is a valid number.

---

## Mini Project: Mini Student Management System

Create a file named:

```text
student_management.py
```

This project serves as a capstone for Phase 1.

The program should allow you to:

* Add students.
* Store student grades in a list within a dictionary.
* View all student records.
* Calculate the average grade for a student.
* Exit the application.

### Suggested Structure

The main data structure should follow this general concept:

```text
students = {
    "Student Name": [grade1, grade2, grade3]
}
```

### Project Requirements

1. Create a dictionary to store student information.
2. Display a menu with multiple options.
3. Allow the user to add a student and grade.
4. If the student already exists, add the new grade to their existing list.
5. Display all students and their grades.
6. Allow the user to calculate a student's average grade.
7. Handle students who do not exist.
8. Allow the user to exit the program.
9. Use loops, conditions, lists, and dictionaries together.

> **Challenge:** Try to build the project without looking at a complete solution. Use the concepts you learned during Phase 1 to solve the problem yourself.

---

## Common Mistakes

### ❌ Choosing the Wrong Data Structure

**Cause:** Using a list for data that needs unique entries or using a tuple for data that needs to change.

**Solution:** Choose the data structure based on the type of data and operations your program requires.

### ❌ Nested Logic Complexity

**Cause:** Making `if` statements or loops too deeply nested, making code difficult to read.

**Solution:** Try to keep logic flat and use appropriate data structures or dictionary lookups where possible.

### ❌ Input Validation

**Cause:** Assuming users will always enter valid numbers when asked.

**Solution:** Always consider invalid input. You can use methods such as `isdigit()` for basic validation. Later, you will learn `try-except` for more robust error handling.

---

## Summary

Today you learned how to:

* ✅ **Synthesize** all concepts from Phase 1.
* ✅ Build a **multi-feature application** using loops, logic, and dictionaries.
* ✅ **Debug** and refine your foundational Python skills.
* ✅ Combine multiple Python concepts to solve a practical problem.

---

## Key Takeaways

* **Consistency is key:** You have successfully completed the first 20 days of the challenge.
* **Data structure selection** determines how easy your program is to write and maintain.
* The combination of **loops and dictionaries** is useful for building many real-world management systems.
* Reviewing previous concepts helps strengthen your understanding before moving to more advanced topics.

---

## What's Next?

### Day 021 - Functions

You will begin learning how to organize your Python programs using **functions**, making your code more reusable, readable, and maintainable.
