# Python program for B-Tree insertion

class BTreeNode:
	def __init__(self, t, leaf):
		self.keys = [None] * (2 * t - 1) # An array of keys
		self.t = t # Minimum degree (defines the range for number of keys)
		self.C = [None] * (2 * t) # An array of child pointers
		self.n = 0 # Current number of keys
		self.leaf = leaf # Is true when node is leaf. Otherwise false

	# A utility function to insert a new key in the subtree rooted with
	# this node. The assumption is, the node must be non-full when this
	# function is called
	def insertNonFull(self, k):
		i = self.n - 1
		if self.leaf:
			while i >= 0 and self.keys[i] > k:
				self.keys[i + 1] = self.keys[i]
				i -= 1
			self.keys[i + 1] = k
			self.n += 1
		else:
			while i >= 0 and self.keys[i] > k:
				i -= 1
			if self.C[i + 1].n == 2 * self.t - 1:
				self.splitChild(i + 1, self.C[i + 1])
				if self.keys[i + 1] < k:
					i += 1
			self.C[i + 1].insertNonFull(k)

	# A utility function to split the child y of this node. i is index of y in
	# child array C[]. The Child y must be full when this function is called
	def splitChild(self, i, y):
		z = BTreeNode(y.t, y.leaf)
		z.n = self.t - 1
		for j in range(self.t - 1):
			z.keys[j] = y.keys[j + self.t]
		if not y.leaf:
			for j in range(self.t):
				z.C[j] = y.C[j + self.t]
		y.n = self.t - 1
		for j in range(self.n, i, -1):
			self.C[j + 1] = self.C[j]
		self.C[i + 1] = z
		for j in range(self.n - 1, i - 1, -1):
			self.keys[j + 1] = self.keys[j]
		self.keys[i] = y.keys[self.t - 1]
		self.n += 1

	# A function to traverse all nodes in a subtree rooted with this node
	def traverse(self):
		for i in range(self.n):
			if not self.leaf:
				self.C[i].traverse()
			print(self.keys[i], end=' ')
		if not self.leaf:
			self.C[i + 1].traverse()

			
	# A function to search a key in the subtree rooted with this node.
	def search(self, k):
		i = 0
		while i < self.n and k > self.keys[i]:
			i += 1
		if i < self.n and k == self.keys[i]:
			return self
		if self.leaf:
			return None
		return self.C[i].search(k)

# A BTree
class BTree:
	def __init__(self, t):
		self.root = None # Pointer to root node
		self.t = t # Minimum degree

	# function to traverse the tree
	def traverse(self):
		if self.root != None:
			self.root.traverse()

	# function to search a key in this tree
	def search(self, k):
		return None if self.root == None else self.root.search(k)

	# The main function that inserts a new key in this B-Tree
	def insert(self, k):
		if self.root == None:
			self.root = BTreeNode(self.t, True)
			self.root.keys[0] = k # Insert key
			self.root.n = 1
		else:
			if self.root.n == 2 * self.t - 1:
				s = BTreeNode(self.t, False)
				s.C[0] = self.root
				s.splitChild(0, self.root)
				i = 0
				if s.keys[0] < k:
					i += 1
				s.C[i].insertNonFull(k)
				self.root = s
			else:
				self.root.insertNonFull(k)
				
# Driver program to test above functions
if __name__ == '__main__':
	t = BTree(3) # A B-Tree with minimum degree 3
	t.insert(10)
	t.insert(20)
	t.insert(5)
	t.insert(6)
	t.insert(12)
	t.insert(30)
	t.insert(7)
	t.insert(17)

	print("Traversal of the constructed tree is ", end = ' ')
	t.traverse()
	print()

	k = 6
	if t.search(k) != None:
		print("Present")
	else:
		print("Not Present")

	k = 15
	if t.search(k) != None:
		print("Present")
	else:
		print("Not Present")
