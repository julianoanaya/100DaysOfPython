# ################### Scope ####################

# enemies = 1


# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # local scope


# # def drink_potion():
# #     potion_strength = 2
# #     print(potion_strength)


# # drink_potion()

# # global scope
# player_health = 10

# def game()
#   def drink_potion():
#       potion_strength = 2
#       print(player_health)
#   drink_potion

# print(player_health)


# #THERE is no block scope
# game_level=3
# enemies=["skeleton","zombie","alien"]
# def create_enemy():
#   if game_level<5:
#     new_enemy=enemies[0]
#   print(new_enemy)

# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies+1


# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# #global constants
# PI=3.14159
# URL = "https://www.google.com"


import random

# from art import logo
EASY_LIVES = 10
HARD_LIVES = 5
# print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def random_number():
    rand_num = random.randint(1, 100)
    return rand_num


random_generated_number = random_number()
print(f"The answer is {random_generated_number}")


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print("You got it! the answer was {answer}")


def setting_difficulty():
    difficulty = input("Choose a difficulty: Type 'easy or 'hard: ")

    if difficulty == "easy":
        return EASY_LIVES
    else:
        return HARD_LIVES
