def main(is_part2):
    total = 0
    with open("./files/day01.txt", "r") as f:
        for line in f:
            new_line = line
            if is_part2:
                new_line = replace_word_numbers(line)
            numbers = []
            for char in new_line:
                if char.isdigit():
                    numbers.append(int(char))
            total += numbers[0] * 10 + numbers[-1]
    return total


def replace_word_numbers(line):
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
               "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    new_line = ""
    for i in range(len(line)):
        if line[i].isdigit():
            new_line += line[i]
            continue
        for word_length in range(3, 6):
            if i < len(line) - word_length:
                word = line[i:i + word_length]
                if word in numbers.keys():
                    new_line += numbers.get(word)
                    break
    return new_line


print(main(False))
print(main(True))
