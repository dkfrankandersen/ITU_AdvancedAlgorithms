import sys
import random
import math

def constructF(dnf:str):
    clauses = []
    clean = dnf.replace(" ", "").replace("(","").replace(")","")
    for c in clean.split("or"):
        clauses.append(sorted(list(c.split("and"))))
    return clauses

def getMinMaxLiterals(dnf):
    minL = sys.maxsize ; maxL = 1
    for clause in dnf:
        lenC = len(clause)
        print(lenC)
        if lenC < minL:
            minL = lenC
        if maxL < lenC:
            maxL = lenC
    return minL, maxL

def satifyClauseI(clause):
    result = dict()
    for literal in clause:
        result[literal] = 0 if literal[0] == "!" else 1
    return result

def constructU(variables, N:int, minL, maxL):
    clauses = []
    for i in range(0, N):
        r = random.randint(minL,maxL)
        literals = sorted(random.sample(variables, r))
        clauses.append(literals)
    return clauses

def constructSofU(F, U):
    size = len(F)
    print(size)
    subsetU = []
    for cF in F:
        print(f"Looking for cF {cF}")
        for cU in U:
            print(f"Looking in cU {cU}")
            if cF == cU:
                subsetU.append(cF)
                break
    return subsetU

def main():
    L = 10
    variables = [f"X{i}" for i in range(0,L)]+[f"!X{i}" for i in range(0,L)]
    N = 10
    dnf = constructF("(X1 and X2) or (X1 and !X2 and !X3) or (X4 and X6) or (X7 and X8)")
    print("Constructing from DNF Input")
    print(dnf)
    
    minL, maxL = getMinMaxLiterals(dnf)
    T = 200000
    print("Constructing the Universe (U)")
    U = constructU(variables, T, minL, maxL)
    print("Constructing the subset of U  (SU)")
    SU = constructSofU(dnf, U)
    print(SU)

main()
