import sys
from typing import DefaultDict
import cplex
import random

def buildGraph():
    graph = DefaultDict(list)

    for i in range(0,200):
        graph[i]

    for v in graph:
        for w in graph:
            if v != w:
                if random.randint(0,10) > 1:
                    graph[v].append(w)

    return graph


def vertexCover(g):
    visited = [0]*len(g)
    for v in range(len(g)):
        if not visited[v]:
            for w in g[v]:
                if not visited[w]:
                    visited[v] = 1
                    visited[w] = 1
                    break

    return sum(visited), visited

def cplexLpSolver(g):
    prob = cplex.Cplex()
    prob.set_problem_name("Vertex Cover")
    prob.set_problem_type(cplex.Cplex.problem_type.LP)
    names = [str(v) for v in g.keys()]
    w_obj = [1]*len(g)
    low_bnd = [0]*len(g)
    upr_bnd = [1]*len(g)
    prob.variables.add(names=names, obj=w_obj, lb=low_bnd, ub=upr_bnd)
    all_int = [(var, prob.variables.type.integer) for var in names]
    prob.variables.set_types(all_int)
    constraints = []

    for v in g.keys():
        for e in g[v]:
            constraints.append([[str(v),str(e)],[1,1]])
    constraint_names = ["".join(x[0]) for x in constraints]
    rhs = [1] * len(constraints)
    constraint_senses = ["G"] * len(constraints)
    prob.linear_constraints.add(names=constraint_names,
                                lin_expr=constraints,
                                senses=constraint_senses,
                                rhs=rhs)
    print("Problem Type: %s" % prob.problem_type[prob.get_problem_type()])
    prob.solve()
    print("Solution result is: %s" % prob.solution.get_status_string())
    print(prob.solution.get_values())

g = buildGraph()
print("Result from 2-approximation")
print(vertexCover(g))
print()

print("Result from LP-based algorithm")
cplexLpSolver(g)