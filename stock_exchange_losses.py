import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
vals = []
for i in input().split():
    v = int(i)
    vals.append(v)

biggest_loss = 0
current_loss = 0
current_val = 0
last_val = 0
for v in vals:
    current_val = v
    if last_val > current_val:


print(vals)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")
