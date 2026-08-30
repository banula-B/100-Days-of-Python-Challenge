# Day 038 - Datetime

## 🎯 Objectives

By the end of this lesson, you will be able to:

* Understand Python's built-in **`datetime`** module and its core classes.
* Get the **current local date and time** programmatically.
* Format dates and times into customized, readable strings using **`strftime()`**.
* Convert (parse) date strings back into datetime objects using **`strptime()`**.
* Perform date arithmetic using **`timedelta`**.
* Build an **Event Countdown Tracker** project.

---

# What is the `datetime` Module?

In programming, working with dates and times is a common requirement.

Examples include:

* Timestamping log files.
* Recording user registration times.
* Scheduling tasks.
* Tracking deadlines.
* Calculating durations.
* Creating reminders.
* Managing appointments.

Python provides a powerful built-in module called **`datetime`** for working with dates and times.

Import the module with:

```python
import datetime
```

---

# Core `datetime` Classes

The `datetime` module contains several important classes.

The three most commonly used classes are:

### 1. `date`

Represents a calendar date without a time.

```text
Year + Month + Day
```

Example:

```python
from datetime import date

today = date.today()

print(today)
```

---

### 2. `time`

Represents a time independently of a date.

```text
Hour + Minute + Second + Microsecond
```

Example:

```python
from datetime import time

meeting_time = time(14, 30, 0)

print(meeting_time)
```

---

### 3. `datetime`

Represents both a date and a time.

```text
Year + Month + Day + Hour + Minute + Second
```

Example:

```python
from datetime import datetime

now = datetime.now()

print(now)
```

---

# Getting the Current Date and Time

To retrieve the current local date and time, use:

```python
from datetime import datetime

now = datetime.now()

print("Current Date & Time:", now)
```

You can access individual components of the datetime object.

```python
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
```

---

# Getting Today's Date

If you only need the current date, use `date.today()`.

```python
from datetime import date

today = date.today()

print(today)
```

Example output:

```text
2026-08-30
```

---

# Getting the Current Time

If you need the current time, you can obtain it from a datetime object.

```python
from datetime import datetime

now = datetime.now()

print(now.time())
```

---

# Formatting Dates and Times with `strftime()`

Dates and times are often displayed differently depending on the application.

For example:

```text
2026-08-30
```

might be displayed as:

```text
August 30, 2026
```

Python provides `strftime()` to convert a datetime object into a formatted string.

The **`f`** in `strftime` stands for **format**.

---

## Common `strftime()` Format Codes

| Code | Meaning              | Example  |
| ---- | -------------------- | -------- |
| `%Y` | Four-digit year      | `2026`   |
| `%y` | Two-digit year       | `26`     |
| `%m` | Month number         | `08`     |
| `%B` | Full month name      | `August` |
| `%b` | Short month name     | `Aug`    |
| `%d` | Day of the month     | `30`     |
| `%A` | Full weekday name    | `Sunday` |
| `%a` | Short weekday name   | `Sun`    |
| `%H` | Hour, 24-hour format | `14`     |
| `%I` | Hour, 12-hour format | `02`     |
| `%M` | Minute               | `45`     |
| `%S` | Second               | `30`     |
| `%p` | AM/PM                | `PM`     |

---

## Example

```python
from datetime import datetime

now = datetime.now()

readable_date = now.strftime("%B %d, %Y - %I:%M %p")

print(readable_date)
```

Example output:

```text
August 30, 2026 - 10:46 AM
```

The exact output depends on when the program is executed.

---

# Parsing Dates with `strptime()`

Sometimes dates come from:

* User input.
* CSV files.
* JSON files.
* Databases.
* APIs.
* Text files.

These dates are usually stored as strings.

For example:

```python
date_string = "2026-08-30 14:30:00"
```

A string cannot directly be used for datetime calculations.

Python provides `strptime()` to convert a formatted string into a datetime object.

The **`p`** in `strptime` stands for **parse**.

```python
from datetime import datetime

date_string = "2026-08-30 14:30:00"

date_object = datetime.strptime(
    date_string,
    "%Y-%m-%d %H:%M:%S"
)

print(date_object)
```

