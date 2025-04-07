arrayData = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]

# Insertion Sort

def InsertionSort():
	arraysize = len(arrayData)

	for pointer in range(1, arraysize):
		valuetoinsert = arrayData[pointer]
		holePosition = pointer

		while holePosition > 0 and arrayData[holePosition - 1] > valuetoinsert: 
			arrayData[holePosition] = arrayData[holePosition - 1]
			holePosition -= 1
		arrayData[holePosition] = valuetoinsert
