'''Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected
graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
structure'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, v):
        visited = set()
        self.dfs_util(v, visited)

    def bfs(self, v):
        visited = set()
        queue = [v]
        visited.add(v)

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Example usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)
g.add_edge(5, 8)
g.add_edge(5, 9)


#OR
# g = {
#   0: [1, 2],
#   1: [0, 2, 3, 4],
#   2: [0, 1, 4, 5],
#   3: [1, 4],
#   4: [1, 2, 3, 5],
#   5: [2, 4]
# }



print("Depth First Search (DFS):")
g.dfs(1)  # Start DFS from vertex 2

print("\nBreadth First Search (BFS):")
g.bfs(1)  # Start BFS from vertex 2




#############################################################################################################

#from collections import defaultdict
#used for
#from collections import defaultdict

# # Create a defaultdict with default value as an empty list
# my_dict = defaultdict(list)     //line 10
#
# # Since 'key' doesn't exist, it creates 'key' with an empty list as its value
# my_dict['key'].append('value')     //line 13 and 14
#
# print(my_dict)  # Output: defaultdict(<class 'list'>, {'key': ['value']})


#tree used in questions looks like :
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
#        / \
#       8   9
