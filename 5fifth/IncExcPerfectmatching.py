import math
from time import sleep
import numpy as np
import itertools
import threading
from timeit import default_timer as timer

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


def incExcPerfectMatching(n,m,limit):
    nHalf = (n*m) // 2
    vertices,edges = gridToGraph(n,m)
    cumulatedSum = 0
    
    tStart = timer()
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
            if timer()-tStart > limit:
                return None
    
    # print(f"Inclusion-Exclusion: {n}x{m} = {cumulatedSum}")
    return abs(cumulatedSum)

def compare(i,j,limit):
    ka = kasteleyns(i,j)
    ie = incExcPerfectMatching(i,j,limit)
    
    test = "WRONG"
    res = 0
    if ie==None:
        test = "LIMIT"
        res = -1
    elif ka==ie:
        test = "OK" 
        res = 1


    print(f"{test} for {i}x{j} = {i*j} kasteleyns ({ka}) vs. incExcPerfectMatching ({ie})")
    return res

def compareLoop(n):
    timeLimit = 60
    print(f"Comparing for grid 2x2 ...{n}x{n}, time limit {timeLimit}s per grid")
    for i in range(2,n):
        for j in range(2,n):
            res = compare(i,j,timeLimit)
            if res == -1:
                print(f"Breaking at {i}x{j}, goto next i")
                break
            
            # t = threading.Thread(target=compare, args=(j,i))
            # print(f"start thread compare({i},{j})")
            # t.start()
    

if __name__ == "__main__":
    compareLoop(12)