You can then access its components:

```python
print(date_object.year)
print(date_object.month)
print(date_object.day)
```

---

# `strftime()` vs `strptime()`

This is an important distinction.

| Function     | Direction         | Purpose           |
| ------------ | ----------------- | ----------------- |
| `strftime()` | Datetime → String | Format a datetime |
| `strptime()` | String → Datetime | Parse a datetime  |

### Easy Memory Trick

* **`strftime()`** → **f = format**
* **`strptime()`** → **p = parse**

Think:

```text
datetime → strftime() → string
string → strptime() → datetime
```

---

# Date Arithmetic with `timedelta`

Python provides the `timedelta` class for representing a duration of time.

You can use it to:

* Add days.
* Subtract days.
* Add hours.
* Subtract minutes.
* Calculate differences between dates and times.

Import it using:

```python
from datetime import datetime, timedelta
```

---

## Adding Time

For example, to calculate the date two weeks from today:

```python
from datetime import datetime, timedelta

today = datetime.now()

two_weeks_later = today + timedelta(days=14)

print(two_weeks_later)
```

---

## Subtracting Time

You can also subtract a duration.

```python
three_hours_ago = today - timedelta(hours=3)

print(three_hours_ago)
```

---

## Adding Minutes

```python
future_time = today + timedelta(minutes=30)

print(future_time)
```

---

## Calculating the Difference Between Dates

You can subtract one datetime object from another.

```python
from datetime import datetime

today = datetime.now()

new_year = datetime(2027, 1, 1)

time_remaining = new_year - today

print(time_remaining)
```

The result is a `timedelta` object.

You can access the number of days:

```python
print(time_remaining.days)
```

---

# Common `timedelta` Arguments

You can create durations using:

```python
timedelta(
    days=0,
    seconds=0,
    minutes=0,
    hours=0,
    weeks=0
)
```

Examples:

```python
timedelta(days=7)
timedelta(hours=5)
timedelta(minutes=30)
timedelta(seconds=10)
timedelta(weeks=2)
```

---

# Calculating Total Seconds

A `timedelta` object provides `total_seconds()`.

```python
from datetime import timedelta

duration = timedelta(days=1, hours=2)

print(duration.total_seconds())
```

This is useful when building countdown timers or calculating precise durations.

---

# Comparing Datetimes

Datetime objects can be compared using normal comparison operators.

```python
from datetime import datetime

now = datetime.now()

future = datetime(2027, 1, 1)

print(future > now)
```

You can use:

```text
>
<
>=
<=
==
!=
```

This is useful for checking whether:

* A deadline has passed.
* An event is upcoming.
* A subscription has expired.
* A scheduled task should run.

---

# Exercises

## Exercise 1

Print the current time in the following format:

```text
HH:MM:SS
```

Use the 24-hour clock.

---

## Exercise 2

Write a program that asks the user to enter their birthday in the format:

```text
DD/MM/YYYY
```

Parse the string into a Python datetime object and print the day of the week they were born on.

### Hint

Use:

```python
strftime("%A")
```

---

## Exercise 3

Write a program that calculates and prints the exact date and time it will be **10,000 minutes** from the current moment.

Use `timedelta`.

---

# Mini Project: Event Countdown Tracker

## Project Overview

Build an **Event Countdown Tracker** that allows users to enter an event name and its target date and time.

The application should calculate how much time remains until the event.

For example:

```text
Event: Final Exam
Target: 2026-12-20 09:00
```

The program should calculate the remaining:

* Days
* Hours
* Minutes

If the event has already passed, the program should notify the user.

---

## Project Requirements

Your program should:

1. Ask the user for an event name.
2. Ask the user for the event date and time.
3. Accept the date format:

```text
YYYY-MM-DD HH:MM
```

4. Convert the user's input into a datetime object using `strptime()`.
5. Get the current date and time using `datetime.now()`.
6. Compare the target datetime with the current datetime.
7. Calculate the remaining time using `timedelta`.
8. Display the remaining days, hours, and minutes.
9. Detect when the event has already passed.
10. Handle invalid date input using `try` / `except`.

---

## Suggested Program Structure

