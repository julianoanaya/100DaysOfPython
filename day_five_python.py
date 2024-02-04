fruits = [
    "apple",
    "banana",
    "cherry",
    "kiwi",
    "mango",
]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
number_of_student = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

for student in student_heights:
    number_of_student += 1
print(f"number of students = {number_of_student}")
average = total_height / number_of_student
print(f"average height = {round(average)}")


# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
base_score = 0
for scores in student_scores:
    if base_score <= scores:
        base_score = scores
print(f"The highest score in the class is: {base_score}")
