import heapq


class Node:
    def __init__(self, position, parent=None, cost=0, heuristic=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def total_cost(self):
        return self.cost + self.heuristic


def calculate_heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def get_neighbors(grid, node):
    neighbors = []
    x, y = node.position

    # Define possible movements: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != '#':
            neighbors.append((new_x, new_y))

    return neighbors


def astar(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    start_node.heuristic = calculate_heuristic(start, goal)
    heapq.heappush(open_list, (start_node.total_cost(), id(start_node), start_node))

    while open_list:
        _, _, current_node = heapq.heappop(open_list)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse path to get from start to goal

        closed_set.add(current_node.position)

        for neighbor_pos in get_neighbors(grid, current_node):
            if neighbor_pos in closed_set:
                continue

            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.cost = current_node.cost + 1
            neighbor_node.heuristic = calculate_heuristic(neighbor_pos, goal)

            heapq.heappush(open_list, (neighbor_node.total_cost(), id(neighbor_node), neighbor_node))

    return None  # No path found


# Example usage
grid = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '#', '.', '#'],
    ['#', '.', '#', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#']
]

start = (1, 1)
goal = (5, 3)

path = astar(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")

# op
# Path found: [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)]
# grid = [    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
#             ['#', '+', '.', '.', '.', '.', '.', '.', '#'],
#             ['#', '.', '#', '#', '#', '.', '#', '.', '#'],
#             ['#', '.', '#', '.', '.', '.', '#', '.', '#'],
#             ['#', '.', '#', '#', '#', '#', '#', '.', '#'],
#             ['#', '.', '.', '.', '.', '.', '.', '+', '#'],
#             ['#', '#', '#', '#', '#', '#', '#', '#', '#']
# ]
# " + " matlab start and goal nodes

#Change goal node asper you wish eg, goal = (3, 3) or goal = (5, 7) or goal = (5, 3)