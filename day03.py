def main():
    grid = []
    with open("./files/day03.txt", "r") as f:
        for line in f:
            grid.append(line.replace("\n", ""))

    total = 0
    for y_pointer in range(len(grid)):
        x_pointer = 0
        while x_pointer < len(grid[y_pointer]):
            if grid[y_pointer][x_pointer].isdigit():
                start_pointer = x_pointer
                end_pointer = x_pointer
                while end_pointer < len(grid[y_pointer]) - 1:
                    if grid[y_pointer][end_pointer + 1].isdigit():
                        end_pointer += 1
                    else:
                        break
                if is_adjacent_to_symbol(grid, y_pointer, start_pointer, end_pointer):
                    total += get_part_number(grid[y_pointer], start_pointer, end_pointer)
                x_pointer += 1 + end_pointer - start_pointer
                continue
            x_pointer += 1
    return total


def is_adjacent_to_symbol(grid, y_pointer, start_pointer, end_pointer):
    if y_pointer > 0 and start_pointer > 0:
        if is_symbol(grid, start_pointer - 1, y_pointer - 1):
            return True
    if y_pointer > 0 and end_pointer < len(grid[y_pointer]) - 1:
        if is_symbol(grid, end_pointer + 1, y_pointer - 1):
            return True
    if y_pointer < len(grid) - 1 and start_pointer > 0:
        if is_symbol(grid, start_pointer - 1, y_pointer + 1):
            return True
    if y_pointer < len(grid) - 1 and end_pointer < len(grid[y_pointer]) - 1:
        if is_symbol(grid, end_pointer + 1, y_pointer + 1):
            return True
    if y_pointer > 0:
        for x in range(start_pointer, end_pointer + 1):
            if is_symbol(grid, x, y_pointer - 1):
                return True
    if y_pointer < len(grid) - 1:
        for x in range(start_pointer, end_pointer + 1):
            if is_symbol(grid, x, y_pointer + 1):
                return True
    if start_pointer > 0:
        if is_symbol(grid, start_pointer - 1, y_pointer):
            return True
    if end_pointer < len(grid[y_pointer]) - 1:
        if is_symbol(grid, end_pointer + 1, y_pointer):
            return True
    return False


def is_symbol(grid, x, y):
    char = grid[y][x]
    return not char.isdigit() and not char == "."


def get_part_number(line, start_pointer, end_pointer):
    power = 0
    total = 0
    while end_pointer >= start_pointer:
        total += int(line[end_pointer]) * 10 ** power
        end_pointer -= 1
        power += 1
    return total


print(main())
