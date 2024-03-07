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
