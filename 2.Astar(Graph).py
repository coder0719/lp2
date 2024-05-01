def a_star_algo(start_node, stop_node):
    open_set = set([start_node])  # Initialize the open set with the start node
    closed_set = set()  # Initialize the closed set
    g = {start_node: 0}  # Store distance from starting node
    parents = {start_node: start_node}  # Parents contains an adjacency map of all nodes

    while len(open_set) > 0:
        # Find the node with the lowest f() value (g(n) + h(n))
        n = min(open_set, key=lambda x: g[x] + heuristic(x))

        # If the current node is the stop node or it doesn't have neighbors, exit the loop
        if n == stop_node or n not in Graph_nodes:
            break

        # Iterate over neighbors of the current node
        for m, weight in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                # Add the neighbor to the open set if it's not in either open or closed set
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    # Update g value and parent if a shorter path to neighbor is found
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        # If neighbor was in closed set, move it to open set
                        closed_set.remove(m)
                        open_set.add(m)

        # Remove the current node from open set and add it to closed set
        open_set.remove(n)
        closed_set.add(n)

    if n is None:  # If no path is found
        print('Path does not exist!')
        return None

    # If the stop node is reached, reconstruct the path from start to stop node
    if n == stop_node:
        path = []
        while parents[n] != n:
            path.append(n)
            n = parents[n]
        path.append(start_node)
        path.reverse()
        print('Path found:', path)
        return path

    print('Path does not exist!')
    return None


# Function to get neighbors of a node
def get_neighbors(v):
    return Graph_nodes.get(v, None)


# Heuristic function to estimate distance from a node to the goal
def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 1, 'D': 1, 'E': 7, 'G': 0}
    return H_dist.get(n, 0)


# Define the graph with nodes and their neighbors
Graph_nodes = {
    'A': [('B', 6), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 0)],
    'C': [('B', 1)],
    'D': [('G', 0), ("E", 6)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)],
}

# Call the A* algorithm with start and stop nodes
a_star_algo('A', 'D')




# This is how the graph looks
#      A ---6---> B ---1----> C
#      |           |          |
#      3           2          |
#      |           |          |
#      v           v          v
#      E <---6--- D <---1---- G