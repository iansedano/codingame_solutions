import sys

deck_p1 = [5, 8, 10, 9, 4, 6, 12, 6, 6, 9, 2, 7, 14, 5, 7, 9, 12, 4, 3, 11, 2, 13, 10, 12, 3, 8]
deck_p2 = [4, 11, 8, 10, 5, 7, 3, 14, 13, 10, 11, 6, 2, 13, 8, 9, 13, 3, 14, 11, 4, 7, 2, 12, 5, 14]

turn = 1
print(f"starting deck 1 {deck_p1}", file=sys.stderr)
print(f"starting deck 2 {deck_p2}", file=sys.stderr)
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
    print(f"turn {turn}", file=sys.stderr)
    result = battle()
    print(f"///// result {result}", file=sys.stderr)
    print(f"b deck 1 {deck_p1}", file=sys.stderr)
    print(f"b deck 2 {deck_p2}", file=sys.stderr)
    print(f"b w deck 1 {war_deck_p1}", file=sys.stderr)
    print(f"b w deck 2 {war_deck_p2}", file=sys.stderr)
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
    
    print(f"deck 1 {deck_p1}", file=sys.stderr)
    print(f"deck 2 {deck_p2}", file=sys.stderr)
    print(f"w deck 1 {war_deck_p1}", file=sys.stderr)
    print(f"w deck 2 {war_deck_p2}", file=sys.stderr)
    

print(f"deck 1 {deck_p1}", file=sys.stderr)
print(f"deck 2 {deck_p2}", file=sys.stderr)

if winner == "PAT":
    message = winner
else:
    message = f"{winner} {turn}"

print(message)
