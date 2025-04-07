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