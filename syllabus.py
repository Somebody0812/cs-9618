'''SHOW UNDERSTANDING OF LINEAR AND BINARY SEARCHING METHODS'''

# Linear Search
# In this, each element in an array is checked one by one in order from lower bound
# till upper bound until the item is found or lower bound = upper bound

arrayData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linearSearch(toSearch):
	for x in range(0, 10):
		if arrayData[x] == toSearch:
			return True
	return False



# Binary Search
# In this, the array is divided into two halves and the middle element is checked
# If the middle element is equal to the item, the search is successful
# If the value required is less than middle value then (LowerBound = Midpoint + 1)
# If the value required is less than middle value then (UpperBound = Midpoint - 1)
# This process is repeated until the item is found or the lower bound = upper bound
# Conditions: The array must be sorted in ascending order, fixed size, and no duplicates

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
		




'''Show understanding of insertion sort and bubble sort methods

Performance of a sorting routine may depend on
the initial order of the data and the number of data
items'''

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





'''Show understanding of and use Abstract Data Types (ADT)'''

'''
   1. Stack: A list operating on the Last In First Out (LIFO) principle. Items can be added to the stack (Push) and removed from the
   stack (Pop). The first item added to the stack is the last item removed.
'''
StackData = []
stackPointer = 0
def Push(value):
	if stackPointer > len(StackData) - 1:
		print('Stack is full.')

	else:
		StackData[stackPointer] = value
		stackPointer += 1
		print('Value pushed to stack.')

def Pop():
	if stackPointer == 0:
		print('Stack is empty.')
	else:
		stackPointer -= 1
		print(StackData[stackPointer])



'''
   2. Queue: A list operating on the First In First Out (FIFO) principle. Data is added (enqueue) from the rear end by using the EndPointer and
   removed (dequeue) from the front end using the StartPointer. The first item added is the first item removed from the queue.'''

QueueData = []
StartPointer = -1
EndPointer = 0

# Linear enqueue
def Enqueue(value):
	if EndPointer < 10:
		QueueData[EndPointer] = value
		EndPointer += 1
		
		if StartPointer == -1:
			StartPointer = 0
	
	else:
		print("Queue is full")

# Linear dequeue
def Dequeue():
	if StartPointer == -1:
		print('Queue is empty')
		return

	item = QueueData[StartPointer]
	print(item)
	StartPointer += 1

	if StartPointer == EndPointer:
		EndPointer = 0
		StartPointer = -1


NumberOfItems = 8 # Random value

# Circular enqueue

def CircularEnqueue(value):

	if NumberOfItems >= 10:
		return False
	
	QueueData[EndPointer]  = value
	if EndPointer >= 9:
		EndPointer = 0

	else:
		EndPointer += 1

	NumberOfItems += 1
	return True

def CircularDequeue(value):
	if NumberOfItems == 0:
		return 'Queue is full'
	
	StartPointer += 1
	if StartPointer > 9:
		StartPointer = 0

	NumberOfItems -= 1



'''
	Linked Lists
	
	- Can be ordered or unordered
	- For incrementing the pointer --> point = List[point].pointer # this increments till the end of the list ig
	'''

class node():
	def __init__(self, nData, nPointer):
		self.data = nData
		self.nextNode = nPointer

	def __repr__(self):
		return f"({self.data}, {self.nextNode})"

linkedlist = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
# Think of this in the sense where it creates a list with 2 rows (data, pointer) and x columns as shown below
'''
| Index | Data | NextNode |
|-------|------|----------|
|   0   |  1   |    1     |
|   1   |  5   |    4     |
|   2   |  6   |    7     |
|   3   |  7   |   -1     |
|   4   |  2   |    2     |
|   5   |  0   |    6     |
|   6   |  0   |    8     |
|   7   |  56  |    3     |
|   8   |  0   |    9     |
|   9   |  0   |   -1     |

'''
startPointer = 0 # first index value
emptyList = 5 # first node where data = 0

def AddLinkedListNode(currentPointer):
	global linkedlist
	global emptyList

	data = int(input("Enter the data to add: "))

	# Check if linked list is full
	if emptyList < 0 or emptyList > 9:
		return "List is full."

	else:
		freeList = emptyList # Basically, you have to store the currently free index value into emptyList
		emptyList = linkedlist[emptyList].nextNode # And update emptyList to the next index that is empty

		linkedlist[freeList] = node(data, -1) # Now add data to where the freeList is pointing with null pointer because its most recent

		previousPointer = 0

		while currentPointer != -1:
			previousPointer = currentPointer
			currentPointer = linkedlist[currentPointer].nextNode

		linkedlist[previousPointer].nextNode = freeList
		return True
	
