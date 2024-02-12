import random

# play_game = input(
#     "Do you want to play a game of Blackjack? type 'y' for yes and 'n' for no "
# )
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user_cards = []
# computer_hand = []

# if play_game == "y":
#     for stating_hand in range(1, 3):
#         random_card = random.choice(cards)
#         user_cards.append(random_card)
#     for computer_starting_hand in range(1, 3):
#         random_card = random.choice(cards)
#         computer_hand.append(random_card)
#     first_cards = user_cards[0]
#     second_card = user_cards[1]
#     score = first_cards + second_card
#     computer_score = 0
#     first_comp_card = computer_hand[0]
#     second_comp_card = computer_hand[1]
#     computer_score = first_comp_card + second_comp_card
#     print(f"Your cards: {user_cards}, current score: {score}")
#     if score == 21:
#         play_game = "n"
#         print("You win")
#     print(f"Computer's first hand: {computer_hand[0]}")
#     if computer_score == 21:
#         print("You lose")
#         play_game = "n"
#     hit = input("type 'y' to get another card, type 'n' to pass: ")
#     while hit == "y":
#         random_card = random.choice(cards)
#         user_cards.append(random_card)
#         score = 0
#         check_if_11_score = 0
#         for user_single_card in user_cards:
#             score += user_single_card
#         print(f"Your cards: {user_cards}, current score: {score}")
#         if score > 21:
#             for check_if_user_has_11 in range(len(user_cards)):
#                 if user_cards[check_if_user_has_11] == 11:
#                     user_cards[check_if_user_has_11] = 1
#                     check_if_11_score += user_single_card
#                     score = check_if_11_score

#                     if score > 21:
#                         print("You lose")
#                         print(f"Your final hand: {user_cards}, final score: {score}")
#                         hit = "n"

#             print(f"Your hand is: {user_cards}, your final score is {score}")
#             print("you lose")
#             hit = "n"
#         elif score < 21:
#             hit = input("type 'y' to get another card, type 'n' to pass: ")
#             play_game = "n"
#         elif score == 21:
#             print("You win")
#             hit = "n"
#             play_game = "n"
#         else:
#             hit = "n"
#             play_game = "n"
#     while computer_score < 16:
#         random_card = random.choice(cards)
#         computer_hand.append(random_card)
#         computer_score = 0
#         for computer_single_card in computer_hand:
#             computer_score += computer_single_card
#         if computer_score > 21:
#             for check_if_comp_has_11 in range(len(computer_hand)):
#                 if computer_hand[check_if_comp_has_11] == 11:
#                     computer_hand[check_if_comp_has_11] = 1


# print(user_cards)

# # else:
# #     print(f"Your score is: {score}")
# # print(user_cards)
# # print(score)


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."
    if user_score == calculate_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has blackjack. You lose"
    elif user_score == 0:
        return "User has blackjack. You win"
    elif user_score > computer_score:
        return "You win"
    elif user_score > 21:
        return "You lose"
    elif computer_score > 21:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first cards: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card. Type 'n' to pass")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(
            f"   Computer's final hand: {computer_cards}, final score: {computer_score}"
        )
        print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
