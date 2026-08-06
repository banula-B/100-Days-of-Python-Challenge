# Quiz Game

questions = [
    ("What is the capital of France?", "Paris"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What is 5 + 7?", "12")
]

score = 0

for question, answer in questions:
    print(question)
    user_answer = input().strip()

    # Exit the quiz early
    if user_answer.lower() == "quit":
        print("Exiting game...")
        break

    # Skip unanswered questions
    if user_answer == "":
        print("Question skipped.")
        continue

    # Check the answer
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")

print(f"Game Over! Your final score is {score}/{len(questions)}.")