# Python program to illustrate
# recursive approach to ternary search
# Time complexity is better than the
# better known binary search: O(log base 3 n)
# Space complexity also O(log base 3 n)

import math as mt

# Function to perform Ternary Search
def ternarySearch(left, right, key, array):

	if (right >= left):

		# Find the mid1 and mid2
		mid1 = left + (right - left) //3
		mid2 = right - (right - left) //3

		# Check if key is present at any mid
		if (array[mid1] == key):
			return mid1
		
		if (array[mid2] == key):
			return mid2
		
		# Since key is not present at mid,
		# check in which region it is present
		# then repeat the Search operation
		# in that region
		if (key < array[mid1]):

			# The key lies in between l and mid1
			return ternarySearch(left, mid1 - 1, key, array)
		
		elif (key > array[mid2]):

			# The key lies in between mid2 and r
			return ternarySearch(mid2 + 1, right, key, array)
		
		else:

			# The key lies in between mid1 and mid2
			return ternarySearch(mid1 + 1,
								mid2 - 1, key, array)
		
	# Key not found
	return -1

# Driver code
l, r, p = 0, 9, 5

# Get the array
# Sort the array if not sorted
array = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Starting index
l = 0

# end element index
r = 9

# Checking for 5

# Key to be searched in the array
key = 5

# Search the key using ternarySearch
p = ternarySearch(l, r, key, array)

# Print the result
print("Index of", key, "is", p)

# Checking for 50

# Key to be searched in the array
key = 50

# Search the key using ternarySearch
p = ternarySearch(l, r, key, array)

# Print the result
print("Index of", key, "is", p)


