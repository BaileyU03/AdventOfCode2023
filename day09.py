def main(is_part2):
    sequences = []
    with open("./files/day09.txt", "r") as f:
        for line in f:
            sequences.append(list(map(int, line.split())))

    total = 0
    for s in sequences:
        s_tree = [s]
        while not all(x == 0 for x in s_tree[-1]):
            sub = [s_tree[-1][i+1] - s_tree[-1][i] for i in range(len(s_tree[-1]) - 1)]
            s_tree.append(sub)
        for layer in range(len(s_tree) - 2, -1, -1):
            s_tree[layer] = ([s_tree[layer][0] - s_tree[layer + 1][0]] + s_tree[layer] if is_part2
                             else s_tree[layer] + [s_tree[layer][-1] + s_tree[layer + 1][-1]])
        total += s_tree[0][0] if is_part2 else s_tree[0][-1]
    return total


print(main(False))
print(main(True))
