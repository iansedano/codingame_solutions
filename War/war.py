import sys
import math

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
    deck_p1.append(int(cardp_1))
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()[:-1]  # the m cards of player 2
    cardp_2 = convert_faces(cardp_2)
    deck_p2.append(int(cardp_2))

turn = 1
war_deck_p1 = []
war_deck_p2 = []


def battle():
    print(f"BATTLE!", file=sys.stderr)
    if deck_p1[0] > deck_p2[0]:
        war_deck_p1.append(deck_p1.pop(0))
        war_deck_p2.append(deck_p2.pop(0))
        return 1

    elif deck_p1[0] < deck_p2[0]:
        war_deck_p1.append(deck_p1.pop(0))
        war_deck_p2.append(deck_p2.pop(0))
        return 2

    elif deck_p1[0] == deck_p2[0]:
        try:
            war_deck_p1.append(deck_p1.pop(0))
            war_deck_p1.append(deck_p1.pop(0))
            war_deck_p1.append(deck_p1.pop(0))
            war_deck_p1.append(deck_p1.pop(0))
            war_deck_p2.append(deck_p2.pop(0))
            war_deck_p2.append(deck_p2.pop(0))
            war_deck_p2.append(deck_p2.pop(0))
            war_deck_p2.append(deck_p2.pop(0))
            return 3
        except:
            return "PAT"


winner = 0
previous_result = 1
while True:
    # Start of turn
    result = battle()
    # if in a War
    if previous_result == 3:
        if result == 1:
            for c in war_deck_p1:
                deck_p1.append(c)
                war_deck_p1 = []
            for c in war_deck_p2:
                deck_p1.append(c)
                war_deck_p2 = []
            if len(deck_p2) == 0:
                winner = "PAT"
                break
            turn += 1
            previous_result = 1
        elif result == 2:
            for c in war_deck_p1:
                deck_p2.append(c)
                war_deck_p1 = []
            for c in war_deck_p2:
                deck_p2.append(c)
                war_deck_p2 = []
            if len(deck_p1) == 0:
                winner = "PAT"
                break
            turn += 1
            previous_result = 2
        elif result == 3:
            previous_result = 3
    # Normal turn
    elif result == 1 or result ==2:
        # If player 1 wins
        if result == 1:
            for c in war_deck_p1:
                deck_p1.append(c)
                war_deck_p1 = []
            for c in war_deck_p2:
                deck_p1.append(c)
                war_deck_p2 = []
            if len(deck_p2) == 0:
                winner = 1
                break
            turn += 1
            previous_result = 1
        # If player 2 wins
        elif result == 2:
            for c in war_deck_p1:
                deck_p2.append(c)
                war_deck_p1 = []
            for c in war_deck_p2:
                deck_p2.append(c)
                war_deck_p2 = []
            if len(deck_p1) == 0:
                winner = 2
                break
            turn += 1
            previous_result = 2
        elif result == 3:
            previous_result = 3
    elif result == "PAT":
        winner = "PAT"
        break

if winner == "PAT":
    message = winner
else:
    message = f"{winner} {turn}"

print(message)
