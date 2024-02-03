# number = int(input())
# if number % 2 == 1:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")

# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi >= 18.5 and bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi >= 25 and bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi >= 30 and bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# elif bmi >= 35:
#     print(f"Your BMI is {bmi}, you are clincally obese.")

# # Which year do you want to check?
# year = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if year % 4 == 0 and year % 100 != 00 or year % 400 == 00:
#     print("Leap year")
# else:
#     print("Not leap year")

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? S, M, or L
# add_pepperoni = input()  # Do you want pepperoni? Y or N
# extra_cheese = input()  # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1
# else:
#     bill += 0
# print(f"Your final bill is: ${bill}.")

# print("The Love Calculator is calculating your score...")
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# name_together = name1 + name2
# small_name = name_together.lower()
# t = small_name.count("t")
# r = small_name.count("r")
# u = small_name.count("u")
# e = small_name.count("e")
# digit_1 = t + r + u + e
# l = small_name.count("l")
# o = small_name.count("o")
# v = small_name.count("v")
# e = small_name.count("e")

# digit_2 = l + o + v + e

# score = int(str(digit_1) + str(digit_2))

# # print(f"Your score is {score}")

# if score < 10:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score > 40 and score < 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")

print(
    '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
)
print("Welcome to treasure island! Let's start the game")
