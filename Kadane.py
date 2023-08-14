# Python program to find maximum contiguous subarray
# in an ordinary array.
# The idea of Kadane’s algorithm is to maintain a variable max_ending_here thatstores the
# maximum sum contiguous subarray ending at current index and a variable max_so_far that
#stores the maximum sum of contiguous subarray found so far, Everytime there is a positive-sum
# value in max_ending_here compare it with max_so_far and update max_so_far if it is greater than max_ending_here.
# Time complexity O(n) and space complexity is O(1).

from sys import maxsize


def maxSubArraySum(a, size):

	max_so_far = -maxsize - 1
	max_ending_here = 0

	for i in range(0, size):
		max_ending_here = max_ending_here + a[i]
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here

		if max_ending_here < 0:
			max_ending_here = 0
	return max_so_far

# Driver code  to test the above function


a = [-2, -3, 4, -1, -2, 1, 5, -3]

print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))


