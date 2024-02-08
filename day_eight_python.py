# # Review:
# # Create a function called greet().
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.


# def greet():
#     print("Hello")
#     print("How are you?")
#     print("How is the weather?")


# greet()


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#     print(f"How is the weather {name}?")


# greet_with_name("Angela")


# # function with more an 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")


# greet_with("Angela", "London")


# # function with keyword arguments
# # def greet_with(name, location):
# #     print(f"Hello {name}")
# #     print(f"What is it like in {location}?")


# greet_with(location="London", name="Booby")

# # Write your code below this line 👇
# import math


# def paint_calc(height, width, cover):
#     number_of_cans = (height * width) / cover
#     rounded_cans = math.ceil(number_of_cans)
#     print(f"You'll need {rounded_cans} cans of paint.")


# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.

# # 🚨 Don't change the code below 👇
# test_h = int(input())  # Height of wall (m)
# test_w = int(input())  # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# # Write your code below this line 👇


# def prime_checker(number):
#     is_prime = True
#     for i in range(2, 9):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")


# # Write your code above this line 👆

# # Do NOT change any of the code below👇
# n = int(input())  # Check this number
# prime_checker(number=n)


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, num_shifts):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + num_shifts
        # print(new_position)
        new_letter = alphabet[new_position]
        # print(new_letter)
        cipher_text += new_letter
        # print(cipher_text)
    print(cipher_text)


# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text, shift)
