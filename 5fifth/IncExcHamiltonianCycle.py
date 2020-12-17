import numpy as np
from itertools import combinations
from numpy.linalg import matrix_power
import sys
from timeit import default_timer as timer

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

def graphFromInput():
    edges = []
    nameToId = dict()
    idToName = dict()
    N = int(sys.stdin.readline())
    for line in sys.stdin.readlines():
        u,v = line.strip().split(" ")
        if u not in nameToId:
            nameToId[u] = len(nameToId)
        if v not in nameToId:
            nameToId[v] = len(nameToId)
        edges.append((nameToId[u],nameToId[v]))
        edges.append((nameToId[v],nameToId[u]))
    vertices = list(nameToId.values())
    for k,v in nameToId.items():
        idToName[v] = k

    if not N == len(vertices):
        print("Input error vertices size N wrong.")
        exit(0)

    return idToName, vertices, sorted(edges)

def adjMatrix(vertices, edges):
    # Create adjacency matrix
    N = len(vertices)
    adj = np.array([[0 for _ in range(0, N)] for _ in range(0, N)])
    for u,v in edges:
        adj[u][v] = 1
        adj[v][u] = 1
    return adj

def incExcHC(vertices, edges):
    adjMat = adjMatrix(vertices, edges)
    N = len(adjMat)
    totalSum = 0
    for i in range(2, N+1):
        neg = (-1)**(N-i)
        for S in combinations(range(N), i):
            subMatrix = np.array(adjMat[np.ix_(S,S)], dtype=object)
            totalSum += neg * matrix_power(subMatrix, N).trace()
    return int((totalSum/N)/2)

def createCompleteGraph(n):
    vertices = list(range(0,n))
    edges = []
    for i in range(n):
        for j in range(n):
            if i != j:
                edges.append((i,j))
    return vertices, sorted(edges)

if __name__ == "__main__":
    idToName, vertices, edges = graphFromInput()
    res = incExcHC(vertices, edges)
    print(f"Vertices: {len(vertices)} HC Found: {res} ")
    for i in range(2,20,2):
        vertices, edges = createCompleteGraph(i)
        tStart = timer()
        res = incExcHC(vertices, edges)
        tEnd = timer()
        print(f"Vertices: {i} Time {(tEnd-tStart):.4f}s HC Found: {res} ")