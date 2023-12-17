class Node:
    def __init__(self, n, x, y):
        self.value = int(n)
        self.dist = -1
        self.prev_dir = ""
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
    graph = []
    queue = []
    with open("./files/day17.txt", "r") as f:
        for y, line in enumerate(f):
            node_line = []
            for x, n in enumerate(line):
                if n == "\n":
                    continue
                node = Node(n, x, y)
                node_line.append(node)
                queue.append(node)
            graph.append(node_line)
    graph[0][0].dist = 0
    graph[0][0].prev_dir = "e"

    while queue:
        u = min(*queue)
        print(u.x, u.y, u.dist, u.prev_dir)
        queue.remove(u)
        left_x = right_x = forward_x = u.x
        left_y = right_y = forward_y = u.y
        if "e" in u.prev_dir:
            left_y = u.y - 1
            right_y = u.y + 1
            forward_x = u.x + 1
            left = "n"
            right = "s"
        if "w" in u.prev_dir:
            left_y = u.y + 1
            right_y = u.y - 1
            forward_x = u.x - 1
            left = "s"
            right = "n"
        if "n" in u.prev_dir:
            left_x = u.x - 1
            right_x = u.x + 1
            forward_y = u.y - 1
            left = "w"
            right = "e"
        if "s" in u.prev_dir:
            left_x = u.x + 1
            right_x = u.x - 1
            forward_y = u.y + 1
            left = "e"
            right = "w"
        forward = u.prev_dir + u.prev_dir[0]

        if 0 <= left_x < len(graph[0]) and 0 <= left_y < len(graph):
            left_node = graph[left_y][left_x]
            if left_node in queue:
                temp = u.dist + left_node.value
                if left_node.dist == -1 or temp < left_node.dist or (temp == left_node.dist and len(u.prev_dir) > len(left_node.prev_dir)):
                    left_node.dist = temp
                    left_node.prev = u
                    left_node.prev_dir = left
        if 0 <= right_x < len(graph[0]) and 0 <= right_y < len(graph):
            right_node = graph[right_y][right_x]
            if right_node in queue:
                temp = u.dist + right_node.value
                if right_node.dist == -1 or temp < right_node.dist or (temp == right_node.dist and len(u.prev_dir) > len(right_node.prev_dir)):
                    right_node.dist = temp
                    right_node.prev = u
                    right_node.prev_dir = right
        if 0 <= forward_x < len(graph[0]) and 0 <= forward_y < len(graph) and len(forward) <= 3:
            forward_node = graph[forward_y][forward_x]
            if forward_node in queue:
                temp = u.dist + forward_node.value
                if forward_node.dist == -1 or temp < forward_node.dist or (temp == forward_node.dist and len(u.prev_dir) > len(forward_node.prev_dir)):
                    forward_node.dist = temp
                    forward_node.prev = u
                    forward_node.prev_dir = forward

        if u == graph[len(graph) - 1][len(graph[0]) - 1]:
            v = u
            while v:
                print(v.x, v.y)
                v = v.prev
            return u.dist


print(main())


