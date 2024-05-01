
# Prim's Algorithm in Python
INF = 9999999

# number of vertices in graph
N = 5

#creating graph by adjacency matrix method
G = [[0, 19, 5, 0, 0],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [0, 9, 1, 0, 1],
    [0, 2, 6, 1, 0]]

selected_node = [0, 0, 0, 0, 0]
no_edge = 0

selected_node[0] = True

print("--------------------------------------------------------")
print("Edge : Weight\n") # printing for edge and weight

cost = 0
while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n

    print(str(a) + "-" + str(b) + " : " + str(G[a][b]))
    cost = cost + G[a][b]
    selected_node[b] = True
    no_edge += 1

print("Cost of the path is : ",cost)