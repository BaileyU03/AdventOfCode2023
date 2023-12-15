def main():
    image = []
    with open("./files/day14.txt", "r") as f:
        for line in f:
            image.append(list(line.replace("\n", "")))
    new_image = [["." if char == "O" else char for char in line] for line in image]
    for i, line in enumerate(image):
        for j, char in enumerate(line):
            if char == "O":
                current_line = i
                while new_image[current_line - 1][j] == "." and current_line - 1 >= 0:
                    current_line -= 1
                new_image[current_line][j] = "X"
    new_image.reverse()
    multiplier = 1
    total = 0
    for line in new_image:
        total += multiplier * len([char for char in line if char == "X"])
        multiplier += 1
    return total


print(main())