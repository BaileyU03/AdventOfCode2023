def part01():
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


def part02():
    grid = []
    with open("./files/day03.txt", "r") as f:
        for line in f:
            grid.append(list(line.replace("\n", "")))

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "*":
                adjacency = get_adjacency(grid, y, x)
                gears = [adjacency[x] for x in adjacency.keys() if adjacency[x] is not None]
                if len(gears) == 2:
                    total += gears[0] * gears[1]
    return total


def get_adjacency(grid, y, x):
    adjacency = {
        "u": None,
        "d": None,
        "l": None,
        "r": None,
        "ul": None,
        "ur": None,
        "dl": None,
        "dr": None
    }
    if y > 0:
        adjacency["u"] = get_part_number_one_point(grid, y - 1, x)
    if y < len(grid):
        adjacency["d"] = get_part_number_one_point(grid, y + 1, x)
    if x > 0:
        adjacency["l"] = get_part_number_one_point(grid, y, x - 1)
    if x < len(grid[y]):
        adjacency["r"] = get_part_number_one_point(grid, y, x + 1)
    if adjacency["u"] is None and y > 0:
        if x > 0:
            adjacency["ul"] = get_part_number_one_point(grid, y - 1, x - 1)
        if x < len(grid[y]):
            adjacency["ur"] = get_part_number_one_point(grid, y - 1, x + 1)
    if adjacency["d"] is None and y < len(grid):
        if x > 0:
            adjacency["dl"] = get_part_number_one_point(grid, y + 1, x - 1)
        if x < len(grid[y]):
            adjacency["dr"] = get_part_number_one_point(grid, y + 1, x + 1)
    return adjacency


def get_part_number_one_point(grid, y, x):
    if not grid[y][x].isdigit():
        return None
    start_pointer = end_pointer = x
    while end_pointer < len(grid[y]) - 1:
        if grid[y][end_pointer + 1].isdigit():
            end_pointer += 1
        else:
            break
    while start_pointer > 0:
        if grid[y][start_pointer - 1].isdigit():
            start_pointer -= 1
        else:
            break
    return get_part_number(grid[y], start_pointer, end_pointer)


print(part01())
print(part02())
