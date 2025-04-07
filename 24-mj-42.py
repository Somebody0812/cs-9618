# Q1

NumberOfWords = 0
WordArray = []

def ReadWords(filename):
	global NumberOfWords
	global WordArray

	try:
		file = open(filename, "r")
		word = file.readline().strip()
		WordArray[0] = word
		answer = file.readline().strip()
		while answer != "":
			WordArray.append(answer)
			NumberOfWords += 1
			answer = file.readline().strip()
		
		file.close()
		Play()


	except:
		pass

def Play():
	global WordArray
	global NumberOfWords

	print(WordArray[0])
	user_answer = input("Enter the answer: ")
	correct = 0
	index = 0

	while (user_answer).lower() != "no":
		if user_answer in WordArray:
			WordArray[index] = ""
			correct += 1
			print("You answered correctly!")

		else:
			print("You did not answer correctly.")
		
		index += 1

	print("Percentage of answers entered: ", (correct/NumberOfWords)*100, "%")
	for i in WordArray:
		if i != "":
			print(i)

# option = input("Easy, medium, or hard?")
# if option.lower() == 'easy':
# 	ReadWords("Easy.txt")

# elif option.lower() == 'medium':
# 	ReadWords("Medium.txt")

# else:
# 	ReadWords("Hard.txt")



# Q2

class Node:
	def __init__(self, dataN):
		self.__LeftPointer = -1
		self.__Data = dataN
		self.__RightPointer = -1

	def GetLeft(self):
		return self.__LeftPointer
	
	def GetRight(self):
		return self.__RightPointer
	
	def GetData(self):
		return self.__Data
	
	def SetLeft(self, value):
		self.__LeftPointer = value

	def SetRight(self, value):
		self.__RightPointer = value

	def SetData(self, value):
		self.__Data = value

class TreeClass:
	def __init__(self):
		self.__Tree = []
		self.__FirstNode = -1
		self.__NumberNodes = 0
		for x in range(20):
			self.__Tree.append(Node(-1))

	def InsertNode(self, NewNodeObj):
		if self.__NumberNodes == 0:
			self.__Tree[self.__NumberNodes] = NewNodeObj
			self.__NumberNodes += 1
			self.__FirstNode = 0
			print('first')

		else:
			self.__Tree[self.__NumberNodes] = NewNodeObj

# EVERYTHING BELOW THIS I DID NOT KNOW

			NodeAccess = self.__FirstNode
			Direction = ""

			while (NodeAccess != -1):
				Previous = NodeAccess

				if NewNodeObj.GetData() < self.__Tree[NodeAccess].GetData(): 
					NodeAccess = self.__Tree[NodeAccess].GetLeft()
					Direction = "left"

				elif NewNodeObj.GetData() > self.__Tree[NodeAccess].GetData():
					NodeAccess = self.__Tree[NodeAccess].GetRight()
					Direction = "right"

				if (Direction == "left"):
					self.__Tree[Previous].SetLeft(self.__NumberNodes)
					self.__NumberNodes = self.__NumberNodes + 1

				else:
					self.__Tree[Previous].SetRight(self.__NumberNodes)
					self.__NumberNodes = self.__NumberNodes + 1

		print('doneanana')

	def OutputTree(self):
		if self.__NumberNodes == 0:
			print("No nodes.")

		else:
			for x in range(0, self.__NumberNodes):
				print(self.__Tree[x].GetLeft(), " ", self.__Tree[x].GetData(), " ",self.__Tree[x].GetRight())

# TheTree = TreeClass()
# TheTree.InsertNode(Node(10))
# TheTree.InsertNode(Node(11))
# TheTree.InsertNode(Node(5))
# TheTree.InsertNode(Node(1))
# TheTree.InsertNode(Node(20))
# TheTree.InsertNode(Node(7))
# TheTree.InsertNode(Node(15))
# TheTree.OutputTree()



# Q3

NumberArray = [100, 85, 644, 22, 15, 8, 1]

LastItem = 0
CheckItem = 0
LoopAgain = True

def RecursiveInsertion(IntegerArray: list, NumberElements: int):
	global LastItem
	global CheckItem
	global LoopAgain

	if NumberElements <= 1:
		return IntegerArray
	
	else:
		RecursiveInsertion(IntegerArray, NumberElements-1)
		LastItem = IntegerArray[NumberElements-1]
		CheckItem = NumberElements - 2
	
	LoopAgain = True
	if CheckItem < 0:
		LoopAgain = False
	elif IntegerArray[CheckItem] < LastItem:
		LoopAgain = False
	
	while LoopAgain == True:
		IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
		CheckItem -= 1
		if CheckItem < 0:
			LoopAgain = False
		elif IntegerArray[CheckItem] < LastItem:
			LoopAgain = False
	
	IntegerArray[CheckItem+1] = LastItem
	return IntegerArray

new_array = RecursiveInsertion(NumberArray, 7)
print("Recursive")
print(new_array)

def IterativeInsertion(): # Didn't know this
	pass

def BinarySearch(IntegerArray, First, Last, ToFind): # Didn't know this
	if First > Last:
		return -1
	
	else:
		Middle = int((First+Last)/2)

		if IntegerArray[Middle] == ToFind:
			return Middle
		
		elif IntegerArray[Middle] > ToFind:
			return BinarySearch(IntegerArray, First, Middle-1, ToFind)
		
		else:
			return BinarySearch(IntegerArray, Middle+1, Last, ToFind)