import sys
import numpy as np

'''
FPT (Fixed parameter tractable) Vertex cover
'''

def pickEdge(G):
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i,j] == 1:
                return (i,j)
    return None

def checkCover(G,u,k):
    # delete vertex from graph
    G = np.delete(np.delete(G, u, 0), u, 1)
    # Recursive FPTVertexCover
    result, coverLst = FPTVertexCover(G, k-1)
    if result:
        for i in range(len(coverLst)):
            if coverLst[i] >= u:
                coverLst[i] += 1
        coverLst.append(u)
        return True, coverLst
    return False, []

def FPTVertexCover(G,k):
    # returns result (true/false) and cover lst
    edge = pickEdge(G)
    if k==0 and edge != None:
        return False,[]
    elif k==0 or edge == None:
        return True, []
    else:
        u,v = edge
        result, coverLst = checkCover(G,u,k)
        if result:
            return True, coverLst
        result, coverLst = checkCover(G,v,k)
        if result:
            return True, coverLst

        return False,[]

def testcase_input():
    print("- From Input -")
    lines = sys.stdin.readlines()
    n = len(lines)
    adjMatrix = np.zeros((n,n))
    for line in lines:
        u,v = map(int, line.split(" "))
        adjMatrix[u-1,v-1] = 1
        adjMatrix[v-1,u-1] = 1

    for k in range(1, n+1):
        result = FPTVertexCover(adjMatrix, k)
        print(f"k: {k}, {result}")

def testcase_complete(n=5):
    print("- Complete -")
    adjMatrix = np.ones((n,n))
    for i in range(n):
        adjMatrix[i,i] = 0
    for k in range(n):
        result = FPTVertexCover(adjMatrix, k+1)
        print(f"k: {k+1}, {result}")

def testcase_star(n=5):
    print("- Star -")
    adjMatrix = np.zeros((n,n))
    for i in range(1,n):
        adjMatrix[0,i] = 1
    k = 1
    result = FPTVertexCover(adjMatrix, k)
    print(f"k: {k}, {result}")

def testcase_square():
    print("- Square -")
    n=4
    adjMatrix = np.zeros((n,n))
    adjMatrix[0,1] = 1
    adjMatrix[1,0] = 1
    adjMatrix[1,2] = 1
    adjMatrix[2,1] = 1
    adjMatrix[2,3] = 1
    adjMatrix[2,3] = 1
    adjMatrix[3,0] = 1
    adjMatrix[0,3] = 1
    for k in range(2,5):
        result = FPTVertexCover(adjMatrix, k)
        print(f"k: {k}, {result}")

if __name__ == "__main__":
    testcase_complete()
    testcase_star()
    testcase_square()
    testcase_input()