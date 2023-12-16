def main():
    mirror_map = []
    with open("./files/day16.txt", "r") as f:
        for line in f:
            mirror_map.append(line.replace("\n", ""))
    light_map = [[[] for _ in line] for line in mirror_map]
    p1light_map = get_light_travel(mirror_map, light_map, 0, -1, ">")
    p1total = get_total(p1light_map)
    p2best = 0
    for i in range(len(light_map)):
        light_map = [[[] for _ in line] for line in mirror_map]
        left = get_total(get_light_travel(mirror_map, light_map, i, -1, ">"))
        light_map = [[[] for _ in line] for line in mirror_map]
        right = get_total(get_light_travel(mirror_map, light_map, i, len(light_map[0]), "<"))
        p2best = max(left, right) if max(left, right) > p2best else p2best
    for i in range(len(light_map[0])):
        light_map = [[[] for _ in line] for line in mirror_map]
        top = get_total(get_light_travel(mirror_map, light_map, -1, i, "v"))
        light_map = [[[] for _ in line] for line in mirror_map]
        bottom = get_total(get_light_travel(mirror_map, light_map, len(light_map), i, "^"))
        p2best = max(top, bottom) if max(top, bottom) > p2best else p2best
    return p1total, p2best


def get_light_travel(mirror_map, light_map, row, col, direction):
    flag = True
    while flag:
        if direction == ">":
            col += 1
        elif direction == "<":
            col -= 1
        elif direction == "^":
            row -= 1
        elif direction == "v":
            row += 1

        if row == -1 or row == len(mirror_map) or col == -1 or col == len(mirror_map[0]):
            return light_map
        if direction in light_map[row][col]:
            return light_map

        if mirror_map[row][col] == ".":
            light_map[row][col].append(direction)
        elif mirror_map[row][col] == "/":
            light_map[row][col].append(direction)
            if direction == ">":
                direction = "^"
            elif direction == "<":
                direction = "v"
            elif direction == "^":
                direction = ">"
            elif direction == "v":
                direction = "<"
        elif mirror_map[row][col] == "\\":
            light_map[row][col].append(direction)
            if direction == ">":
                direction = "v"
            elif direction == "<":
                direction = "^"
            elif direction == "^":
                direction = "<"
            elif direction == "v":
                direction = ">"
        elif mirror_map[row][col] == "-":
            light_map[row][col].append(direction)
            if direction == "v" or direction == "^":
                return combine_light_maps(
                    get_light_travel(mirror_map, light_map, row, col, ">"),
                    get_light_travel(mirror_map, light_map, row, col, "<"))
        elif mirror_map[row][col] == "|":
            light_map[row][col].append(direction)
            if direction == "<" or direction == ">":
                return combine_light_maps(
                    get_light_travel(mirror_map, light_map, row, col, "^"),
                    get_light_travel(mirror_map, light_map, row, col, "v"))


def combine_light_maps(lm1, lm2):
    m = []
    for r in range(len(lm1)):
        row = []
        for c in range(len(lm1[0])):
            row.append(list(set(lm1[r][c] + lm2[r][c])))
        m.append(row)
    return m


def get_total(light_map):
    t = 0
    for r in light_map:
        for c in r:
            if c:
                t += 1
    return t


print(main())
