import sys
import math
import numpy as np
import itertools
from collections import defaultdict

class DirectedWeightedGraph():
    def __init__(self):
        self.edges = defaultdict(dict)

    def N(self):
        return len(self.edges)

    def V(self):
        return [k for k in self.edges.keys()]

    def addEdge(self, v:int, u:int, weight:float):
        self.edges[v][u] = weight

    def edgeTo(self, src):
        return self.edges[src]

    def print(self):
        print(self.edges)

class GeoCoord:
    def __init__(self, lat:float, lon:float):
        self.lat = lat
        self.lon = lon


def haversineDistance(src:GeoCoord, dst:GeoCoord) -> float:
    pi180 = math.pi/180
    phi1 = src.lat * pi180
    phi2 = dst.lat * pi180
    dPhi = (dst.lat-src.lat) * pi180
    dLambda = (src.lon-dst.lon) * pi180

    R = 6371e3 # metres
    a = math.sin(dPhi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dLambda/2)**2 # Haversine
    c = 2 * math.atan2(math.sqrt(a), math.sqrt((1-a)))
    d = R*c
    return d

def hardcodedInput():
    return [
            ("Copenhagen", 55.676, 12.566),
            ("Aarhus", 56.157, 10.211),
            ("Odense", 55.396, 10.388),
            ("Aalborg", 57.048, 9.919),
            ("Esbjerg", 55.47, 8.452),
            ("Horsens", 55.861, 9.85),
            ("Randers", 56.461, 10.036),
            ("Kolding", 55.49, 9.472),
            ("Vejle", 55.709, 9.536),
            ("Greve", 55.583, 12.3),
            ("Svendborg", 55.060337, 10.611613),
            ("Thisted", 56.956957, 8.686066),
            ("Holstebro", 56.358404, 8.613281),
            ("Aabenraa", 55.045335, 9.419403),
            ("Faaborg", 55.098016, 10.244751),
            ("Grenaa", 56.413142, 10.879211)
            ]

if __name__ == "__main__" :
    # cities = hardcodedInput()
    # N = len(cities)
    # g = DirectedWeightedGraph(N)

    # for i in range(len(cities)):
    #     for j in range(len(cities)):
    #         if not i==j:
    #             gc1 = GeoCoord(cities[i][1], cities[i][2])
    #             gc2 = GeoCoord(cities[j][1], cities[j][2])
    #             g.addEdge(i,j, haversineDistance(gc1, gc2))




    cities = [(1,2,10), (1,3,15), (1,4,20),
            (2,1,10), (2,3,35), (2,4,25),
            (3,1,15), (3,2,35), (3,4,30),
            (4,1,20), (4,2,25), (4,3,30)]

    g = DirectedWeightedGraph()
    #Add to graph
    for edge in cities:
        g.addEdge(edge[0], edge[1], edge[2])
    start = 1
    C = defaultdict(int)
    for i in range(2, g.N()):
        print(f"i: {i}")
        for S in itertools.combinations([v for v in g.V() if not v == start], i):
            print(f" S: {S}")
            vertices = tuple([start]) + tuple(S)
            if i==2:
                C[vertices] = g.edges[start][S[0]]
            else: 
                values = []
                for last in S:
                    values.append(C[vertices[:-1]] + g.edges[start][last])
                C[vertices] = min(values)

print(C)