"""
Homework 4
This script converts graph coloring problems into SAT (Satisfiability) problems using CNF (Conjunctive Normal Form).

- node2var: Computes a unique SAT variable index for a node-color pair based on the total number of colors.
    This mapping ensures each combination of node and color gets a unique variable in the SAT solver's scope.

- at_least_one_color: Generates a clause ensuring that node n is assigned at least one of the colors from 1 to k.
    This is achieved by creating a disjunctive clause (OR) that contains all possible colors a node can take.

- at_most_one_color: Generates clauses to ensure that node n does not receive more than one color.
    This involves creating pairwise combinations of negated variables, indicating that if one color is true, the others must be false.

- generate_node_clauses: Generates a combined set of clauses that ensure a node n receives exactly one color.
    This function uses the at_least_one_color and at_most_one_color functions to create a complete set of conditions
    for a single node's color assignment.

- generate_edge_clauses: Generates clauses to prevent two adjacent nodes specified by edge e from having the same color.
    Each clause for an edge and color combination uses negated variables to block both nodes from sharing that color.
"""


"""
Returns the index of the variable that corresponds to the fact that
"Node n gets color c" when there are k possible colors

Args:
    n (int): Node index.
    c (int): Color index.
    k (int): Total number of colors available.

Returns:
    int: The index of the SAT variable corresponding to the node n having color c.
"""
def node2var(n, c, k):
    return (n - 1) * k + c


""""
Returns *a clause* for the constraint:
"Node n gets at least one color from the set {1, 2, ..., k}"

Args:
    n (int): Node index.
    k (int): Total number of colors.

Returns:
    list: A clause containing all positive literals for node n's color possibilities.
 """
def at_least_one_color(n, k):
    clause = []
    for c in range(1, k + 1):
        clause.append(node2var(n, c, k))
    return clause


"""
Returns *a list of clauses* for the constraint:
"Node n gets at most one color from the set {1, 2, ..., k}"

Args:
    n (int): Node index.
    k (int): Total number of colors.

Returns:
    list of lists: A list of clauses, each containing a pair of negated variables for each color combination.
"""
def at_most_one_color(n, k):
    clauses = []
    for c1 in range(1, k):
        for c2 in range(c1 + 1, k + 1):
            clauses.append([-node2var(n, c1, k), -node2var(n, c2, k)])
    return clauses

"""
Returns *a list of clauses* for the constraint:
"Node n gets exactly one color from the set {1, 2, ..., k}"

Args:
    n (int): Node index.
    k (int): Total number of colors.

Returns:
    list of lists: A comprehensive list of clauses ensuring exact one color assignment for node n.
"""
def generate_node_clauses(n, k):
    clauses = []
    clauses.append(at_least_one_color(n, k))
    clauses.extend(at_most_one_color(n, k))
    return clauses

"""
Returns *a list of clauses* for the constraint:
"Nodes connected by an edge e cannot have the same color"
The edge e is represented by a tuple

Args:
    e (tuple): Tuple containing two integers representing nodes connected by an edge.
    k (int): Total number of colors.

Returns:
    list of lists: Clauses that ensure nodes m and n (from edge e) do not share any of the k colors.
"""
def generate_edge_clauses(e, k):
    m, n = e
    clauses = []
    for c in range(1, k + 1):
        clause = [-node2var(m, c, k), -node2var(n, c, k)]
        clauses.append(clause)
    return clauses

# The function below converts a graph coloring problem to SAT
# Return CNF as a list of clauses
# DO NOT MODIFY
def graph_coloring_to_sat(graph_fl, sat_fl, k):
    clauses = []
    with open(graph_fl) as graph_fp:
        node_count, edge_count = tuple(map(int, graph_fp.readline().split()))
        for n in range(1, node_count + 1):
            clauses += generate_node_clauses(n, k)
        for _ in range(edge_count):
            e = tuple(map(int, graph_fp.readline().split()))
            clauses += generate_edge_clauses(e, k)
    var_count = node_count * k
    clause_count = len(clauses)
    with open(sat_fl, "w") as sat_fp:
        sat_fp.write("p cnf %d %d\n" % (var_count, clause_count))
        for clause in clauses:
            sat_fp.write(" ".join(map(str, clause)) + " 0\n")
    return clauses, var_count


# Example function call
if __name__ == "__main__":
   k1 = 3
   graph_coloring_to_sat("graph1.txt", "graph1_3.cnf", k1)

   k2 = 4
   graph_coloring_to_sat("graph1.txt", "graph1_4.cnf", k2)
