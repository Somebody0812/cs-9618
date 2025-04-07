# Linear Search
# In this, each element in an array is checked one by one in order from lower bound
# till upper bound until the item is found or lower bound = upper bound

arrayData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linearSearch(toSearch):
	for x in range(0, 10):
		if arrayData[x] == toSearch:
			return True
	return False