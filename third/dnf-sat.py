from random import randint
import sys
import random

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

def findSatAssignment(names, rndConj):
    result = dict()
    for k in names:
        result[k] = names[k]
    for i in range(0, len(rndConj)):
        result[rndConj[i]] = 0 if rndConj[i][0] == "!" else 1
    return result

def isMinimalIndex(satConj, conjunctions, index):
    # fasOrg = findSatAssignment(names, conjunctions[index])
    if index == 0:
        return True
    else:
        count = index
        print(count)
        for i in range(0, index):
            fat = findSatAssignment(dict(), conjunctions[i])
            for k in fat.keys():
                if k not in satConj or satConj[k] != fat[k]:
                    # print(f"failed {satConj} != {fat}")
                    count -= 1
                    break
        return count > 0

def satAssigment(dnf):
    names, conjunctions = dnf 
    rndIndex = random.randint(0, len(conjunctions)-1)
    rndConj = conjunctions[rndIndex]
    satConj = findSatAssignment(names, rndConj)
    satAssig = dict()

    isMinimal = isMinimalIndex(satConj, conjunctions, rndIndex)

    for k in satConj.keys():
        if satConj[k] == -1:
            satAssig[k] = random.randint(0,1)
        else:
            satAssig[k] = satConj[k]

    for i in range(0,len(conjunctions)):
        for j in range(0,len(conjunctions[i])):
            v = conjunctions[i][j]
            conjunctions[i][j] = satAssig[v]
    
    print(f"Satisfying index / conjunctions: {rndIndex} / {satConj}")
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

dnf = convertDNF("(x1 and x2) or (x2 and x3) or (x1 and x3")
satAssigment(dnf)