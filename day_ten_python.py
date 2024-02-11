# Function with outputs


def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("angela", "YU")
print(formatted_string)

# Function with more outputs
# Function with outputs


def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


formatted_string = format_name(
    input("What is your first name?"), input("What is your last name?")
)
print(formatted_string)


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]


# 🚨 Do NOT change any of the co 
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)


from art import logo

print(logo)

# calculator


# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
num1 = int(input("What's the first number?: "))

num2 = int(input("What's the second number?: "))
for symbol in operations:
    print(f"{symbol}")
operation_symbol = input("Pick an operation from the line above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
