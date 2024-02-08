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
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with(location="London", name="Booby")
