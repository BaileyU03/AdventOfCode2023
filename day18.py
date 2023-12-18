def main():
    moves = []
    with open("./files/day18.txt", "r") as f:
        for line in f:
            moves.append([line.split()[0], int(line.split()[1])])
    positions = get_corners(moves)
    xs = [pos[0] for pos in positions]
    ys = [pos[1] for pos in positions]
    grid = fill_edges(positions, xs, ys)
    filled_grid = fill_centre(grid)
    flat = [x for r in filled_grid for x in r]
    return len([x for x in flat if x == "#"])


def get_corners(moves):
    positions = [[0, 0]]
    for move in moves:
        if move[0] == "U":
            pos = positions[-1][:]
            pos[1] -= move[1]
            positions.append(pos)
        elif move[0] == "D":
            pos = positions[-1][:]
            pos[1] += move[1]
            positions.append(pos)
        elif move[0] == "L":
            pos = positions[-1][:]
            pos[0] -= move[1]
            positions.append(pos)
        elif move[0] == "R":
            pos = positions[-1][:]
            pos[0] += move[1]
            positions.append(pos)
    return positions


def fill_edges(positions, xs, ys):
    width = max(xs) - min(xs) + 1
    height = max(ys) - min(ys) + 1
    grid = [["." for _ in range(width)] for _ in range(height)]
    for p in positions:
        grid[p[1] - min(ys)][p[0] - min(xs)] = "#"
    last_pos = positions[0]
    for pos in positions[1:]:
        if last_pos[1] == pos[1]:
            for x in range(min(last_pos[0], pos[0]), max(last_pos[0], pos[0])):
                grid[pos[1] - min(ys)][x - min(xs)] = "#"
        else:
            for y in range(min(last_pos[1], pos[1]), max(last_pos[1], pos[1])):
                grid[y - min(ys)][pos[0] - min(xs)] = "#"
        last_pos = pos
    return grid


def fill_centre(grid):
    # Breadth-first search
    filled_grid = [x[:] for x in grid]
    visited = []
    queue = [[150, 200]]  # Hardcoded centre of crater lol
    while queue:
        current = queue[0]
        queue = queue[1:]
        visited.append(current)
        filled_grid[current[0]][current[1]] = "#"
        if (current[0] < len(grid) - 1 and grid[current[0] + 1][current[1]] == "."
                and [current[0] + 1, current[1]] not in visited + queue):
            queue.append([current[0] + 1, current[1]])
        if (current[0] > 0 and grid[current[0] - 1][current[1]] == "."
                and [current[0] - 1, current[1]] not in visited + queue):
            queue.append([current[0] - 1, current[1]])
        if (current[1] < len(grid[0]) - 1 and grid[current[0]][current[1] + 1] == "."
                and [current[0], current[1] + 1] not in visited + queue):
            queue.append([current[0], current[1] + 1])
        if (current[1] > 0 and grid[current[0]][current[1] - 1] == "."
                and [current[0],current[1] - 1] not in visited + queue):
            queue.append([current[0], current[1] - 1])
    return filled_grid


print(main())
