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
        node_data = []
        for i, node in enumerate(current_nodes):
            node_datum = {"first_z": None, "intermediate_z": [], "steps_of_loop": None}
            steps_copy = steps
            history = [node]
            current_node = node
            while current_node[-1] != "Z":
                step = steps_copy[0]
                current_node = adj_list[current_node][0] if step == "L" else adj_list[current_node][1]
                history.append(current_node)
                steps_copy = steps_copy[1:] + step
            node_datum["first_z"] = len(history) - 1
            loop_steps = 0
            while current_node != history[node_datum["first_z"]] or loop_steps == 0:
                step = steps_copy[0]
                current_node = adj_list[current_node][0] if step == "L" else adj_list[current_node][1]
                loop_steps += 1
                steps_copy = steps_copy[1:] + step
                if current_node[-1] == "Z":
                    node_datum["intermediate_z"].append(loop_steps)
            node_datum["steps_of_loop"] = loop_steps
            node_data.append(node_datum)
        return math.lcm(*[node["first_z"] for node in node_data])
    else:
        current_node = "AAA"
        while current_node != "ZZZ":
            step = steps[0]
            current_node = adj_list[current_node][0] if step == "L" else adj_list[current_node][1]
            total += 1
            steps = steps[1:] + step
    return total


# print(main(False))
print(main(True))
