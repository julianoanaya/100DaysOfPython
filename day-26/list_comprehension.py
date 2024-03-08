numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

# Write your code 👆 above:
squared_numbers = [number**2 for number in numbers]

print(squared_numbers)

list_of_strings = input().split(",")
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:


# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
# print(list_of_strings)
result = [
    int(even_number) for even_number in list_of_strings if int(even_number) % 2 == 0
]

# Write your code 👆 above:
print(result)


with open("file1.txt") as data_1:
    content = data_1.readlines()

stripped_number = [int(number.strip()) for number in content]
# print(stripped_number)

with open("file2.txt") as data_2:
    data = data_2.readlines()

number_file_2 = [int(number_2.strip()) for number_2 in data]
# print(number_file_2)

result = [list for list in stripped_number if list in number_file_2]
# print(result)


# Write your code above 👆
print(result)

sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇
words = sentence.split()
dict = {letter: len(letter) for letter in words}
print(dict)

# print(result)
