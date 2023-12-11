def main(is_part2):
    image = []
    with open("./files/day11.txt", "r") as f:
        for line in f:
            image.append(line.replace("\n", ""))
    galaxy_pos = get_galaxy_positions(image)
    empty_rows, empty_cols = expand(image)
    distances = get_distances(galaxy_pos, empty_rows, empty_cols, is_part2)
    return sum(distances)


def expand(image):
    empty_rows = []
    empty_cols = []
    for i, row in enumerate(image):
        if all(x == "." for x in row):
            empty_rows.append(i)
    for i, col in enumerate(list(map(list, zip(*image)))):
        if all(x == "." for x in col):
            empty_cols.append(i)
    return empty_rows, empty_cols


def get_galaxy_positions(image):
    galaxies = []
    for i, r in enumerate(image):
        for j, c in enumerate(r):
            if c == "#":
                galaxies.append([i, j])
    return galaxies


def get_distances(g, empty_rows, empty_cols, is_part2):
    distances = []
    for i in range(len(g) - 1):
        for j in range(i + 1, len(g)):
            total_distance = abs(g[i][0] - g[j][0]) + abs(g[i][1] - g[j][1])
            min_r, max_r = min(g[i][0] + 1, g[j][0]), max(g[i][0] + 1, g[j][0])
            for r in range(min_r, max_r):
                if r in empty_rows:
                    total_distance += 1000000 - 1 if is_part2 else 1
            min_c, max_c = min(g[i][1] + 1, g[j][1]), max(g[i][1] + 1, g[j][1])
            for c in range(min_c, max_c):
                if c in empty_cols:
                    total_distance += 1000000 - 1 if is_part2 else 1
            distances.append(total_distance)
    return distances


print(main(False))
print(main(True))
