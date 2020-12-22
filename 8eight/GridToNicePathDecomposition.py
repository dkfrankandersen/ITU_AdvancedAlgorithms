import sys

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


if __name__ == "__main__":
    V,E = gridToGraph(2,2)

    print(V)
    print(E)
    pass