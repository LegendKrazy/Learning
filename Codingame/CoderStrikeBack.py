import sys
import math
podSpeed = 0
# Boost Counter, only 1 per match
BoostCount = 1
# game loop
while True:
    # next_cp_x: x position of the next check point
    # next_cp_y: y position of the next check point
    # next_cp_dist: distance to the next checkpoint
    # next_cp_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_cp_x, next_cp_y, next_cp_dist, next_cp_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # Speed Control: Slow down when closer to avoid overshooting
    if next_cp_angle > 90 or next_cp_angle < -90:
        podSpeed = 0
    else:
        if next_cp_dist > 8000 and BoostCount == 1:
            podSpeed = "BOOST"
            BoostCount = 0
        elif next_cp_dist <= 3500:
            podSpeed = 80
        elif next_cp_dist <= 3300:
            podSpeed = 70
        elif next_cp_dist <= 2550:
            podSpeed = 30
        elif next_cp_dist <= 1800:
            podSpeed = 0
        else:
            podSpeed = 100
    # Dashboard of Information!!! for testing purposes only
    print("BoostCount: " + str(BoostCount), file=sys.stderr)
    print("Speed: " + str(podSpeed), file=sys.stderr)
    print("Angle: " + str(next_cp_angle), file=sys.stderr)
    print("Distance: " + str(next_cp_dist), file=sys.stderr)
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_cp_x) + " " + str(next_cp_y) + " " + str(podSpeed))
