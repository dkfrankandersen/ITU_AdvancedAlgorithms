import math
import itertools
from collections import defaultdict
import sys
from timeit import default_timer as timer
import numpy as np

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

def dpHC(vertices, edges):
    start = sorted(vertices)[0]
    adj = adjMatrix(vertices, edges)
    N = len(vertices)
    C = defaultdict(bool)
    excludingStart = list(filter(lambda x: x!= start, vertices))

    for i in range(1, N):
        perm = list(itertools.permutations(excludingStart, i))
        for S in perm:
            visited = tuple([start])+S
            for s in S:
                if i < 2 and adj[start][s]:
                        C[visited] = True
                else:
                    exLast = visited[:-1]
                    twoLast = visited[-2:]
                    if C.get(exLast) == True and adj[twoLast[0]][twoLast[1]] == 1:
                        C[visited] = True
    count = 0
    for k,v in C.items():
        # last = k[-1:]
        last = k[-1:]
        if len(k) == N and adj[last[0]][start]:
            # print(f"{k} -> {v}")
            count +=1
    return (int(count/2))

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
    tStart = timer()
    res = dpHC(vertices, edges)
    tEnd = timer()
    print(f"House Vertices: {len(vertices)} Time {(tEnd-tStart):.4f}s HC Found: {res} ")

    for i in range(1,20):
        vertices, edges = createCompleteGraph(i)
        tStart = timer()
        res = dpHC(vertices, edges)
        tEnd = timer()
        print(f"Vertices: {i} Time {(tEnd-tStart):.4f}s HC Found: {res} ")
    
    