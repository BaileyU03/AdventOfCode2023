def main():
    image = []
    with open("./files/day14.txt", "r") as f:
        for line in f:
            image.append(list(line.replace("\n", "")))
    history = []
    for x in range(1000000000):
        for y in range(4):
            new_image = slide(image)
            if x == 0 and y == 0:
                part1 = get_total([x[:] for x in new_image])
            # Rotate clockwise
            image = list(zip(*new_image[::-1]))
        if image in history:
            cycle = history[history.index(image):]
            last = cycle[(1000000000 - x - 1) % len(cycle)]
            part2 = get_total(last)
            break
        history.append(image)
    return part1, part2


def get_total(image):
    image.reverse()
    multiplier = 1
    total = 0
    for line in image:
        total += multiplier * len([char for char in line if char == "O"])
        multiplier += 1
    return total


def slide(image):
    new_image = [["." if char == "O" else char for char in line] for line in image]
    for i, line in enumerate(image):
        for j, char in enumerate(line):
            if char == "O":
                current_line = i
                while new_image[current_line - 1][j] == "." and current_line - 1 >= 0:
                    current_line -= 1
                new_image[current_line][j] = "O"
    return new_image


print(main())
