# Day 014 - `break` & `continue`

## 🎯 Objectives

By the end of this lesson, you will be able to:

- Understand and use the **`break` statement** to exit loops early.
- Understand and use the **`continue` statement** to skip the current iteration.
- Control loop execution based on user input or specific conditions.
- Build a **Quiz Game** using `break` and `continue`.

---

# 📚 The `break` Statement

The **`break`** statement immediately terminates a loop.

When Python encounters `break`, it exits the loop and continues executing the code after the loop.

### Example

```python
while True:
    user_input = input("Type 'exit' to quit: ")

    if user_input.lower() == "exit":
        break

    print("You entered:", user_input)

print("Loop finished.")
```

### Output

```text
Type 'exit' to quit: hello
You entered: hello
Type 'exit' to quit: exit
Loop finished.
```

---

# ⏭️ The `continue` Statement

The **`continue`** statement skips the rest of the current iteration.

Instead of ending the loop, Python immediately starts the next iteration.

### Example

```python
for number in range(1, 6):
    if number % 2 != 0:
        continue

    print(number)
```

### Output

```text
2
4
```

The odd numbers are skipped.

---

# 🔍 `break` vs `continue`

| `break` | `continue` |
|----------|------------|
| Ends the entire loop. | Skips only the current iteration. |
| Execution continues after the loop. | Execution continues with the next iteration. |
| Used when you want to stop completely. | Used when you want to ignore specific cases. |

---

# 🚀 Mini Project - Quiz Game

Create a file named **`quiz_game.py`**.

### Requirements

Your program should:

- Ask the user a series of quiz questions.
- Allow the user to type **`quit`** to exit the quiz early using `break`.
- Skip unanswered questions using `continue`.
- Keep track of the user's score.
- Display the final score when the quiz ends.

### Sample Input

```text
What is the capital of France?
Paris

Which planet is known as the Red Planet?
quit
```

### Expected Output

```text
Correct!
Exiting game...
Game Over! Your final score is 1/3.
```

---

# 🏋️ Exercises

## Exercise 1

Use a `for` loop to print the numbers **1 to 10**.

Stop the loop when the number reaches **7** using `break`.

### Expected Output

```text
1
2
3
4
5
6
```

---

## Exercise 2

Create a program that repeatedly asks the user to enter numbers.

- Ignore negative numbers using `continue`.
- Stop the program when the user enters **0** using `break`.

### Sample Input

```text
Enter a number: 5
Enter a number: -3
Enter a number: 10
Enter a number: 0
```

### Expected Output

```text
Total: 15
```

---

## Exercise 3

Search for the word **"Python"** inside the following list:

```python
["Java", "C++", "Python", "JavaScript"]
```

When found, print:

```text
Found it!
```

Then stop searching using `break`.

### Expected Output

```text
Found it!
```

---

# ❌ Common Mistakes

## Using `break` Outside a Loop

Incorrect:

```python
if True:
    break
```

`break` can only be used inside a `for` or `while` loop.

---

## Writing Code After `break`

Incorrect:

```python
for i in range(5):
    break
    print(i)
```

The `print()` statement will never execute because `break` exits the loop immediately.

---

## Infinite Loops with `continue`

Incorrect:

```python
count = 1

while count <= 5:
    if count == 3:
        continue

    count += 1
```

The value of `count` never changes when it is `3`, causing an infinite loop.

Always update the control variable before using `continue` in a `while` loop.

---

# 📝 Summary

Today you learned how to:

- ✅ Exit loops early using `break`.
- ✅ Skip the current iteration using `continue`.
- ✅ Control loop execution based on conditions.
- ✅ Build a Quiz Game using loop control statements.

---

# 🔑 Key Takeaways

- `break` immediately terminates the current loop.
- `continue` skips the current iteration and moves to the next one.
- Both statements are useful for controlling loop behavior.
- Be careful when using `continue` inside `while` loops to avoid infinite loops.

---

# 📖 What's Next?

## Day 015 – Lists