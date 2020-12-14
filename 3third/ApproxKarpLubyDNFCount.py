import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt

class ApproxKarpLubyDNFCount:

    def constructF(self, dnf:str):
        clauses = []
        clean = dnf.replace(" ", "").replace("(","").replace(")","")
        for c in clean.split("or"):
            clauses.append(sorted(list(c.split("and"))))
        return clauses
    
    def randomDiffClauses(self, t_clauses:int, n_literals:int):
        clauses = set()
        while len(clauses) < t_clauses:
            clauses.add(tuple([random.randint(0,2) for _ in range(n_literals)])) # 0: notX 1: X, 2: does not matter
        return list(clauses)

    def allSameClauses(self, t_clauses:int, n_literals:int):
        clauses = list()
        tup = [random.randint(0,2) for _ in range(n_literals)]
        for _ in range(t_clauses):
            clauses.append(tup) # 0: notX 1: X, 2: does not matter
        return clauses
    
    
    def allTrueClauses(self, t_clauses:int, n_literals:int):
        clauses = list()
        tup = [1 for _ in range(n_literals)]
        for _ in range(t_clauses):
            clauses.append(tup) # 0: notX 1: X, 2: does not matter
        return clauses

    def getMinMaxLiterals(self, dnf:list):
        minL = sys.maxsize; maxL = 1
        for clause in dnf:
            lenC = len(clause)
            minL = min(minL, lenC)
            minL = max(maxL, lenC)
        return minL, maxL

    
    def checkSatClause(self, clause, assignment):
        for i in clause:
            # Variable is a positive number but the assignment makes it false or its negated and assignment makes it true
            if (i < 2 and assignment[i] != i):
                return False
        return True

    def sampling(self, clauses, n, m):
        probabilities = np.zeros(len(clauses))
        total = 0
        for i in range(len(clauses)):
            w = 2**(n - len(clauses[i]))
            probabilities[i] = w
            total += w
        probabilities /= total
        # Sampling
        countGoodClauses = 0
        for _ in range(m):
            # Sample clause with given probabilities
            clauseI = np.random.choice(len(clauses), p = probabilities)

            # Sample an assignment (randomly assign variables that are not in the clause)
            assignment = [np.random.randint(2) for _ in range(n)]
            for i in clauses[clauseI]:
                if i < 2: 
                    assignment[i] = clauses[clauseI][i]

            # Check that all the clauses up to i are not satisfied by that assignment
            good = True
            for j in range(clauseI):
                if (self.checkSatClause(clauses[j], assignment)):
                    good = False
                    break

            countGoodClauses += int(good)

        return (countGoodClauses / m) * total

if __name__ == "__main__":
    akl = ApproxKarpLubyDNFCount()
    t = 30 # t clauses
    n = 10 # n variables
    # m samplings
    
    cases = range(1,1000+1)



    # test3 =  [akl.sampling(akl.randomClauses(t,n), n, m) for m in range(1,1001)]
    fig, axs = plt.subplots(3)
    # fig.suptitle('Approx Karp Luby DNF Count')


    test1 =  [akl.sampling(akl.randomDiffClauses(t,n), n, m) for m in cases]
    axs[0].plot(cases, test1, linewidth = 1.0, color = "blue")
    axs[0].set_title('randomDiffClauses')
    axs[0].set(xlabel='# of samples', ylabel='# approx sat assign')

    test2 =  [akl.sampling(akl.allSameClauses(t,n), n, m) for m in cases]
    axs[1].plot(cases, test2, linewidth = 1.0, color = "red")
    axs[1].set_title('allSameClauses')
    axs[1].set(xlabel='# of samples', ylabel='# approx sat assign')

    test3 =  [akl.sampling(akl.allTrueClauses(t,n), n, m) for m in cases]
    axs[2].plot(cases, test3, linewidth = 1.0, color = "green")
    axs[2].set_title('allTrueClauses')
    axs[2].set(xlabel='# of samples', ylabel='# approx sat assign')

    fig.tight_layout()
    plt.legend()
    
    plt.show()