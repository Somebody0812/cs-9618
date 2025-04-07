# Binary Search
# In this, the array is divided into two halves and the middle element is checked
# If the middle element is equal to the item, the search is successful
# If the value required is less than middle value then (LowerBound = Midpoint + 1)
# If the value required is less than middle value then (UpperBound = Midpoint - 1)
# This process is repeated until the item is found or the lower bound = upper bound
# Conditions: The array must be sorted in ascending order, fixed size, and no duplicates

arrayData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def BinarySearch(number):
	upperbound = len(arrayData) - 1
	lowerbound = 0
	found = False
	notinlist = False

	while notinlist == False and found == False:
		midpoint = ((upperbound + lowerbound) / 2)
		if arrayData[midpoint] == number:
			found = True
			return True
		elif arrayData[midpoint] < number:
			lowerbound = midpoint + 1
		elif arrayData[midpoint] > number:
			upperbound = midpoint - 1

		if lowerbound > upperbound:
			notinlist = True
			return False