import random
from pysat.solvers import Minisat22
from timeit import default_timer as timer

'''
Fix n = 100. For a “reasonable” selection of C 2 N and different r 2 Q in the interval [1; 20], pick
C random 4-CNF formulas with n variables and rn clauses. (A random 4-CNF clause is obtained by
choosing 4 of n variables, and then randomly choosing for each variable x whether it appears as x or
x¯ in the clause. A random 4-CNF formula with m clauses is obtained as the conjunction of m random
4-CNF clauses.) Using MiniSAT, compute for each selected r how many of the C random instances
with rn clauses are satisfiable. It will make sense to specify a reasonable timeout value after which you
the execution of MiniSAT is aborted.
'''


def SATSolver(clauses):
    m = Minisat22()
    # m.conf_budget(1000)
    m.prop_budget(2000) # adding limit on solver
    for clause in clauses:
        m.add_clause(clause)
    return m.solve_limited()


def compute(rnd4CNFS, r):
    countSatisfiable = 0
    stimer = timer()
    for clauses in rnd4CNFS:
        if SATSolver(clauses):
            countSatisfiable += 1
    etimer = timer()
    ratio = countSatisfiable/len(rnd4CNFS)
    # print(f"Compute result for r {r} and n {n} ration {ratio} time {etimer-stimer}")
    print(f"{r} {ratio} {(etimer-stimer)/len(rnd4CNFS)}")


def rand4CNF():
    n = 1000
    rnd = random
    for r in range(1,15):
        C = rnd.randint(500,1000)
        rnd4CNFS = []
        for _ in range(C):
            CNFFormulars = []
            for _ in range(r*n):
                clause = random.sample(range(1, n+1), 4)
                assignment = [rnd.randint(0,1) for _ in range(4)]
                casted = []
                for k in range(len(clause)):
                    casted.append(clause[k] if assignment[k] == 1 else -clause[k])
                    CNFFormulars.append(casted)
            rnd4CNFS.append(CNFFormulars)
        compute(rnd4CNFS, r)
        
    print("Done")




if __name__ == "__main__":
    rand4CNF()
    
