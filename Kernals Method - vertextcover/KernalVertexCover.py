import sys
from typing import DefaultDict

class Graph:
    def __init__(self) -> None:
        self.graph = DefaultDict(list)

    def addEdge(self, u,v):
        self.graph[u].append(v)

    def V(self):
        return  list(self.graph.keys())

    def edges(self, v):
        return self.graph[v]

    def remove(self, v):
        self.graph.pop(v)

def readInput():
    g = Graph()

    for line in sys.stdin.readlines():
        v,u = map(int, line.strip().split())
        g.addEdge(u,v)

    return g

def kernalVertecCover(g,k):
    print(len(g.V()))

    # Rule 1 remove isolated vertices:
    for v in g.V():
        if len(g.edges(v)) == 0 :
            g.remove(v)
    print(len(g.V()))
    # Rule 2 



g = readInput()

kernalVertecCover(g,42)