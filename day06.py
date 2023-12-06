import math


def main(is_part2):
    with open("./files/day06.txt", "r") as f:
        # Input file has been manipulated to be:
        # TIME0 TIME1 TIME2 TIME3
        # DIST0 DIST1 DIST2 DIST3
        if is_part2:
            times = [int(f.readline().replace(" ", ""))]
            dists = [int(f.readline().replace(" ", ""))]
        else:
            times = list(map(int, f.readline().split()))
            dists = list(map(int, f.readline().split()))
    total = 1
    for i in range(len(times)):
        mini, maxi = quad_equation(times[i], dists[i])
        total *= maxi - mini
    return total


def quad_equation(time, dist):
    plus = (time + pow(pow(time, 2) - 4 * dist, 0.5)) / 2
    minus = (time - pow(pow(time, 2) - 4 * dist, 0.5)) / 2
    mini = minus + 1 if minus == int(minus) else math.ceil(minus)
    maxi = plus if plus == int(plus) else math.ceil(plus)
    return mini, maxi


print(main(False))
print(main(True))
