def main():
    with open("./files/day15.txt", "r") as f:
        s = f.readline().replace("\n", "").split(",")
    p1_total = 0
    for word in s:
        current_value = box_number = 0
        for char in word:
            current_value += ord(char)
            current_value *= 17
            current_value %= 256
            if char.isalpha():
                box_number += ord(char)
                box_number *= 17
                box_number %= 256
        p1_total += current_value
        boxes = [[] for _ in range(256)]
        if "-" in word:
            label = word[:-1]
            if boxes[box_number] != [] and label in [lens[0] for lens in boxes[box_number]]:
                label_pos = [lens[0] for lens in boxes[box_number]].index(label)
                boxes[box_number].remove(boxes[box_number][label_pos])
        else:
            label = word[:-2]
            if boxes[box_number] == []:
                boxes[box_number].append([label, int(word[-1])])
            elif label in [lens[0] for lens in boxes[box_number]]:
                label_pos = [lens[0] for lens in boxes[box_number]].index(label)
                boxes[box_number][label_pos] = [label, int(word[-1])]
            else:
                boxes[box_number].append([label, int(word[-1])])
    focusing_powers = []
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focusing_powers.append((1 + i) * (j + 1) * lens[1])
    return p1_total, sum(focusing_powers)


print(main())
