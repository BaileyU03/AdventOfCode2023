class Step:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbours(self, garden):
        neighbours = []
        if self.x > 0 and garden[self.y][self.x - 1] == ".":
            neighbours.append(Step(self.x - 1, self.y))
        if self.x < len(garden[0]) - 1 and garden[self.y][self.x + 1] == ".":
            neighbours.append(Step(self.x + 1, self.y))
        if self.y > 0 and garden[self.y - 1][self.x] == ".":
            neighbours.append(Step(self.x, self.y - 1))
        if self.y < len(garden) - 1 and garden[self.y + 1][self.x] == ".":
            neighbours.append(Step(self.x, self.y + 1))
        return neighbours

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def main(steps):
    garden = []
    with open("./files/day21.txt", "r") as f:
        for r, line in enumerate(f):
            garden.append(list(line.replace("\n", "")))
            if "S" in line:
                start = Step(line.index("S"), r)
    step_history = [[0, start]]
    for i in range(steps):
        for step in [step[1] for step in step_history if step[0] == i]:
            for next_step in step.get_neighbours(garden):
                if next_step not in [x[1] for x in step_history]:
                    step_history.append([i + 1, next_step])
    return len([x for x in step_history if x[0] % 2 == 0])


print(main(64))