def DeleteLinkedListNode():
	global linkedlist
	global emptyList
	global startPointer

	currentPointer = startPointer
	data = int(input("Enter the data to delete: "))

	previousPointer = 0
	while currentPointer != -1 and linkedlist[currentPointer].data != data:
		previousPointer = currentPointer
		currentPointer = linkedlist[currentPointer].nextNode
	
	if currentPointer == -1:
		return False
	
	else:
		if currentPointer == startPointer:
			startPointer = linkedlist[startPointer].nextNode
		
		else:
			linkedlist[previousPointer].nextNode = linkedlist[currentPointer].nextNode
		
		linkedlist[currentPointer].data = 0
		linkedlist[currentPointer].nextNode = emptyList
		emptyList = currentPointer
		return True
	
def SearchLinkedList(currentPointer, searchVal):
	while currentPointer != -1:
		if linkedlist[currentPointer].data != searchVal:
			currentPointer = linkedlist[currentPointer].nextNode
		
		else:
			return currentPointer
	
	currentPointer = -1
	return currentPointer

# AddLinkedListNode(currentPointer)
# AddLinkedListNode(currentPointer)
# print(linkedlist)	

def AddOrderedLinkedListNode(currentPointer):
	global linkedlist
	global emptyList

	data = int(input("Enter the data to add: "))

	# Check if linked list is full
	if emptyList < 0 or emptyList > 9:
		return "List is full."

	else:
		freeList = emptyList # Basically, you have to store the currently free index value into emptyList
		emptyList = linkedlist[emptyList].nextNode # And update emptyList to the next index that is empty

		linkedlist[freeList] = node(data, -1) # Now add data to where the freeList is pointing with null pointer because its most recent


		while currentPointer != -1 and linkedlist[currentPointer].Data < data:
			previousPointer = currentPointer
			currentPointer = linkedlist[currentPointer].nextNode
		
		if currentPointer == startPointer:
			linkedlist[freeList].nextNode = startPointer
			startPointer = freeList
		
		else:
			linkedlist[freeList].nextNode = linkedlist[previousPointer].nextNode
			linkedlist[previousPointer].nextNode = freeList

		return True



'''
	Binary Tree

           10
         /    \
        9      30
       /      /  \
      8      25   40
     /              \
    4               50

	How the above can be shown in exams: (i.e. how its initialised)

		Index | LeftPointer | Data | RightPointer
		---------------------------
		0     | 2           | 10   | 1
		1     | 3           | 30   | 5
		2     | 4           | 9    | None
		3     | None        | 25   | None
		4     | 6           | 8    | None
		5     | None        | 40   | 7
		6     | None        | 4    | None
		7     | None        | 50   | None

	Key Points:

	- Always start comparing from root node
	- If bigger value then root -> move right
	- If smaller value then root -> move left
   

	Binary Tree Construction:

		TYPE node
			DECLARE LeftP : Integer
			DECLARE Data : String
			DECLARE RightP : Integer
		ENDTYPE
'''

class BinaryTreeNode():
	def __init__(self, leftP, dataP, rightP):
		self.LeftPointer = leftP
		self.Data = dataP
		self.RightPointer = rightP

Tree = [[0 for x in range(3)] for y in range(8)] # Making it like the example above
FreePointer = 0 # Points towards where the first data is stored
RootPointer = -1 # Points towards the root e.g. 10 in the example above

def AddNode(NodeData: int):
	global Tree
	global FreePointer
	global RootPointer
	#NodeData = int(input("Enter the data: ")) # Passing my data for easier testing

	if FreePointer <= 8:
		Tree[FreePointer][0] = -1
		Tree[FreePointer][1] = NodeData
		Tree[FreePointer][2] = -1

		# Check if you want to store it in the first node
		if RootPointer == -1:
			RootPointer = 0
		else:
			Placed = False
			CurrentPointer = RootPointer
			while Placed == False:
				if NodeData < Tree[CurrentPointer][1]:
					if Tree[CurrentPointer][0] == -1:
						Tree[CurrentPointer][0] = FreePointer
						Placed = True
					
					else:
						CurrentPointer = Tree[CurrentPointer][0]
					
				else:
					if Tree[CurrentPointer][2] == -1:
						Tree[CurrentPointer][2] = FreePointer
						Placed = True
					
					else:
						CurrentPointer = Tree[CurrentPointer][2]
		
		FreePointer += 1
	
	else:
		print("Tree is full")

# print(Tree)
# AddNode(10)
# AddNode(30)
# AddNode(9)
# AddNode(25)
# AddNode(8)
# AddNode(40)
# AddNode(4)
# AddNode(50)
# print(Tree)