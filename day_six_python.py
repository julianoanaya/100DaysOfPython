print("Hello")
num_char = len("Hello")
print(num_char)


def my_function():
    print("Hello")
    print("Bye")


my_function()


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def move_and_jump_reset():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# move()
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_left()
# move_and_jump_reset()
# move_and_jump_reset()
# move_and_jump_reset()
# move_and_jump_reset()
# move()
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()


def move_and_jump_reset():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


jumps = 6
while at_goal() != True:
    move_and_jump_reset()


def jump():
    if wall_in_front():
        turn_left()
        move()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        move()
        while front_is_clear():
            move()
        turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
