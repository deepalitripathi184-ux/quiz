# General Knowledge Quiz

print("=================================")
print("      GENERAL KNOWLEDGE QUIZ     ")
print("=================================")

score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
answer = input("\n2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Question 3
answer = input("\n3. Who wrote 'Romeo and Juliet'? ").strip().lower()

if answer == "william shakespeare" or answer == "shakespeare":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is William Shakespeare.")

# Final Score
print("\n=================================")
print(f"Your Final Score: {score}/3")
print("=================================")

if score == 3:
    print("Excellent! You got all answers correct.")
elif score == 2:
    print("Good Job!")
elif score == 1:
    print("Keep Learning!")
else:
    print("Better Luck Next Time!")