# Python3 program to print Vertex Cover
# of a given undirected graph 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices 

        # Default dictionary to store graph
        self.graph = defaultdict(list) 

    def ajustSize(self):
        self.V = len(self.graph)
        print(f"Ajustet size V {self.V}")

	# Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

	# The function to print vertex cover 
    def printVertexCover(self):
		
        # Initialize all vertices as not visited. 
        visited = [False] * (self.V)
		
        # Consider all edges one by one 
        for u in range(self.V):
            
            # An edge is only picked when 
            # both visited[u] and visited[v] 
            # are false
            if not visited[u]:
                
                # Go through all adjacents of u and 
                # pick the first not yet visited 
                # vertex (We are basically picking
                # an edge (u, v) from remaining edges. 
                for v in self.graph[u]:
                    if not visited[v]:
                        
                        # Add the vertices (u, v) to the
                        # result set. We make the vertex
                        # u and v visited so that all 
                        # edges from/to them would 
                        # be ignored 
                        visited[v] = True
                        visited[u] = True
                        break

        # Print the vertex cover 
        for j in range(self.V):
            if visited[j]:
                print(j, end = ' ')

        print()

# Driver code

# Create a graph given in 
# the above diagram 
g = Graph(7)

vertexMapTo = dict()
vertexMapFrom = dict()
edges = []
i = 0
for line in open("vc_graph.txt"):
    v,u = map(int, line.strip().split(" "))
    if v not in vertexMapFrom.keys():
        vertexMapFrom[v] = i
        vertexMapTo[i] = v
        i += 1
    if u not in vertexMapFrom.keys():
        vertexMapFrom[u] = i
        vertexMapTo[i] = u
        i += 1

print(vertexMapFrom)
print(vertexMapTo)

for line in open("vc_graph.txt"):
    v,u = map(int, line.strip().split(" "))
    g.addEdge(vertexMapFrom[v], vertexMapFrom[u])

g.ajustSize()
g.printVertexCover()

# This code is contributed by Prateek Gupta
