# A Python program to implement  topological sorting of a graph
# using in-degrees. Topological sorting of a DAG (directed
# acyclic graph) is a linear ordering of vertices such that
# for every directed edge uv, vertex u comes before v in the
# sorting. The canonical application of topological sorting
# is in scheduling a sequence of tasks based on their dependencies.
# In computer science, applications of this type arise in
# instruction scheduling, ordering of formula cell evaluation
# when recomputing formula values in spreadsheets, logic synthesis
# and determining the order of compilation tasks to peform
# in make files. Kahn's algorithm works by choosing vertices
# in the same order as the eventual topological graph.
# The algorithm has time complexity O(V +E) since the outer loop
# will be executed V number of times and the inner loop E number o
# times. The queue needs to store all vertices of the graph, so the
# space required is O(V).

from collections import defaultdict

# Class to represent a graph
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list) # dictionary containing adjacency List
		self.V = vertices # No. of vertices

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)


	# The function to do Topological Sort.
	def topologicalSort(self):
		
		# Create a vector to store indegrees of all
		# vertices. Initialize all indegrees as 0.
		in_degree = [0]*(self.V)
		
		# Traverse adjacency lists to fill indegrees of
		# vertices. This step takes O(V + E) time
		for i in self.graph:
			for j in self.graph[i]:
				in_degree[j] += 1

		# Create an queue and enqueue all vertices with
		# indegree 0
		queue = []
		for i in range(self.V):
			if in_degree[i] == 0:
				queue.append(i)

		# Initialize count of visited vertices
		cnt = 0

		# Create a vector to store result (A topological
		# ordering of the vertices)
		top_order = []

		# One by one dequeue vertices from queue and enqueue
		# adjacents if indegree of adjacent becomes 0
		while queue:

			# Extract front of queue (or perform dequeue)
			# and add it to topological order
			u = queue.pop(0)
			top_order.append(u)

			# Iterate through all neighbouring nodes
			# of dequeued node u and decrease their in-degree
			# by 1
			for i in self.graph[u]:
				in_degree[i] -= 1
				# If in-degree becomes zero, add it to queue
				if in_degree[i] == 0:
					queue.append(i)

			cnt += 1

		# Check if there was a cycle
		if cnt != self.V:
			print ("There exists a cycle in the graph")
		else :
			# Print topological order
			print (top_order)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print ("The following is a Topological Sort of the given graph")
g.topologicalSort()


