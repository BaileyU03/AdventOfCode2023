def main(is_part2):
    total = 0
    with open("./files/day01.txt", "r") as f:
        for line in f:
            if is_part2:
                numbers = replace_word_numbers(line)
            else:
                numbers = [int(char) for char in line if char.isdigit()]
            total += numbers[0] * 10 + numbers[-1]
    return total


def replace_word_numbers(line):
    numbers_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                    "six": 6, "seven": 7, "eight": 8, "nine": 9}
    numbers = []
    for i in range(len(line)):
        if line[i].isdigit():
            numbers.append(int(line[i]))
            continue
        for word_length in range(3, 6):
            if i < len(line) - word_length:
                word = line[i:i + word_length]
                if word in numbers_dict.keys():
                    numbers.append(numbers_dict.get(word))
                    break
    return numbers


print(main(False))
print(main(True))
