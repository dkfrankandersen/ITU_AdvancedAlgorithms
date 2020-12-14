

from typing import DefaultDict
from Collections import defaultdict

def graph():
    graph = defaultdict([])
    n = 10
    for u in range(n):
        for v in range(n):
            graph[u].append(v)
    

def treeComposition(g):
    
