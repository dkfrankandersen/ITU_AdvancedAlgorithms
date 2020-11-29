import sys
from typing import DefaultDict



def buildGraph():
    graph = DefaultDict(list)
    for line in sys.stdin.readlines():
        v,w =  map(int, line.strip().split(" "))
        graph[v].append(w)
        graph[w].append(v)

    return graph


def vertexCover(g):
    visited = [0]*len(g)
    for v in range(len(g)):
        if not visited[v]:
            for w in g[v]:
                if not visited[w]:
                    visited[v] = 1
                    visited[w] = 1
                    break

    return sum(visited), visited
            

g = buildGraph()
print(vertexCover(g))