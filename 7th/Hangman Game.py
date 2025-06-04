#imports
import random
from hangman_words import word_list
from hangman_art import logo,stages

#setting variables
game_over = False
correct_letters = []
lives = 6
print(logo)
chosen_word = random.choice(word_list)

#creating a placeholder for the chosen words to be replaces with "_"
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

#game logic
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    #setting up warning for player if chosen the same correct letter again
    if guess in correct_letters:
        print(f"You Already chose {guess}!, Try another")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    #Losing a life from choosing a letter that's not in the chosen word
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        #losing condition
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"IT WAS {chosen_word}! YOU LOSE")

    #winning condition
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    #printing the ascII art
    print(stages[lives])
