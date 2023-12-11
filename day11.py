def main():
    image = []
    with open("./files/day11.txt", "r") as f:
        for line in f:
            image.append(line.replace("\n", ""))
    expanded_image = expand(image)
    galaxy_pos = get_galaxy_positions(expanded_image)
    distances = get_distances(galaxy_pos)
    return sum(distances)


def expand(image):
    new = []
    for row in image:
        new.append(row)
        if all(x == "." for x in row):
            new.append(row)
    t_new = list(map(list, zip(*new)))
    new = []
    for col in t_new:
        new.append(col)
        if all(x == "." for x in col):
            new.append(col)
    return list(map(list, zip(*new)))


def get_galaxy_positions(image):
    galaxies = []
    for i, r in enumerate(image):
        for j, c in enumerate(r):
            if c == "#":
                galaxies.append([i, j])
    return galaxies


def get_distances(g):
    distances = []
    for i in range(len(g) - 1):
        for j in range(i + 1, len(g)):
            distances.append(abs(g[i][0] - g[j][0]) + abs(g[i][1] - g[j][1]))
    return distances


print(main())