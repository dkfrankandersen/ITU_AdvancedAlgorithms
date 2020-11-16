import math
import numpy as np
import itertools

# Kasteleyns Formular:
def kasteleyns(n:int,m:int):
    T = np.zeros((n,m))
    for j in range(1,n+1):
        for k in range(1,m+1):
            T[j-1,k-1] = (4 * (math.cos( (math.pi * j)/(n + 1))**2) + 4 * (math.cos( (math.pi * k)/(m + 1))**2))**(1/4)
    result = math.prod(math.prod(T))
    rounded = int(round(result))
    # print(f"kasteleyns: {n}x{m} = {rounded}")
    return rounded


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


def incExcPerfectMatching(n,m):
    nHalf = (n*m) // 2
    vertices,edges = gridToGraph(n,m)
    cumulatedSum = 0
    # For all vertices (starts 1)
    for i in range(1, len(vertices) + 1):
        # All combinations of vertices of lenght i 
        for combinations in itertools.combinations(vertices, i):            
            # Count a matches of a combination c in every edge
            count = 0
            for edge in edges:
                for c in combinations:
                    if c in edge:
                        count += 1
                        break # break if match in c found
            cumulatedSum += (-1)**len(combinations) * math.comb(count, nHalf)
    
    # print(f"Inclusion-Exclusion: {n}x{m} = {cumulatedSum}")
    return abs(cumulatedSum)


def compareTest(n):
    print(f"Comparing for 2..{n}")
    for i in range(2,n):
        for j in range(2,n):
            ka = kasteleyns(i,j)
            ie = incExcPerfectMatching(i,j)
            test = "OK" if ka==ie else "WRONG"
            print(f"{test} for {i}x{j} kasteleyns == incExcPerfectMatching {ka} == {ie}")


if __name__ == "__main__":
    compareTest(10)