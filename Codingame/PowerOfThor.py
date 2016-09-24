import sys
import math

# Solve this puzzle by writing the shortest code.
# Whitespaces (spaces, new lines, tabs...) are counted in the total amount of chars.
# These comments should be burnt after reading!

# lx: the X position of the light of power
# ly: the Y position of the light of power
# tx: Thor's starting X position
# ty: Thor's starting Y position
lx, ly, tx, ty = [int(i) for i in input().split()]
# game loop
while 1:
    remaining_turns = int(input())  # The level of Thor's remaining energy, representing the number of moves he can still make.
    if lx > tx:
        if ly > ty:
            print("NE")
        else:
            print("SE")
    elif lx < tx
        if ly > ty:
            print("NW")
        else:
            print("SW")



