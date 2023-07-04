#  Python code to delete  a node in AVL tree.                                           
# AN AVL tree (also known as a height binary                                             
# tree) is a tree in which each node possesses                                           
# one of the following properties:                                                       
# 1) a node is called left heavy if the longest                                          
# path in its left subtree is one longer than the                                        
# longest path of its right subtree                                                      
# 2) A node is called right heavy if the longest                                         
# path in the right subtree is one longer than                                           
# longest path in its left subtree.                                                      
# 3) A node is called balanced if the longest path in                                    
# both the left and right subtree are equal.                                             
#                                                                                         # An AVL tree is a height-balanced tree where the                                       
# difference between the heights of the left and right                                   
# subtrees of every node is either 1,0, or -1. The                                       
# difference between the heights of the subtrees is                                      
# maintained by a factor named the balance factor. We                                    
# can therefore define AVL as a balanced binary search                                   
# tree where the balance factor of every node in the tree                                
# is either -1, 0, or 1. The balance formular is simply;                                 
# height of left subtree - height of right subtree. Since                                
# an AVL tree is a height-balanced tree, it helps to control                             
# the height of the binary search tree and further helps                                 
# the tree to prevent skewing. When the binary tree gets                                 
# skewed, the running-time complexity becomes the                                        
# worst case scenario (i.e. O(n)) but in the case of                                     
# the AVL tree, the time complexity remains O(log n).An                                  
# AVL tree is always preferable to a binary search tree.                                 
# Rotation is alwatys required to restore the balance after                              
# an insertion or deletion from an AVL tree. There is no                                 
# space to discuss this here.                                                             

# Generic tree node class
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports insertion,
# deletion operations
class AVL_Tree(object):

	def insert(self, root, key):
		
		# Step 1 - Perform normal BST
		if not root:
			return TreeNode(key)
		elif key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		# Step 2 - Update the height of the
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and key < root.left.val:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and key > root.right.val:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and key > root.left.val:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and key < root.right.val:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	# Recursive function to delete a node with
	# given key from subtree with given root.
	# It returns root of the modified subtree.
	def delete(self, root, key):

		# Step 1 - Perform standard BST delete
		if not root:
			return root

		elif key < root.val:
			root.left = self.delete(root.left, key)

		elif key > root.val:
			root.right = self.delete(root.right, key)

		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp

			elif root.right is None:
				temp = root.left
				root = None
				return temp

			temp = self.getMinValueNode(root.right)
			root.val = temp.val
			root.right = self.delete(root.right,
									temp.val)

		# If the tree has only one node,
		# simply return it
		if root is None:
			return root

		# Step 2 - Update the height of the
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
							self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and self.getBalance(root.left) >= 0:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and self.getBalance(root.right) <= 0:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and self.getBalance(root.left) < 0:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and self.getBalance(root.right) > 0:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def leftRotate(self, z):

		y = z.right
		T2 = y.left

		# Perform rotation
		y.left = z
		z.right = T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def rightRotate(self, z):

		y = z.left
		T3 = y.right

		# Perform rotation
		y.right = z
		z.left = T3

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.height

	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)

	def getMinValueNode(self, root):
		if root is None or root.left is None:
			return root

		return self.getMinValueNode(root.left)

	def preOrder(self, root):

		if not root:
			return

		print("{0} ".format(root.val), end="")
		self.preOrder(root.left)
		self.preOrder(root.right)


myTree = AVL_Tree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
	root = myTree.insert(root, num)

# Preorder Traversal
print("Preorder Traversal of the constructed AVL tree is -")
myTree.preOrder(root)
print()

# Delete
key = 10
root = myTree.delete(root, key)

# Preorder Traversal
print("Preorder Traversal after deletion of 10  -")
myTree.preOrder(root)
print()


