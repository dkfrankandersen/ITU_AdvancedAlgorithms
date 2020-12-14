import sys
import random
import math

class ApproxKarpLubyDNFCount:

    def constructF(dnf:str):
        clauses = []
        clean = dnf.replace(" ", "").replace("(","").replace(")","")
        for c in clean.split("or"):
            clauses.append(sorted(list(c.split("and"))))
        return clauses
    
    def randomClauses(t_clauses:int, n_literals:int):
        '''
            Creates a clauses
        '''
        clauses = set()
        while len(clauses) < t_clauses:
            clauses.add(tuple([random.randint(0,2) for _ in range(n_literals)])) # 0: notX 1: X, 2: does not matter
        return clauses

    def getMinMaxLiterals(dnf:list):
        minL = sys.maxsize; maxL = 1
        for clause in dnf:
            lenC = len(clause)
            minL = min(minL, lenC)
            minL = max(maxL, lenC)
        return minL, maxL

print(ApproxKarpLubyDNFCount.randomClauses(1000,1000))