Consider organising the project into these logical steps:

```text
1. Display program title
2. Get event name
3. Get target date and time
4. Parse the input
5. Get current datetime
6. Compare target and current time
7. Calculate remaining duration
8. Display countdown
9. Handle past events
10. Handle invalid input
```

---

## Example Input

```text
Enter the name of your event: Final Exam
Enter the event date: 2026-12-20 09:00
```

---

## Example Output

```text
Countdown to 'Final Exam':

XX Days, XX Hours, and XX Minutes remaining!
```

> The exact values will depend on when the program is executed.

---

## Skills Practiced

This project gives you practice with:

* `datetime`
* `datetime.now()`
* `datetime.strptime()`
* `strftime()`
* `timedelta`
* Datetime comparisons
* String formatting
* User input
* Exception handling
* `ValueError`
* Date arithmetic
* Functions and program structure

---

# Common Mistakes

## ❌ Confusing `strftime()` and `strptime()`

### Cause

Using `strptime()` when you want to format a datetime object, or using `strftime()` when you need to parse a string.

### Solution

Remember:

* **`strftime()`** → Format datetime into a string.
* **`strptime()`** → Parse a string into a datetime.

```text
datetime → strftime() → string

string → strptime() → datetime
```

---

## ❌ Mismatched Parsing Formats

### Cause

Trying to parse:

```text
2026/08/30
```

using:

```python
"%Y-%m-%d"
```

The separators and structure must match.

### Correct Example

For:

```text
2026-08-30
```

use:

```python
"%Y-%m-%d"
```

For:

```text
30/08/2026
```

use:

```python
"%d/%m/%Y"
```

---

## ❌ Forgetting That User Input Is a String

When the user enters:

```text
2026-08-30 14:30
```

Python initially receives it as a string.

You cannot perform datetime calculations directly on it.

You need to parse it first:

```python
datetime.strptime(date_string, "%Y-%m-%d %H:%M")
```

---

## ❌ Incorrect Time Calculations

When calculating hours and minutes from a `timedelta`, remember that:

```text
1 day = 24 hours
1 hour = 60 minutes
1 minute = 60 seconds
```

For countdown applications, `total_seconds()` can be useful when you need to break a duration into individual components.

---

## ❌ Mixing Naive and Timezone-Aware Datetimes

A **naive datetime** does not contain timezone information.

Example:

```python
datetime.now()
```

A **timezone-aware datetime** contains timezone information.

Comparing a naive datetime with an aware datetime can result in a `TypeError`.

### Solution

For simple beginner programs, consistently use naive datetimes.

For larger applications that work across multiple time zones, learn Python's timezone tools such as `zoneinfo`.

---

# Summary

Today you learned how to:

* ✅ Import Python's built-in **`datetime`** module.
* ✅ Understand the `date`, `time`, and `datetime` classes.
* ✅ Get the current date and time using `datetime.now()`.
* ✅ Extract individual date and time components.
* ✅ Format datetime objects using `strftime()`.
* ✅ Parse date strings using `strptime()`.
* ✅ Perform date arithmetic using `timedelta`.
* ✅ Calculate differences between dates and times.
* ✅ Compare datetime objects.
* ✅ Build an **Event Countdown Tracker**.

---

# Key Takeaways

* The **`datetime`** module provides tools for working with dates and times.
* A `date` represents a date without a time.
* A `time` represents a time without a date.
* A `datetime` combines both date and time.
* `strftime()` converts a datetime object into a formatted string.
* `strptime()` converts a formatted string into a datetime object.
* `timedelta` represents a duration and makes date arithmetic easier.
* Datetime objects can be compared using standard comparison operators.
* Always make sure your parsing format exactly matches the input string.
* Timezone-aware applications require additional consideration when working with dates and times.

---

# What's Next?

## Day 039 - OS Module (System Operations)

In the next lesson, you will learn how Python can interact with the **operating system** using the built-in `os` module.

You will learn how to:

* Work with directories.
* Create and remove folders.
* Check whether files and folders exist.
* Rename files and directories.
* List directory contents.
* Work with file and directory paths.
* Build a practical **File Organizer** project.
