import math


def main(is_part2):
    adj_list = {}
    with open("./files/day08.txt", "r") as f:
        steps = f.readline().replace("\n", "")
        f.readline()
        for line in f:
            adj_list[line.split(" = ")[0]] = line.split(" = ")[1].replace("(", "").replace(")", "").replace("\n", "").split(", ")
    total = 0
    if is_part2:
        current_nodes = [node for node in adj_list.keys() if node[-1] == "A"]
        steps_to_zs = []
        for i, node in enumerate(current_nodes):
            steps_copy = steps
            current_node = node
            counter = 0
            while current_node[-1] != "Z":
                step = steps_copy[0]
                current_node = adj_list[current_node][0] if step == "L" else adj_list[current_node][1]
                counter += 1
                steps_copy = steps_copy[1:] + step
            steps_to_zs.append(counter)
        return math.lcm(*steps_to_zs)
    else:
        current_node = "AAA"
        while current_node != "ZZZ":
            step = steps[0]
            current_node = adj_list[current_node][0] if step == "L" else adj_list[current_node][1]
            total += 1
            steps = steps[1:] + step
    return total


print(main(False))
print(main(True))
