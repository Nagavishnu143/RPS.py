import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")


def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")


rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))
result_label = tk.Label(root, text="")


rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)
result_label.pack(pady=10)


root.mainloop()
