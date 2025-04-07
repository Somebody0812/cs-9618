# 2. Queue: A list operating on the First In First Out (FIFO) principle. Data is added (enqueue) from the rear end by using the EndPointer and
# removed (dequeue) from the front end using the StartPointer. The first item added is the first item removed from the queue.
# There are two types: linear and circular (minimal difference)

QueueData = []
StartPointer = -1
EndPointer = 0

# Linear enqueue
def Enqueue(value):
	if EndPointer < 10:
		QueueData[EndPointer] = value
		EndPointer += 1
		
		if StartPointer == -1: # If this is the first value
			StartPointer = 0   # .. then set startpointer -> 0
	
	else:
		print("Queue is full")

# Linear dequeue
def Dequeue():
	if StartPointer == -1:
		print('Queue is empty')
		return

	item = QueueData[StartPointer]
	print(item) # Question usually asks to output item. Item is output before Pointer is incremented +1
	StartPointer += 1

	if StartPointer == EndPointer: # If queue becomes empty, go back to initialization values 
		EndPointer = 0
		StartPointer = -1


NumberOfItems = 8 # Random value just for teesting purposes

# Circular enqueue

def CircularEnqueue(value):

	if NumberOfItems >= 10:
		return False
	
	QueueData[EndPointer]  = value # Store the value
	if EndPointer >= 9: # Now, if endpointer reaches its maximum value at the bottom, take it to the top i.e. 9 -> 0
		EndPointer = 0

	else:
		EndPointer += 1 # If it doesn't, then just increment as usual

	NumberOfItems += 1
	return True

def CircularDequeue(value):
	if NumberOfItems == 0:
		return 'Queue is full'
	
	StartPointer += 1
	if StartPointer > 9:
		StartPointer = 0

	NumberOfItems -= 1