# Linked Lists

# - Can be ordered or unordered
# - For incrementing the pointer --> point = List[point].pointer # this increments till the end of the list

class node():
	def __init__(self, nData, nPointer):
		self.data = nData
		self.nextNode = nPointer

	def __repr__(self): # Just to make outputing the linked list easier. Ignore this.
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
startPointer = 0 # the index where the actual list starts
emptyList = 5 # where the first unused (empty) node is

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

		linkedlist[freeList] = node(data, -1) # Add data to where list is 'free'

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