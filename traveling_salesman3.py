# Python implementation of the Traveling Salesman Problem
# using Branch and Bound type algorithm. Branch and bound
# is a method for solving optimization problems by breaking
# them down into smaller sub-problems and using a bounding
# function to eliminate sub-problems that cannot contain
# the optimal solution. It consists of a systematic
# enumeration of candidate solutions by means of state
# space search where the set of candidates is thought
# of as forming a rooted tree with the full set at the
# root. The algorithm explores "branches" of this tree,
# which represent sub-sets of the solution set.
# Before enumerating the candidate solutions of a branch,
# the branch is checked against upper and lower estimated
# "bounds" on the optimal solution, and is discarded if
# ir cannot produce a better solution than the best one
# found so far by the algorithm. The time complexity is
# O(n^2) because of the cost of the row and column
# reduction functions.

V = 4
answer = []

# Function to find the minimum weight
# Hamiltonian Cycle
def tsp(graph, v, currPos, n, count, cost):

	# If last node is reached and it has
	# a link to the starting node i.e
	# the source then keep the minimum
	# value out of the total cost of
	# traversal and "ans"
	# Finally return to check for
	# more possible values
	if (count == n and graph[currPos][0]):
		answer.append(cost + graph[currPos][0])
		return

	# BACKTRACKING STEP
	# Loop to traverse the adjacency list
	# of currPos node and increasing the count
	# by 1 and cost by graph[currPos][i] value
	for i in range(n):
		if (v[i] == False and graph[currPos][i]):
			
			# Mark as visited
			v[i] = True
			tsp(graph, v, i, n, count + 1,
				cost + graph[currPos][i])
			
			# Mark ith node as unvisited
			v[i] = False

# Driver code

# n is the number of nodes i.e. V
if __name__ == '__main__':
	n = 4
	graph= [[ 0, 10, 15, 20 ],
			[ 10, 0, 35, 25 ],
			[ 15, 35, 0, 30 ],
			[ 20, 25, 30, 0 ]]

	# Boolean array to check if a node
	# has been visited or not
	v = [False for i in range(n)]
	
	# Mark 0th node as visited
	v[0] = True

	# Find the minimum weight Hamiltonian Cycle
	tsp(graph, v, 0, n, 1, 0)

	# ans is the minimum weight Hamiltonian Cycle
	print(min(answer))


