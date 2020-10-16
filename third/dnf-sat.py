import sys
import random
import matplotlib.pyplot as plt

def convertDNF(dnfInput):
    print("----- Testing DNF Input -----")
    print(dnfInput)
    print()
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

def findSatConjAssignment(names, rndConj):
    result = dict(names)
    for i in range(0, len(rndConj)):
        result[rndConj[i]] = 0 if rndConj[i][0] == "!" else 1
    return result

def isMinimalIndex(satConj, conjunctions, index):
    if index == 0:
        return True
    else:
        count = index
        for i in range(0, index):
            fat = findSatConjAssignment(dict(), conjunctions[i])
            for k in fat.keys():
                if k not in satConj or satConj[k] != fat[k]:
                    count -= 1
                    break
        return count > 0

def findSatAssignment(satConj, satAssig, conjunctions):
    for k in satConj.keys():
        if satConj[k] == -1:
            satAssig[k] = random.randint(0,1)
        else:
            satAssig[k] = satConj[k]

    for i in range(0,len(conjunctions)):
        for j in range(0,len(conjunctions[i])):
            conjunctions[i][j] = satAssig[conjunctions[i][j]]

def satAssigment(dnf):
    names, conjunctions = dnf 
    rndIndex = random.randint(0, len(conjunctions)-1)
    rndConj = list(conjunctions[rndIndex])
    satConj = findSatConjAssignment(names, rndConj)
    satAssig = dict()
    isMinimal = isMinimalIndex(satConj, conjunctions, rndIndex)
    findSatAssignment(satConj, satAssig, conjunctions)
    
    print(f"Satisfying index / conjunctions: {rndIndex} / {rndConj}")
    print(f"Satisfying variables assignment: {satAssig}")
    print(f"Satisfying assignment: {conjunctions}")
    print(f"Is minimal index: {isMinimal}")
    print()


# Notations:
# not: !
# and: and  
# or: or

dnf = convertDNF("(x1 and !x2 and !x3) or (x2 and x3) or (x2 and x4) or x7")
satAssigment(dnf)

dnf = convertDNF("(x1 and x2) or x1 or x2")
satAssigment(dnf)

dnf = convertDNF("(x1 and x2) or (x2 and x3) or (x1 and x3)")
satAssigment(dnf)