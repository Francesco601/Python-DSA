# Python program to implement Traveling Salesman
# Problem using naive approach. Given a set of
# cities and distances between every pair of
# cities, the problem is to find the shortest
# possible route that visits every city exactly
# once and returns to the starting point.
#
# Note the difference between a Hamiltonian Cycle
# and TSP. The Hamiltonian problem is to find if
# there exists a tour that visits every city
# exactly once.Here we know that a Hamiltonian
# Cycle exists (because the graph is complete)
# and, in fact, many such tours exist.The problem
#is to find a minimum weight Hamiltonian Cycle.
# This problem is NP-hard and has no known polynomial
# time solution. The time complexity is O(n!) where
# n is the number of vertices in the graph. This is+
# the case because the algorithm uses the next_permutation
# function that generates all possible permutations of
# the set of vertices. Auxiliary space is O(n) since
# we use a vector to store all vertices.

from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

	# store all vertex apart from source vertex
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	# store minimum weight Hamiltonian Cycle
	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost)
		current_pathweight = 0

		# compute current path weight
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		# update minimum
		min_path = min(min_path, current_pathweight)
		
	return min_path


# Driver Code
if __name__ == "__main__":

	# matrix representation of graph
	graph = [[0, 10, 15, 20], [10, 0, 35, 25],
			[15, 35, 0, 30], [20, 25, 30, 0]]
	s = 0
	print(travellingSalesmanProblem(graph, s))
