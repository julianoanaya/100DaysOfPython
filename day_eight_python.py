# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Hello")
    print("How are you?")
    print("How is the weather?")


greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    print(f"How is the weather {name}?")


greet_with_name("Angela")


# function with more an 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Angela", "London")


# function with keyword arguments
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")


greet_with(location="London", name="Booby")

# Write your code below this line 👇
import math


def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    rounded_cans = math.ceil(number_of_cans)
    print(f"You'll need {rounded_cans} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
