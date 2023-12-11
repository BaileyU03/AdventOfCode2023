def main():
    image = []
    s = []
    with open("./files/day10.txt", "r") as f:
        for line in f:
            image.append(line.replace("\n", ""))
            if "S" in line:
                s = [len(image) - 1, line.index("S")]
    if image[s[0]][s[1] + 1] in ["J", "-", "7"]:
        current_pipe_pos = [s[0], s[1] + 1]
        last_direction = "R"
    elif image[s[0]][s[1] - 1] in ["L", "-", "F"]:
        current_pipe_pos = [s[0], s[1] - 1]
        last_direction = "L"
    elif image[s[0] + 1][s[1]] in ["J", "|", "L"]:
        current_pipe_pos = [s[0] + 1, s[1]]
        last_direction = "D"
    elif image[s[0] - 1][s[1]] in ["7", "|", "F"]:
        current_pipe_pos = [s[0] - 1, s[1]]
        last_direction = "U"
    counter = 1
    while current_pipe_pos != s:
        current_pipe_pos, last_direction = move(current_pipe_pos, last_direction, image)
        counter += 1
    return counter // 2


def move(pos, last_d, image):
    if image[pos[0]][pos[1]] == "|":
        new_d = last_d
        new_pos = [pos[0] + 1, pos[1]] if last_d == "D" else [pos[0] - 1, pos[1]]
    elif image[pos[0]][pos[1]] == "-":
        new_d = last_d
        new_pos = [pos[0], pos[1] + 1] if last_d == "R" else [pos[0], pos[1] - 1]
    elif image[pos[0]][pos[1]] == "7":
        new_d = "L" if last_d == "U" else "D"
        new_pos = [pos[0], pos[1] - 1] if last_d == "U" else [pos[0] + 1, pos[1]]
    elif image[pos[0]][pos[1]] == "F":
        new_d = "R" if last_d == "U" else "D"
        new_pos = [pos[0], pos[1] + 1] if last_d == "U" else [pos[0] + 1, pos[1]]
    elif image[pos[0]][pos[1]] == "J":
        new_d = "L" if last_d == "D" else "U"
        new_pos = [pos[0], pos[1] - 1] if last_d == "D" else [pos[0] - 1, pos[1]]
    elif image[pos[0]][pos[1]] == "L":
        new_d = "R" if last_d == "D" else "U"
        new_pos = [pos[0], pos[1] + 1] if last_d == "D" else [pos[0] - 1, pos[1]]
    return new_pos, new_d


print(main())
