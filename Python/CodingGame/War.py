# https://www.codingame.com/ide/puzzle/winamax-battle

import sys

# Define card values
values = {str(i): i for i in range(2, 11)}
values.update({'J': 11, 'Q': 12, 'K': 13, 'A': 14})

# Read number of cards and cards themselves for player 1
n = int(input())
deck1 = [input() for _ in range(n)]

# Read number of cards and cards themselves for player 2
m = int(input())
deck2 = [input() for _ in range(m)]

turns = 0
while deck1 and deck2:
    turns += 1
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    war_cards1 = [card1]
    war_cards2 = [card2]

    while card1 and card2 and values[card1[:-1]] == values[card2[:-1]]:
        # If it's a war situation and any player has less than 4 cards, it's a draw
        if len(deck1) < 4 or len(deck2) < 4:
            print("PAT")
            sys.exit()
        war_cards1 += [deck1.pop(0) for _ in range(3)]
        war_cards2 += [deck2.pop(0) for _ in range(3)]
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        war_cards1.append(card1)
        war_cards2.append(card2)

    # Compare latest card of war
    if values[card1[:-1]] > values[card2[:-1]]:
        deck1 += war_cards1 + war_cards2
    else:
        deck2 += war_cards1 + war_cards2

# Output winner
if deck1:
    print("1", turns)
else:
    print("2", turns)
