def main():
    total = 0
    with open("./files/day04.txt", "r") as f:
        for line in f:
            winning = list(map(int, line.split(":")[1].split(" | ")[0].split()))
            have = list(map(int, line.split(":")[1].split(" | ")[1].split()))
            points = 0
            for number in winning:
                if number in have:
                    points = points * 2 if points else 1
            total += points
    return total


print(main())
