# # # Step 1

# # word_list = ["aardvark", "baboon", "camel"]

# import random

# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# # # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# # import random

# # word_chosen = random.choice(word_list)
# # print(word_chosen)

# # # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# # guess = input("Guess a letter: ").lower()
# # print(guess)
# # # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# # for letter in word_chosen:
# #     if letter == guess:
# #         print("Right")
# #     else:
# #         print("Wrong")

# # TODO-1: - Create an empty List called display.
# # For each letter in the chosen_word, add a "_" to 'display'.
# # So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# display = []
# guess = input("Guess a letter: ").lower()
# for letter in chosen_word:
#     display.append("_")
# print(display)

# # TODO-2: - Loop through each position in the chosen_word;
# # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter

# # TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# # Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(display)


# Step 3

#

# Step 4

import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
