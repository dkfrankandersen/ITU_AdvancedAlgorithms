import sys
import numpy as np
from numpy.lib.function_base import delete

def gridToGraph(n,m):
    # Created vertice grid of n x m size
    grid = [(i,j) for j in range(m) for i in range(n)]
    gridVer = np.zeros((n,m), dtype=int)
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
            gridVer[r+1,c] = names[(r+1,c)]
        if (c+1) < m:
            edges.append((v1, names[(r,c+1)])) # Right
            gridVer[r,c+1] = names[(r,c+1)]

    return vertices, sorted(edges), gridVer

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
        self.bag = []
        self.child = None

# def decomposeGridGraph(a):
#     aT = a.T
#     T = []
#     for i in range(len(aT)):
#         t = []
#         if i > 0: t.extend(aT[i-1])
#         t.extend(aT[i])
#         T.append(t)
#     return T

def decomposeGridGraph2(a, adj):
    aT = a.T
    root = Node("introduce")
    node = root
    
    for i in range(len(aT)):
        for j in range(len(aT[i])):
            w = aT[i,j]
            node.bag.append(w)
            for x in node.bag:
                if x!=w and adj[w,x] == 0:
                    childForget = Node("forget")
                    childForget.bag.extend([v for v in node.bag if v != x])
                    node.child = childForget
                    node = childForget
                    break
            adj[i,j]
            childIntro = Node("introduce")
            childIntro.bag.extend(node.bag)
            node.child = childIntro
            node = childIntro
    
    n = root
    i = 1
    while n != None:
        print(i, n.type, n.bag)
        n = n.child
        i+=1



if __name__ == "__main__":
    vertices, edges, gridVer = gridToGraph(4,3)
    print(gridVer)
    adj = adjMatrix(vertices, edges)
    # print(edges)
    # print(adj)
    # a =np.array([[11,12,13],[21,22,23],[31,32,33],[41,42,43]])
    
    # print(a)
    # print()
    # # print("Decomposed graph")
    # # print(decomposeGridGraph(a))
    # # print()
    decomposeGridGraph2(gridVer, adj.T)