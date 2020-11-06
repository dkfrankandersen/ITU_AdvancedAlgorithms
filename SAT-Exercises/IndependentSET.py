import igraph as ig
import numpy as np

def graphToCNF(g:ig.Graph, k:int):
    # ivs = g.independent_vertex_sets(min=k, max=k)
    # print(ivs)
    n = len(g.vs.indices)
    choices = [[0]*n]*k
    for i in range(k):
        for j in range(n):
            if i == j:
                choices[i][j] = 1
    print(np.matrix(choices))

g = ig.Graph(5)
g.add_edges([(0,1), (0,2),(0,3),(0,4), (1,0),(2,0),(3,0),(4,0)])

print(g)

graphToCNF(g, 4)