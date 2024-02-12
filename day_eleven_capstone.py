import random

play_game = input(
    "Do you want to play a game of Blackjack? type 'y' for yes and 'n' for no "
)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_hand = []

if play_game == "y":
    for stating_hand in range(1, 3):
        random_card = random.choice(cards)
        user_cards.append(random_card)
    for computer_starting_hand in range(1, 3):
        random_card = random.choice(cards)
        computer_hand.append(random_card)

first_cards = user_cards[0]
second_card = user_cards[1]
score = first_cards + second_card
# print(score)

computer_score = 0
first_comp_card = computer_hand[0]
second_comp_card = computer_hand[1]
computer_score = first_comp_card + second_comp_card

print(f"Your cards: {user_cards}, current score: {score}")
print(f"Computer's first hand: {computer_hand[0]}")

# for current_user_score in range(1, user_hand + 1):

hit = input("type 'y' to get another card, type 'n' to pass: ")
if hit == "y":
    random_card = random.choice(cards)
    user_cards.append(random_card)
    score = 0
    check_if_11_score = 0
    for user_single_card in user_cards:
        score += user_single_card
    print(f"Your cards: {user_cards}, current score: {score}")
    if score > 21:
        for check_if_user_has_11 in range(len(user_cards)):
            if user_cards[check_if_user_has_11] == 11:
                user_cards[check_if_user_has_11] = 1
                check_if_11_score += user_single_card
                if score > 21:
                    print("You lose")
                    print(f"Your final hand: {user_cards}, final score: {score}")
                    hit = "n"
                score = check_if_11_score

        print(f"Your hand is: {user_cards}, your score is {score}")
    elif score < 21:
        hit = input("type 'y' to get another card, type 'n' to pass: ")
    elif score == 21:
        print("You win")
        hit = "n"
    else:
        hit = "n"


print(user_cards)

# else:
#     print(f"Your score is: {score}")
# print(user_cards)
# print(score)

if computer_score < 16:
    random_card = random.choice(cards)
    computer_hand.append(random_card)
    computer_score = 0
    for computer_single_card in computer_hand:
        computer_score += computer_single_card
    if computer_score > 21:
        for check_if_comp_has_11 in range(len(computer_hand)):
            if computer_hand[check_if_comp_has_11] == 11:
                computer_hand[check_if_comp_has_11] = 1
