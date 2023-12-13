import os
import json

data = []
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

data = [d.strip().split() for d in data]
hands = {'high card': 0, 'one pair': 1, 'two pair': 2, 'three of a kind': 3, 'full house': 4, 'four of a kind': 5, 'five of a kind': 6}
cards = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}


def sort_poker_hand(hand, part2):
    card_counts = {}
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1

    if part2:
        cards['J'] = 0
        wild_card = max({card: count for card, count in card_counts.items() if card != 'J'}, key=card_counts.get, default=None)
        if wild_card:
            if (card_counts[wild_card] + card_counts.get('J', 0)) > 5:
                card_counts[wild_card] = 5
            else:
                card_counts[wild_card] += card_counts.get('J', 0)
        card_counts = {card: count for card, count in card_counts.items() if card != 'J' or card_counts[card] == 5 }

    holdings = list(card_counts.values())
    if 5 in holdings:
        return (hands['five of a kind'], cards[hand[0]], cards[hand[1]], cards[hand[2]], cards[hand[3]], cards[hand[4]])
    if 4 in holdings:
        return (hands['four of a kind'], cards[hand[0]], cards[hand[1]], cards[hand[2]], cards[hand[3]], cards[hand[4]])
    if 3 in holdings:
        if 2 in holdings:
            return (hands['full house'], cards[hand[0]], cards[hand[1]], cards[hand[2]], cards[hand[3]], cards[hand[4]])
        return (hands['three of a kind'], cards[hand[0]], cards[hand[1]], cards[hand[2]], cards[hand[3]], cards[hand[4]])
    if 2 in holdings:
        if holdings.count(2) == 2:
            return (hands['two pair'], cards[hand[0]], cards[hand[1]], cards[hand[2]], cards[hand[3]], cards[hand[4]])
        return (hands['one pair'], cards[hand[0]], cards[hand[1]], cards[hand[2]], cards[hand[3]], cards[hand[4]])
    return (hands['high card'], cards[hand[0]], cards[hand[1]], cards[hand[2]], cards[hand[3]], cards[hand[4]])


# part 1
res = 0
rank = sorted(data, key=lambda d: sort_poker_hand(d[0], False))
for i, (hand, bid) in enumerate(rank, start=1):
    res += (i * int(bid))

print(f"part 1: {res}")

# part 2
res = 0
rank = sorted(data, key=lambda d: sort_poker_hand(d[0], True))
for i, (hand, bid) in enumerate(rank, start=1):
    res += (i * int(bid))

print(f"part 2: {res}")
