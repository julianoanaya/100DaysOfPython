import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
# random_card = random.choice(cards)
for stating_hand in range(1, 3):
    random_card = random.choice(cards)
    user_cards.append(random_card)
print(user_cards)
