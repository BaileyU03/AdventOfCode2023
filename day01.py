def main(part2):
    total = 0
    with open("./files/day01.txt", "r") as f:
        for line in f:
            newLine = line
            if part2:
                newLine = replace_word_numbers(line)
            numbers = []
            for char in newLine:
                if char.isdigit():
                    numbers.append(int(char))
            total += numbers[0] * 10 + numbers[-1]
    return total


def replace_word_numbers(line):
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    newLine = ""
    for i in range(len(line)):
        if line[i].isdigit():
            newLine += line[i]
            continue
        for wordLength in range(3, 6):
            if i < len(line) - wordLength:
                word = line[i:i+wordLength]
                if word in numbers.keys():
                    newLine += numbers.get(word)
                    break
    return newLine


print(main(False))
print(main(True))
