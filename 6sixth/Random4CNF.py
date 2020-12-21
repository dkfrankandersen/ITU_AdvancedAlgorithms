import random

'''
Fix n = 100. For a “reasonable” selection of C 2 N and different r 2 Q in the interval [1; 20], pick
C random 4-CNF formulas with n variables and rn clauses. (A random 4-CNF clause is obtained by
choosing 4 of n variables, and then randomly choosing for each variable x whether it appears as x or
x¯ in the clause. A random 4-CNF formula with m clauses is obtained as the conjunction of m random
4-CNF clauses.) Using MiniSAT, compute for each selected r how many of the C random instances
with rn clauses are satisfiable. It will make sense to specify a reasonable timeout value after which you
the execution of MiniSAT is aborted.
'''

def rand4CNF():
    n = 1000
    rnd = random
    for r in range(1,20):
        C = rnd.randint(500,1000)
        rnd4CNFS = []
        for _ in range(C):
            CNFFormulars = []
            for _ in range(r*n):
                clause = random.sample(range(1, n+1), 4)
                # print(clause)
                assignment = [rnd.randint(0,1) for _ in range(4)]
                # print(assignment)
                casted = []
                for k in range(len(clause)):
                    casted.append(clause[k] if assignment[k] == 1 else -clause[k])
                    CNFFormulars.append(casted)
        rnd4CNFS.append(CNFFormulars)
    print(len(rnd4CNFS))


if __name__ == "__main__":
    rand4CNF()