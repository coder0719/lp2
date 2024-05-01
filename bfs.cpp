#include <iostream>
#include <list>
#include <queue>
#include <vector>

using namespace std;

class Graph {
    int V;
    list<int> *adj;

public:
    Graph(int V) {
        this->V = V;
        adj = new list<int>[V];
    }

    void addEdge(int v, int w) {
        // Adjust vertices to be 0-indexed
        v--;
        w--;

        if (v < 0 || v >= V || w < 0 || w >= V) {
            cout << "Error: Vertex index out of bounds." << endl;
            return;
        }
        adj[v].push_back(w);
        adj[w].push_back(v);
    }

    void BFS(int start) {
        // Adjust start vertex to be 0-indexed
        start--;

        vector<bool> visited(V, false);
        queue<int> q;
        q.push(start);
        visited[start] = true;

        cout << "BFS Traversal starting from vertex " << start + 1 << ": ";
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            cout << current + 1 << " ";

            for (list<int>::iterator it = adj[current].begin(); it != adj[current].end(); ++it) {
                int neighbor = *it;
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        cout << endl;
    }
};

int main() {
    int V, E;
    cout << "Enter the number of vertices and edges: ";
    cin >> V >> E;

    Graph g(V);

    cout << "Enter the edges (vertex1 vertex2):" << endl;
    for (int i = 0; i < E; ++i) {
        int v, w;
        cin >> v >> w;
        g.addEdge(v, w);
    }

    int startVertex;
    cout << "Enter the starting vertex for BFS: ";
    cin >> startVertex;

    g.BFS(startVertex);

    return 0;
}
