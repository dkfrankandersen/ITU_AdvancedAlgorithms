from random import randint
import sys
import random

def convertDNF(dnfInput):
    names = dict()
    conjunctions = []
    clean = dnfInput.replace("(", "").replace(")", "")
    for con in clean.split("or"):
        lst = list(con.strip().split("and"))
        literals = []
        for lit in lst:
            literals.append(lit.strip())
            names[lit.strip()] = -1
        conjunctions.append(literals)
    return (names, conjunctions)

def findSatAssignment(combined, rndConj):
    for i in range(0, len(rndConj)):
        combined[rndConj[i]] = 0 if rndConj[i][0] == "!" else 1
    return combined

def isMinimalIndex(conjunctions, index, names, conj):
    if index == 0:
        return True
    else:
        for i in range(0, index):
            v = findSatAssignment(names, conjunctions[i])
            n = dict()
            for k in v:
                if v[k] != -1:
                    n[k] = v[k]
            print(n)

def satAssigment(dnf):
    names, conjunctions = dnf 
    rndIndex = random.randint(0, len(conjunctions)-1)
    rndConj = conjunctions[rndIndex]
    satAssigConj = findSatAssignment(names, rndConj)
    satAssig = dict()

    isMinimal = isMinimalIndex(conjunctions, rndIndex, names, rndConj)

    for k in satAssigConj.keys():
        if satAssigConj[k] == -1:
            satAssig[k] = random.randint(0,1)
        else:
            satAssig[k] = satAssigConj[k]

    for i in range(0,len(conjunctions)):
        for j in range(0,len(conjunctions[i])):
            v = conjunctions[i][j]
            conjunctions[i][j] = satAssig[v]
    
    print(f"Satisfying variables assignment: {satAssig}")
    print(f"Satisfying assignment: {conjunctions}")
    print(f"Is minimal index: {isMinimal}")

    return satAssig


# Notations:
# not: !
# and: and  
# or: or

dnf = convertDNF("(x1 and !x2 and !x3) or (x2 and x3) or (x2 and x4) or x7")
a = satAssigment(dnf)