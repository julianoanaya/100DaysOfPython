import random

# import my_module


random_integer = random.randint(1, 10)
print(random_integer)
# print(my_module.pi)
random_float = random.random()
print(random_float)

# random_integer = random.randint(1, 10)
# print(random_integer)
# # print(my_module.pi)
# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
# print(len(names))
import random

nuber_of_people = len(names) - 1
random_int = random.randint(0, nuber_of_people)
person_chosen = names[random_int]
print(f"{person_chosen} is going to buy the meal today!")
