import random
# Rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock,paper,scissors]

print("Welcome to Rock paper scissors")
user_input = int(input("What do u want to choose. 0 for rock, 1 for paper, 2 for scissors:\n"))

if user_input >=0 or user_input <3:
    print(game_images[user_input])
else:
    print("Choose a valid option.")

computer_ans = random.randint(0,2)
print(f"Computer chooses:\n{game_images[computer_ans]}")


if user_input == 0 and computer_ans == 1:
    print("Computer Won.")
elif user_input == 0 and computer_ans == 2:
    print("Player Wins.")
elif user_input == 0 and computer_ans == 0:
    print("Draw.")
elif user_input == 1 and computer_ans == 0:
    print("Player Wins.")
elif user_input == 1 and computer_ans == 1:
    print("Draw.")
elif user_input == 1 and computer_ans == 2:
    print("Computer Wins.")
elif user_input == 2 and computer_ans == 0:
    print("Computer Wins")
elif user_input == 2 and computer_ans == 1:
    print("Player Wins.")
elif user_input == 2 and computer_ans == 2:
    print("Draw.")