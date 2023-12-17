class Node:
    def __init__(self, n, x, y, dir):
        self.value = int(n)
        self.dist = -1
        self.dir = dir
        self.x = x
        self.y = y
        self.prev = None

    def __lt__(self, other):
        if self.dist == -1 and other.dist != -1:
            return self.dist > other.dist
        if self.dist != -1 and other.dist == -1:
            return self.dist > other.dist
        return self.dist < other.dist


def main():
    queue = []
    height = width = 12
    with open("./files/day17.txt", "r") as f:
        for y, line in enumerate(f):
            for x, n in enumerate(line):
                if n == "\n":
                    continue
                for direction in ["n", "e", "s", "w"]:
                    for multiplier in range(1, 4):
                        node = Node(n, x, y, direction * multiplier)
                        if y == 0 and x == 0 and direction * multiplier == "e":
                            node.dist = 0
                        queue.append(node)
    final_nodes = [node for node in queue if node.x == width - 1 and node.y == height - 1]
    while queue:
        u = min(*queue)
        queue.remove(u)
        left_x = right_x = forward_x = u.x
        left_y = right_y = forward_y = u.y
        if "e" in u.dir:
            left_y = u.y - 1
            right_y = u.y + 1
            forward_x = u.x + 1
            left = "n"
            right = "s"
        if "w" in u.dir:
            left_y = u.y + 1
            right_y = u.y - 1
            forward_x = u.x - 1
            left = "s"
            right = "n"
        if "n" in u.dir:
            left_x = u.x - 1
            right_x = u.x + 1
            forward_y = u.y - 1
            left = "w"
            right = "e"
        if "s" in u.dir:
            left_x = u.x + 1
            right_x = u.x - 1
            forward_y = u.y + 1
            left = "e"
            right = "w"
        forward = u.dir + u.dir[0]

        if 0 <= left_x < width and 0 <= left_y < height:
            left_node = [node for node in queue if node.x == left_x and node.y == left_y and node.dir == left]
            if left_node:
                left_node = left_node[0]
                temp = u.dist + left_node.value
                if left_node.dist == -1 or temp < left_node.dist:
                    left_node.dist = temp
                    left_node.prev = u
        if 0 <= right_x < width and 0 <= right_y < height:
            right_node = [node for node in queue if node.x == right_x and node.y == right_y and node.dir == right]
            if right_node:
                right_node = right_node[0]
                temp = u.dist + right_node.value
                if right_node.dist == -1 or temp < right_node.dist:
                    right_node.dist = temp
                    right_node.prev = u
        if 0 <= forward_x < width and 0 <= forward_y < height:
            forward_node = [node for node in queue if node.x == forward_x and node.y == forward_y and node.dir == forward]
            if forward_node:
                forward_node = forward_node[0]
                temp = u.dist + forward_node.value
                if forward_node.dist == -1 or temp < forward_node.dist:
                    forward_node.dist = temp
                    forward_node.prev = u

        if u.x == width - 1 and u.y == height - 1 and len([node for node in queue if node.x == width - 1 and node.y == height - 1]) == 6:
            v = min(*final_nodes)
            return v.dist

print(main())


