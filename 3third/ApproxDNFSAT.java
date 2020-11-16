package adv_algorithms;

import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ApproxDNFSAT {

    public static void main(String[] args) {
        ApproxDNFSAT dnfs = new ApproxDNFSAT();
        int noVariables = 10;
        int[][] clauses = dnfs.generateDNFSATs(1, 8);
        int[][] variablesAssigned = dnfs.assignVariables(clauses, noVariables);
        System.out.println(dnfs.bruteForceSolution(clauses, variablesAssigned, noVariables));
    }

    public int bruteForceSolution(int[][] clauses, int[][] variablesAssigned, int numberOfVariables) {
        HashSet<HashMap<Integer, Integer>> validSolutions = new HashSet<>();
        ArrayList<int[]> clauseList = new ArrayList<>();
        ArrayList<int[]> assignmentList = new ArrayList<>();
        List<List<Integer>> permutations = new ArrayList<>();
        generateAllPermutations(permutations, numberOfVariables);
        //Try to satisfy every clause for every assignment
        for (int clause = 0; clause < clauses.length; clause++) {
            nextAssignment:
            for (List<Integer> assignment : permutations) {
                HashMap<Integer, Integer> varToAssign = assignment.stream().collect(HashMap::new,
                        (map, streamValue) -> map.put(map.size(), streamValue),
                        (map, map2) -> {
                        });
                //Look at every clause var and see if correct
                for (int clauseIndex = 0; clauseIndex < clauses[0].length; clauseIndex++) {
                    if (varToAssign.get(variablesAssigned[clause][clauseIndex]) != clauses[clause][clauseIndex]) {
                        continue nextAssignment;
                    }
                }
                validSolutions.add(varToAssign);
                System.out.println("FOUND ASSIGNMENT FOR" + Arrays.toString(clauses[clause]));
                System.out.println("VARIABLES ASSIGNED FOR CLAUSE" + Arrays.toString(variablesAssigned[clause]));
                System.out.println("HERE WE SET VALUES FOR VARIABLES" + varToAssign);
            }
        }
        return validSolutions.size();
    }

    public void generateAllPermutations(List<List<Integer>> permutations, int numberOfVariables) {
        //Add first all zeroes
        //Then add all permutations
        ArrayList<Integer> withZero = new ArrayList<>();
        withZero.add(0);
        ArrayList<Integer> withOne = new ArrayList<>();
        withOne.add(1);
        permutationHelper(permutations, numberOfVariables, withOne);
        permutationHelper(permutations, numberOfVariables, withZero);
    }

    private void permutationHelper(List<List<Integer>> addWhenFinished, int numberOfVariables, ArrayList<Integer> currList) {
        if (currList.size() == numberOfVariables) {
            addWhenFinished.add(currList);
        }
        else {
            ArrayList<Integer> withZero = new ArrayList<>(currList);
            withZero.add(0);

            ArrayList<Integer> withOne = new ArrayList<>(currList);
            withOne.add(1);

            permutationHelper(addWhenFinished, numberOfVariables, withZero);
            permutationHelper(addWhenFinished, numberOfVariables, withOne);
        }

    }
    public int[][] assignVariables(int[][] res, int numberOfVariables) {
        Random r = new Random(2L);
        int[][] assignments = new int[res.length][res[0].length];
        for (int i = 0; i < res.length; i++) {
            assignments[i] = r.ints(0, numberOfVariables)
                                .distinct()
                                .limit(res[0].length)
                                .toArray();
        }
        return assignments;
    }

    public int[][] generateDNFSATs(int clauses, int variablesInClauses) {
        Random r = new Random(2L);
        HashSet<List<Integer>> uniqueClauses = new HashSet<>();
        for (int i = 0; i < clauses; i++) {
            uniqueClauses.add(r.ints(0, 2)
                    .limit(variablesInClauses)
                    .boxed()
                    .collect(Collectors.toList()));
        }
        int[][] uniques = new int[uniqueClauses.size()][variablesInClauses];
        int i = 0;
        for (List<Integer> clause : uniqueClauses) {
            uniques[i] = clause.stream().mapToInt(x -> x).toArray();
            i++;
        }
        return uniques;
    }

}