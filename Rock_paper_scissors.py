import tkinter as tk
import random

# Game logic
def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "You win!"
        global user_score
        user_score += 1
    else:
        result = "You lose!"
        global computer_score
        computer_score += 1

    update_score()
    update_result(result, user_choice, computer_choice)

# GUI setup
user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock Paper Scissors")

result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"You: {user_score} - Computer: {computer_score}", font=("Arial", 14))
score_label.pack(pady=10)

def update_result(result, user_choice, computer_choice):
    result_label.config(text=f"{result}\nYou chose: {user_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}")

def update_score():
    score_label.config(text=f"You: {user_score} - Computer: {computer_score}")

rock_button = tk.Button(root, text="Rock", command=lambda: play_game('rock'), padx=20, pady=10)
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('paper'), padx=20, pady=10)
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('scissors'), padx=20, pady=10)
scissors_button.pack(pady=10)

root.mainloop()
