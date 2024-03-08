# fruits = [
#     "apple",
#     "banana",
#     "cherry",
#     "kiwi",
#     "mango",
# ]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# total_height = 0
# number_of_student = 0
# for height in student_heights:
#     total_height += height
# print(f"total height = {total_height}")

# for student in student_heights:
#     number_of_student += 1
# print(f"number of students = {number_of_student}")
# average = total_height / number_of_student
# print(f"average height = {round(average)}")


# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# # Write your code below this row 👇
# base_score = 0
# for scores in student_scores:
#     if base_score <= scores:
#         base_score = scores
# print(f"The highest score in the class is: {base_score}")

# # for loop w/ range
# for number in range(
#     1,
#     10,
# ):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# target = int(input())  # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇


# total = 0
# for number in range(2, target + 1, 2):
#     total += number
# print(total)


# # Write your code here 👇
# target = 1 - 0
# for number in range(1, 100 + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# Password Generator Project
import random

letters = [
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
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# letters
letter = len(letters) - 1
password = ""
for abc in range(1, nr_letters + 1):
    chose_letter = random.randint(0, letter)
    password = password + letters[int(chose_letter)]
print(password)


# symbols
symbol = len(symbols) - 1
symbols_password = ""
for symbol_ in range(1, nr_symbols + 1):
    chose_symbol = random.randint(0, symbol)
    symbols_password = symbols_password + symbols[int(chose_symbol)]
print(symbols_password)

# number
number = len(numbers) - 1
numbers_password = ""
for number_ in range(1, nr_numbers + 1):
    chose_number = random.randint(0, number)
    numbers_password = numbers_password + numbers[int(chose_number)]
print(numbers_password)

print(f"Your password is {password}{symbols_password}{numbers_password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# randomized_password = password + symbols_password + numbers_password
# list_randomized_passwords = list(randomized_password)
# new_password = ""
# print(list_randomized_passwords)
# random_password = len(list_randomized_passwords) - 1
# for password_ in range(1, random_password + 1):
#     chosen_password = random.list_randomized_passwords[random_password])
#     new_password = new_password + list_randomized_passwords[int(chose_symbol)]
# print(new_password)
