from random import randint

n =  5 # variables
# r = range(1,15)
C = 2

clauses = []
for _ in range(C):
    for r in range(1,15):
        clause = []
        for _ in range(r*n):
            # Choose a random var, with random positive / negated value
            rndVar = [randint(0,n) if randint(0,1)==1 else -randint(0,n)]
            clause.append(rndVar)
        clauses.append(clause)

print(clauses)
