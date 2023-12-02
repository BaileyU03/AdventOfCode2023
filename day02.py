import re


def part01():
    total = 0
    with open("./files/day02.txt", "r") as f:
        for line in f:
            words = re.split("; |: |, ", line[5:].replace("\n", ""))
            game_id = int(words[0])
            reds = [int(x.split(" ")[0]) for x in words[1:] if x.split(" ")[1] == "red"]
            greens = [int(x.split(" ")[0]) for x in words[1:] if x.split(" ")[1] == "green"]
            blues = [int(x.split(" ")[0]) for x in words[1:] if x.split(" ")[1] == "blue"]
            if all(r <= 12 for r in reds) and all(g <= 13 for g in greens) and all(b <= 14 for b in blues):
                total += game_id
    return total


def main():
    print(part01())


main()
