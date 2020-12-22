import sys
import numpy as np

def gridToGraph(n,m):
    # Created vertice grid of n x m size
    grid = [(i,j) for j in range(m) for i in range(n)]
    # Create mapping from each grid coords to vertice id (0..n)
    names = dict()
    for v in range(len(grid)):
        names[grid[v]] = v
    # Vertices as id's
    vertices = list(names.values())
    # Add grid edges as an undirected graph, and replace coords with vertices id's (0..n)
    edges = []
    for (r,c) in grid:
        v1 = names[(r,c)]
        if (r+1) < n:
            edges.append((v1, names[(r+1,c)])) # Down
        if (c+1) < m:
            edges.append((v1, names[(r,c+1)])) # Right

    return vertices, sorted(edges)

def adjMatrix(vertices, edges):
    # Create adjacency matrix
    N = len(vertices)
    adj = np.array([[0 for _ in range(0, N)] for _ in range(0, N)])
    for u,v in edges:
        adj[u][v] = 1
        adj[v][u] = 1
    return adj

class Node:
    def __init__(self, type):
        self.type = type
        self.bag = set()
        self.child = None
        self.type = None

def decomposeGridGraph(a):
    aT = a.T
    T = []
    for i in range(len(aT)):
        t = []
        if i > 0:
            t.extend([v for v in aT[i-1]])
        t.extend([v for v in aT[i]])
        T.append(t)
    return T

if __name__ == "__main__":
    vertices, edges = gridToGraph(2,2)
    adj = adjMatrix(vertices, edges)
    a =np.array([[11,12,13],[21,22,23],[31,32,33],[41,42,43]])
    print(a)
    print()
    print("Decomposed graph")
    print(decomposeGridGraph(a))