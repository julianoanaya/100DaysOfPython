# # Step 1

# word_list = ["aardvark", "baboon", "camel"]

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# import random

# word_chosen = random.choice(word_list)
# print(word_chosen)

# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower()
# print(guess)
# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in word_chosen:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    display.append("_")
print(display)

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
