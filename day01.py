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
    pointer = 0
    end = False
    while pointer < len(line) and not end:
        if not line[pointer].isalnum():
            end = True
            continue
        if line[pointer].isdigit():
            newLine += line[pointer]
            pointer += 1
            continue
        for number_length in range(5, 2, -1):
            if pointer < len(line) - (number_length - 1):
                word = line[pointer:pointer + number_length]
                if word in numbers.keys():
                    newLine += numbers.get(word)
                    continue
        pointer += 1
    return newLine


print(main(False))
print(main(True))
