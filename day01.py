def part1():
    total = 0
    with open("./files/day01.txt", "r") as f:
        for line in f:
            numbers = []
            for char in line:
                if char.isdigit():
                    numbers.append(int(char))
            total += numbers[0] * 10 + numbers[-1]
    return total


def main():
    print(part1())


main()
