def main():
    trail_map = []
    with open("./files/day23.txt", "r") as f:
        first = f.readline().strip()
        start_pos = {"y": 0, "x": first.index(".")}
        trail_map.append(list(first))
        for line in f:
            trail_map.append(list(line.replace("\n", "")))
    return part1(trail_map, start_pos)


def part1(trail_map, pos):
    while pos["y"] != len(trail_map) - 1:
        trail_map[pos["y"]][pos["x"]] = "O"
        neighbours = get_neighbours(trail_map, pos)
        if len(neighbours) == 0:
            return 0
        if len(neighbours) > 1:
            return max(*[part1(copy_trail_map(trail_map), n) for n in neighbours])
        n = neighbours[0]
        trail_map[n["y"]][n["x"]] = "O"
        pos = n
    return get_trail_length(trail_map)


def get_neighbours(trail_map, pos):
    neighbours = []
    if pos["y"] > 0 and trail_map[pos["y"] - 1][pos["x"]] in ".^":
        new = pos.copy()
        new["y"] -= 1
        neighbours.append(new)
    if pos["y"] < len(trail_map) - 1 and trail_map[pos["y"] + 1][pos["x"]] in ".v":
        new = pos.copy()
        new["y"] += 1
        neighbours.append(new)
    if pos["x"] > 0 and trail_map[pos["y"]][pos["x"] - 1] in ".<":
        new = pos.copy()
        new["x"] -= 1
        neighbours.append(new)
    if pos["x"] < len(trail_map[0]) - 1 and trail_map[pos["y"]][pos["x"] + 1] in ".>":
        new = pos.copy()
        new["x"] += 1
        neighbours.append(new)
    return neighbours


def get_trail_length(trail_map):
    return len([x for line in trail_map for x in line if x == "O"]) - 1


def copy_trail_map(trail_map):
    return [x[:] for x in trail_map]


print(main())
