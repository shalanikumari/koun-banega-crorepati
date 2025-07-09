🎮 Program Description: KBC - Quiz Game in Python
This program simulates a Kaun Banega Crorepati (KBC)-style quiz show in Python. The user is presented with multiple-choice questions, and for each correct answer, they win a certain amount of virtual money. The quiz gets progressively harder, and the stakes increase with each correct answer.

✅ Key Components of the Program:
1. Welcome Message:
python
Copy
Edit
print("Welcome to KBC!")
Displays a friendly greeting to the user.

2. Question Bank:
python
Copy
Edit
questions = [ ... ]
A list of questions, each containing:

The question itself.

Four answer choices.

The correct answer's index (as an integer, 1–4).

3. Prize Money Levels:
python
Copy
Edit
levels = [1000, 2000, 3000, ..., 75000000]
Each question corresponds to a specific prize level that increases with each round.

4. Quiz Logic Loop:
python
Copy
Edit
for i in range(0, len(questions)):
    ...
Loops through all questions one by one.

Displays the question, its options, and prize level.

Accepts the user's answer using input().

5. Answer Validation:
python
Copy
Edit
if reply == question[-1]:
Checks if the selected answer is correct.

If correct:

Informs the player.

Updates the guaranteed amount at milestones (5th, 10th, 15th, and final question).

If incorrect:

Ends the game.

Displays the amount the user is taking home (based on the last milestone reached).

6. Milestone Amounts:
python
Copy
Edit
if(i == 4): money = 1000
elif (i == 9): money = 320000
...
These are safe money levels: the player is guaranteed to take home at least this amount if they cross the milestone.

📝 Example Gameplay Flow:
User sees question 1 for ₹1000.

Chooses an answer.

If correct, moves to question 2 for ₹2000.

This continues up to question 16 (₹7.5 crore).

A wrong answer ends the game immediately, and the player takes home only the last milestone amount.
