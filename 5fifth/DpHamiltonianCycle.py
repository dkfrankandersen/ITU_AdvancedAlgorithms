import math
import itertools
from collections import defaultdict
import sys

class WeightedGraph():
    def __init__(self):
        self.edges = defaultdict(lambda: defaultdict(lambda: float('inf')))

    def V(self):
        return list(self.edges.keys())

    def addEdge(self, v:int, u:int, cost:float):
        self.edges[v][u] = cost

    def getCost(self, v:int, u:int):
        return self.edges[v][u]

    def print(self):
        print(self.edges)

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

def dpHC(g: WeightedGraph):
    start = 0
    N = len(g.V())
    C = defaultdict(lambda: defaultdict(lambda: []))
    for i in range(2, N+1):
        for S in itertools.combinations([v for v in g.V()], i):
            for s in S:
                if s == start:
                    continue
                elif i == 2:
                    C[S][s] = ([start, s])
                else:
                    t = tuple(filter(lambda x: x!= s, S))
                    # C[S][s] = min([(C[t][k][0] + g.getCost(k,s), C[t][k][1]+[s]) for k in S if k != s and k !=start])
                    C[S][s] = min([(C[t][k]+[s]) for k in S])
                    

    tours = []
    t = tuple(g.V())
    for j in range(2,N+1):
        if len(C[t][j]+[start]) == N+1:
            tours.append(C[t][j]+[start])
    print(len(tours))
    print(tours)

if __name__ == "__main__":
    idToName, vertices, edges = graphFromInput()
    g = WeightedGraph()
    for u,v in edges:
        g.addEdge(u,v,0)
    dpHC(g)