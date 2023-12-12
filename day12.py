def main():
    field = []
    with open("./files/day12.txt", "r") as f:
        for line in f:
            field.append([line.split()[0], list(map(int, line.split()[1].split(",")))])
    total = 0
    for row in field:
        total += part1(row[0], row[1])
    return total


def part1(springs, data):
    if "?" not in springs:
        return is_valid(springs, data)
    s1 = s2 = springs[:]
    s1 = s1[:springs.index("?")] + "." + s1[springs.index("?") + 1:]
    s2 = s2[:springs.index("?")] + "#" + s2[springs.index("?") + 1:]
    return part1(s1, data) + part1(s2, data)


def is_valid(springs, data):
    damages = [x for x in springs.split(".") if len(x) > 0]
    if len(damages) != len(data):
        return 0
    for i, d in enumerate(damages):
        if len(d) != data[i]:
            return 0
    return 1


print(main())
