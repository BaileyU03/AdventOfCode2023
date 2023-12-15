def main():
    with open("./files/day15.txt", "r") as f:
        s = f.readline().replace("\n", "").split(",")
    p1_total = 0
    boxes = [[] for _ in range(256)]
    for word in s:
        current_value = hash(word)
        p1_total += current_value
        if "-" in word:
            label = word[:-1]
            box_number = hash(label)
            if boxes[box_number] != [] and label in [lens[0] for lens in boxes[box_number]]:
                label_pos = [lens[0] for lens in boxes[box_number]].index(label)
                boxes[box_number].remove(boxes[box_number][label_pos])
        else:
            label = word[:-2]
            box_number = hash(label)
            if not boxes[box_number]:
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


def hash(word):
    v = 0
    for char in word:
        v += ord(char)
        v *= 17
        v %= 256
    return v


print(main())
