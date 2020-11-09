import sys
import math
from collections import deque

class Vertex:
    def __init__(self, key:int, name:str, lat:float, lon:float):
        self.key = key
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.key} {self.name} ({self.lat} | {self.lon})"

    def haversineDistance(self,dst:'Vertex') -> float:
        pi180 = math.pi/180
        phi1 = self.lat * pi180
        phi2 = dst.lat * pi180
        dPhi = (dst.lat-self.lat) * pi180
        dLambda = (self.lon-dst.lon) * pi180

        R = 6371e3 # metres
        a = math.sin(dPhi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dLambda/2)**2 # Haversine
        c = 2 * math.atan2(math.sqrt(a), math.sqrt((1-a)))
        d = R*c
        return d

class Edge:
    def __init__(self, src:Vertex, dst:Vertex, weight:float):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        return f"{self.src.key} -> ({self.weight}) -> {self.dst.key}"

class Graph:
    def __init__(self):
        self.V = dict()
        self.E = 0

    def __len__(self):
        len(self.V.keys())

    def addVertex(self, v:Vertex) -> bool:
        if v not in self.V:
            self.V[v] = []
            return True
        else:
            False

    def addVertices(self, vertices:list):
        count = 0
        for v in vertices:
            if self.addVertex(v):
                count += 1
        return count

    def allVerticeKeys(self) -> list:
        return list(self.V.keys())

    def addEdge(self, edge:Edge):
        self.V[edge.src].append(edge)
        self.E += 1

    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(self, edge)

    def adjEdges(self, v:Vertex) -> list:
        return self.V[v]

    def allEdgeKeyPairs(self) -> int:
        pairs = []
        for k in self.V.keys():
            for edge in self.V[k]:
                pairs.append((k.key, edge.dst.key))
        return pairs

    def allEdges(self):
        pairs = []
        for k in self.V.keys():
            pairs.extend((self.V[k]))
        return pairs

    def edgeExists(self, src, dst):
        True if dst in self.V[src] else False

    def copy(self):
        g = Graph()
        g.V = self.V.copy()
        g.E = self.E
        return g

    def print(self):
        print(f"# of vertices: {len(self.V)}")
        print("Vertices: ")
        for v in self.V:
            print(v)
        print()
        print(f"# of edges: {self.E}")
        print(self.allEdgeKeyPairs())

    def primMST(self):
        start = list(self.V.keys())[0]
        mstEdges = []
        mstVertices = []
        mstVertices.append(start)

        q = deque()
        q.append(start)
        
        while q:
            this = q.pop()
            sortedEdges = sorted(self.V[this], key=lambda x: x.weight, reverse=False)
            for e in sortedEdges:
                if not this == e.dst and e.dst not in mstVertices:
                    mstVertices.append(e.dst)
                    mstEdges.append(e)
                    q.append(e.dst)
                    break

        totalWeight = sum([e.weight for e in mstEdges])
        return (mstVertices, mstEdges, totalWeight)
    
    def isConnected(self):
        visited = [0 for _ in range(len(self.V))]
        start = list(self.V.keys())[0]
        adj = list(self.V[start])
        while adj:
            e = adj.pop()
            visited[e.src.key] = 1
            if visited[e.dst.key] == 0:
                    adj.extend(self.V[e.dst])

        return sum(visited) == len(self.V)
            

    def findEulerPath(self):
        # Hierholzer’s algorithm can find Euler Path in linear time, O(E)
        
        # First, make sure that the input graph G is connected 
        if not self.isConnected():
            print("findEulerPath: graph not connected...")
            return None

        # select a starting vertex
        start = list(self.V)[0]

        # Check that graph contains exactly 0 or 2 odd degree vertices.
        countOdd = 0
        for k,v in self.V.items():
            if not len(v) % 2 == 0:
                countOdd += 1
                start = k
        if countOdd == 0 or not countOdd == 2:
            print("Error: should contain exactly 0 or 2 odd degree vertices.")
            return

        # Making a copy to delete from
        tmp = self.copy()
        tempPath = [start]
        finalPath = []
        
        while tempPath:
            v = tempPath[-1]
            if tmp.V[v]:
                e = tmp.V[v].pop()
                tempPath.append(e.dst)
            else:
                tempPath.remove(v)
                finalPath.append(v)
        return finalPath

    def findTSP(self):
        # Run MST on graph
        (vertices,edges,_) = g.primMST()

        # Build new graph from edges
        gMST = Graph()
        gMST.addVertices(vertices)
        for e in edges:
            gMST.addEdge(e)
            gMST.addEdge(Edge(e.dst, e.src, e.weight))
        
        eulerPath = gMST.findEulerPath()
        path = []
        for v in eulerPath:
            if v not in path:
                path.append(v)
        path.append(eulerPath[0])

        dist = 0
        last = path[-1]
        for v in path:
            dist += last.haversineDistance(v)
            last = v
        
        return path, dist

def readInput():
    cities = []
    for line in sys.stdin.readlines():
        name, coords = line.split(",")
        lat, lon = coords.split("/")
        cities.append((name, float(lat), float(lon)))
    return cities

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
    cities = hardcodedInput()

    g = Graph()
    # Add vertices:
    for i in range(len(cities)):
        v = Vertex(i, cities[i][0],cities[i][1],cities[i][2])
        g.addVertex(v)

    for v in g.allVerticeKeys():
        for w in g.allVerticeKeys():
            if not v == w:
                g.addEdge(Edge(v, w, v.haversineDistance(w)))

    (tspPath, dist) = g.findTSP()
    for v in tspPath:
        print(v)
    print()
    print(f"Dist: {dist}")
    
    # gMST.print()
