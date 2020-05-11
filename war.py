import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

deck_p1 = []
deck_p2 = []


def convert_faces(card):
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    else:
        return card


n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()[:-1]  # the n cards of player 1
    cardp_1 = convert_faces(cardp_1)
    deck_p1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()[:-1]  # the m cards of player 2
    cardp_2 = convert_faces(cardp_2)
    deck_p2.append(cardp_2)

turn = 1

war_deck_p1 = []
war_deck_p2 = []


def battle():
    if int(deck_p1[0]) > int(deck_p2[0]):
        war_deck_p1.append(deck_p1.pop(0))
        war_deck_p2.append(deck_p2.pop(0))
        return 1

    elif int(deck_p1[0]) < int(deck_p2[0]):
        war_deck_p1.append(deck_p1.pop(0))
        war_deck_p2.append(deck_p2.pop(0))
        return 2

    elif int(deck_p1[0]) == int(deck_p2[0]):
        war_deck_p1.append(deck_p1.pop(0))
        war_deck_p1.append(deck_p1.pop(0))
        war_deck_p1.append(deck_p1.pop(0))
        war_deck_p1.append(deck_p1.pop(0))
        war_deck_p2.append(deck_p2.pop(0))
        war_deck_p2.append(deck_p2.pop(0))
        war_deck_p2.append(deck_p2.pop(0))
        war_deck_p2.append(deck_p2.pop(0))
        return 3

print(deck_p1, file=sys.stderr)
print(deck_p2, file=sys.stderr)

previous_result = 1
while True:
    if len(deck_p1) == 0 or len(deck_p2) == 0:
        break
    result = battle()
    if len(deck_p1) == 0 or len(deck_p2) == 0:
        break
    if previous_result == 3:
        if result == 1:
            for c in war_deck_p1:
                deck_p1.append(c)
            for c in war_deck_p2:
                deck_p1.append(c)
            previous_result = 1
        elif result == 2:
            for c in war_deck_p1:
                deck_p2.append(c)
            for c in war_deck_p2:
                deck_p2.append(c)
            previous_result = 2
        elif result == 3:
            previous_result = 3
    else:
        if result == 1:
            for c in war_deck_p1:
                deck_p1.append(c)
            for c in war_deck_p2:
                deck_p1.append(c)
            if len(deck_p1) == 0 or len(deck_p2) == 0:
                break
            turn += 1
            previous_result = 1
        elif result == 2:
            for c in war_deck_p1:
                deck_p2.append(c)
            for c in war_deck_p2:
                deck_p2.append(c)
            if len(deck_p1) == 0 or len(deck_p2) == 0:
                break
            turn += 1
            previous_result = 2
        elif result == 3:
            previous_result = 3
    
    print(deck_p1, file=sys.stderr)
    print(deck_p2, file=sys.stderr)
    print(turn, file=sys.stderr)

if deck_p1 > deck_p2:
    winner = 1
else:
    winner = 2

print(f"{winner} {turn}")
