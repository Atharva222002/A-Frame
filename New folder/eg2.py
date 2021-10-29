# Python3 program to count number of
# subsets with given GCDs

# n is size of arr[] and m is sizeof gcd[]
def countSubsets(arr, n, gcd, m):

	# Map to store frequency of array elements
	freq = dict()

	# Map to store number of subsets
	# with given gcd
	subsets = dict()

	# Initialize maximum element.
	# Assumption: all array elements
	# are positive.
	arrMax = 0

	# Find maximum element in array and
	# fill frequency map.
	for i in range(n):
		arrMax = max(arrMax, arr[i])
		if arr[i] not in freq:
			freq[arr[i]] = 1
		else:
			freq[arr[i]] += 1

	# Run a loop from max element to 1
	# to find subsets with all gcds
	for i in range(arrMax, 0, -1):
		sub = 0
		add = 0
		if i in freq:
			add = freq[i]
		j = 2

		# Run a loop for all multiples of i
		while j * i <= arrMax:

			# Sum the frequencies of every element
			# which is a multiple of i
			if j * i in freq:
				add += freq[j * i]

			# Excluding those subsets which have
			# gcd > i but not i i.e. which have gcd
			# as multiple of i in the subset.
			# for ex: {2,3,4} considering i = 2 and
			# subset we need to exclude are those
			# having gcd as 4
			sub += subsets[j * i]
			j += 1

		# Number of subsets with GCD equal
		# to 'i' is pow(2, add) - 1 - sub
		subsets[i] = (1 << add) - 1 - sub

	for i in range(m):
		print("Number of subsets with gcd %d is %d" %
			(gcd[i], subsets[gcd[i]]))

# Driver Code
if __name__ == "__main__":
	gcd = [1]
	arr = [9, 6, 2]
	n = len(arr)
	m = len(gcd)
	countSubsets(arr, n, gcd, m)

# This code is contributed by
# sanjeev2552
