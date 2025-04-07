# Q1

class node():
	def __init__(self, ndata, nextNodeP):
		self.data = ndata
		self.nextNode = nextNodeP

def outputNodes(array, startPointer):
	while (startPointer != -1):
		print(array[startPointer].data)
		startPointer = array[startPointer].nextNode

def addNodes(linkedList, startPointer, emptyList): # DO THIS LATER
	pass

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5

outputNodes(linkedList, 0)




# Q2

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(toSearch):
	for i in arrayData:
		if i == int(toSearch):
			return True
	return False

print('Enter the value to search')
value = input()
found = linearSearch(value)
if found:
	print('Value found')

else:
	print('Value not found')

theArray = []
def BubbleSort():
	temp = 0
	for x in range(0, 10):
		for y in range(0, 9):
			if theArray[y] > theArray[y+1]:
				temp = theArray[y]
				theArray[y] = theArray[y+1]
				theArray[y+1] = temp




# Q3

class TreasureChest():
	# Private question : String
	# Private answer : Integer
	# Private points : Integer
	def __init__(self, cQuestion, cAnswer, cPoints):
		self.__question = cQuestion
		self.__answer = cAnswer
		self.__points = cPoints
	
	def getQuestion(self):
		return self.__question
	
	def getAnswer(self, userAnswer):
		if userAnswer == self.__answer:
			return True
		return False
	
	def getPoints(self, Attempts):
		if Attempts == 1:
			return self.__points
		elif Attempts == 2:
			return (self.__points / 2)
		elif (Attempts == 3) or (Attempts == 4):
			return (self.__points / 4)
		else:
			return 0

arrayTreasure = []
def readData():
	filename = 'TreasureChestData.txt'
	try:
		file = open(filename, "r")
		dataRead = (file.readline()).strip()
		while (dataRead != ""):
			question = dataRead
			answer = (file.readline()).strip()
			points = (file.readline()).strip()
			obj = TreasureChest(question, answer, points)
			arrayTreasure.append(obj)
			dataRead = (file.readline()).strip()
		file.close()
	except:
		print('Could not find file.')

# MADE A MISTAKE BELOW
readData()
choice = int(input("Pick a treasure chest to open"))
if choice > 0 and choice < 6:
	result = False
	attempts = 0
	while result == False:
		answer = int(input(arrayTreasure[choice-1].getQuestion()))
		result = arrayTreasure[choice-1].checkAnswer(answer)
		attempts = attempts + 1
	print(int(arrayTreasure[choice-1].getPoints(attempts))) 