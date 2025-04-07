# Bubble Sort
# Arranges an array either in ascending or descending order
# There are two loops, the outer loop is for the number of passes and the inner loop is for the number of comparisons
# Efficient code: outer loop is conditional loop, inner loop is for loop.
# Inefficient code: both are For loops, and extra loops are used that waste time

'''The correct way to swap a variable:
array = [9, 0]
temp = array[0]
array[0] = array[1]
array[1] = temp
'''

arrayData = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]

def BubbleSort():
	NoSwaps = False
	Boundary = len(arrayData) - 1 #9
	while NoSwaps == False:
		NoSwaps = True
		for x in range(0, Boundary):
			if arrayData[x] > arrayData[x + 1]:
				temp = arrayData[x]
				arrayData[x] = arrayData[x + 1]
				arrayData[x + 1] = temp
				NoSwaps = False
		Boundary -= 1