# Q1

DataArray = [-1 for x in range(100)]

def ReadFile():
	global DataArray

	filename = 'IntegersData.txt'
	try:
		file = open(filename, "r")
		for i in range(100):
			DataArray[i] = file.readline().strip()

	except:
		pass

def FindValues():
	global DataArray

	count = 0
	value = input("Enter a number to search for: ")

	if value >=1 and value <=100:
		for i in range(100):
			if DataArray[i] == int(value):
				count += 1

	return count


def BubbleSort():
	global DataArray

	NoSwaps = False
	Boundary = len(DataArray) - 1
	while NoSwaps == False:
		NoSwaps = True
		for x in range(0, Boundary):
			if DataArray[x] > DataArray[x + 1]:
				temp = DataArray[x]
				DataArray[x] = DataArray[x + 1]
				DataArray[x + 1] = temp
				NoSwaps = False
		Boundary -= 1



# Q2

class Card():
	def __init__(self, cNumber, cColour):
		self.__Number = cNumber
		self.__Colour = cColour

	def GetNumber(self):
		return self.__Number
	
	def GetColour(self):
		return self.__Colour
	
class Hand():
	def __init__(self, Card1, Card2, Card3, Card4, Card5):
		self.__Cards = [Card1, Card2, Card3, Card4, Card5]
		self.__FirstCard = 0
		self.__NumberCards = 5

	def GetCard(self, index):
		return self.__Cards[index]
	
def CalculateValue(hand: Hand):
	total = 0

	for i in range(5):
		card = hand.GetCard(i)
		total += card.GetNumber()
		colour = card.GetColour()

		if colour == 'red':
			total += 5

		elif colour == 'blue':
			total += 10

		else:
			total += 15

	return total


	
OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")

OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")

OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")

Player1 = Hand(TwoYellow, ThreeYellow, ThreeRed, FourRed, OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue)

P1Score = CalculateValue(Player1)
P2Score = CalculateValue(Player2)

# if P1Score > P2Score:
# 	print("Player 1 won")

# elif P2Score > P1Score:
# 	print("Player 2 won")

# else:
# 	print("It was a draw")



# Q3

ArrayNodes = [[-1 for x in range(3)] for y in range(20)]

ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
ArrayNodes[6] = [-1, -1, -1]

RootPointer = 0
FreeNode = 6

def SearchValue(root, searchval):
	global ArrayNodes
	if root == -1:
		return -1
	
	elif ArrayNodes[root][1] == searchval:
		return root
	
	elif ArrayNodes[root][1] == -1:
		return -1
	
	if ArrayNodes[root][1] > searchval:
		return SearchValue(ArrayNodes[root][0], searchval)
	
	elif ArrayNodes[root][1] < searchval:
		return SearchValue(ArrayNodes[root][2], searchval)
	

def PostOrder(rootnode): # Made a mistake here
	if rootnode[0] != -1:
		PostOrder(ArrayNodes[rootnode[0]])
	if rootnode[2] != -1:
		PostOrder(ArrayNodes[rootnode[2]])

	print(str(rootnode[1]))

ReturnValue = SearchValue(RootPointer, 15)
if ReturnValue == -1:
	print("Not found")
else:
	print("Found at " + str(ReturnValue))
PostOrder(ArrayNodes[RootPointer])
