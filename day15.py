def main():
    with open("./files/day15.txt", "r") as f:
        s = f.readline().replace("\n", "").split(",")
    total = 0
    for word in s:
        current_value = 0
        for char in word:
            current_value += ord(char)
            current_value *= 17
            current_value %= 256
        total += current_value
    return total

print(main())
