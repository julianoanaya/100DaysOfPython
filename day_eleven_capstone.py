import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
# random_card = random.choice(cards)
for stating_hand in range(1, 3):
    random_card = random.choice(cards)
    user_cards.append(random_card)
print(user_cards)

first_cards = user_cards[0]
second_card = user_cards[1]
score = first_cards + second_card
print(score)


# for current_user_score in range(1, user_hand + 1):

computer_hand = []
for computer_starting_hand in range(1, 3):
    random_card = random.choice(cards)
    computer_hand.append(random_card)
# print(computer_hand[0])
