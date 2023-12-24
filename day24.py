def main():
    total = 0
    hailstones = []
    with open("./files/day24.txt", "r") as f:
        for line in f:
            pos_vel = line.strip().split(" @ ")
            pos = list(map(int, pos_vel[0].split(", ")))
            vel = list(map(int, pos_vel[1].split(", ")))
            hailstones.append({"pos": pos, "vel": vel})
    for i, h0 in enumerate(hailstones[:-1]):
        h0point0 = (h0["pos"][0], h0["pos"][1])
        h0point1 = (h0["pos"][0] + h0["vel"][0], h0["pos"][1] + h0["vel"][1])
        a0 = - h0["vel"][1]
        b0 = h0["vel"][0]
        c0 = -(h0point0[0] * h0point1[1] - h0point1[0] * h0point0[1])
        for j, h1 in enumerate(hailstones[i + 1:]):
            h1point0 = (h1["pos"][0], h1["pos"][1])
            h1point1 = (h1["pos"][0] + h1["vel"][0], h1["pos"][1] + h1["vel"][1])
            a1 = - h1["vel"][1]
            b1 = h1["vel"][0]
            c1 = -(h1point0[0] * h1point1[1] - h1point1[0] * h1point0[1])

            if intersection([a0,b0,c0], [a1,b1,c1]):
                x, y = intersection([a0,b0,c0], [a1,b1,c1])
                if (200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000 and
                        sign(x - h0point0[0]) == sign(h0["vel"][0]) and sign(y - h0point0[1]) == sign(h0["vel"][1]) and
                        sign(x - h1point0[0]) == sign(h1["vel"][0]) and sign(y - h1point0[1]) == sign(h1["vel"][1])):
                    total += 1
    return total


def intersection(l1, l2):
    D = l1[0] * l2[1] - l1[1] * l2[0]
    Dx = l1[2] * l2[1] - l1[1] * l2[2]
    Dy = l1[0] * l2[2] - l1[2] * l2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0
    

print(main())

