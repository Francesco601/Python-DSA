# A naive recursive implementation
# of 0-1 Knapsack Problem. In the 0/1
# knapsack problem, we are given N items
# where each item has some weight and profit
# associated with it. The goal is to put the
# items into the bag in such a way that the sum
# of profits associated with them is the maximum
# possible. There are many solutions and many different
# algorithmic approaches to knapsack problems. Here
# is a basic, recursive approach. 

# Returns the maximum value that
# can be put in a knapsack of
# capacity W


def knapSack(W, wt, val, n):

	# Base Case
	if n == 0 or W == 0:
		return 0

	# If weight of the nth item is
	# more than Knapsack of capacity W,
	# then this item cannot be included
	# in the optimal solution
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		return max(
			val[n-1] + knapSack(
				W-wt[n-1], wt, val, n-1),
			knapSack(W, wt, val, n-1))

# end of function knapSack


# Driver Code
if __name__ == '__main__':
	profit = [60, 100, 120]
	weight = [10, 20, 30]
	W = 50
	n = len(profit)
	print(knapSack(W, weight, profit, n))


