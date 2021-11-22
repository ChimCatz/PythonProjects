#Step 1
import random
import hangman_art
from hangman_words import word_list

chosen_word = random.choice(word_list)
display = []
lives = 6

from hangman_art import logo
print(logo)
print("Let's play Hangman! I have a secret word. Guess it.")
# print(f'Pssst, the solution is {chosen_word}.')
for letter in chosen_word:
    display.append("_")
print(display)


end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    from hangman_art import stages
    print(stages[lives])