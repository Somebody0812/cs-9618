# Q1

class EventItem:
	def __init__(self, eName, eType, eDifficulty):
		self.__EventName = eName
		self.__Type = eType
		self.__Difficulty = eDifficulty

	def GetName(self):
		return self.__EventName
	
	def GetType(self):
		return self.__Type
	
	def GetDifficulty(self):
		return self.__Difficulty
	
Group = []
Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))

class Character:
	def __init__(self, cName, cJump, cSwim, cRun, cDrive):
		self.__CharacterName = cName
		self.__Jump = cJump
		self.__Swim = cSwim
		self.__Run = cRun
		self.__Drive = cDrive


	def CalculateScore(self, event, difficulty):
		if event.lower() == 'jump':
			level = self.__Jump

		elif event.lower() == 'swim':
			level = self.__Swim

		elif event.lower() == 'run':
			level = self.__Run

		else:
			level = self.__Drive

		if level >= difficulty:
			return 100
		else:
			difference = difficulty - level
			if difference == 1:
				return 80
			
			elif difference == 2:
				return 60
			
			elif difference == 3:
				return 40
			
			elif difference == 4:
				return 20
		
			else:
				return 0
		
Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)
TarzP = 0
GeniP = 0

# for i in range(5):
#     event_type = Group[i].GetType()
#     difficulty = Group[i].GetDifficulty()
 
#     if Tarz.CalculateScore(event_type, difficulty) > Geni.CalculateScore(event_type, difficulty):
#         TarzP += 1
#         print("Tarz has won the event.")

#     elif Tarz.CalculateScore(event_type, difficulty) < Geni.CalculateScore(event_type, difficulty):
#         GeniP += 1
#         print("Geni has won the event.")

#     else:
#         print("The event is a draw.")

# if TarzP > GeniP:
# 	print("Tarz has the most points", TarzP)

# elif GeniP > TarzP:
# 	print("Geni has the most points", GeniP)

# else:
# 	print("It is a draw.")

	

# Q2

class Queue:
	def __init__(self):
		self.QueueArray = []
		self.HeadPointer = 0
		self.TailPointer = 0
		for i in range(100):
			self.QueueArray.append(-1)

TheQueue = Queue()
TheQueue.HeadPointer = -1
TheQueue.TailPointer = 0

def Enqueue(aQueue: Queue, Data: int):
	if aQueue.HeadPointer == -1:
		aQueue.QueueArray[aQueue.TailPointer] = Data
		aQueue.HeadPointer = 0
		aQueue.TailPointer = aQueue.TailPointer + 1

	else:
		if aQueue.TailPointer > 100:
			return -1
		
		else:
			aQueue.QueueArray[aQueue.TailPointer] = Data
			aQueue.TailPointer = aQueue.TailPointer + 1
			return 1
		
def ReturnAllData():
	global TheQueue
	out_string = ""
	for i in range(TheQueue.HeadPointer, 100):
		if TheQueue.QueueArray[i] != -1:
			out_string += str(TheQueue.QueueArray[i]) + ' '

	print(out_string)


# Enqueue(TheQueue, 10)
# Enqueue(TheQueue, 9)
# Enqueue(TheQueue, 8)
# Enqueue(TheQueue, 7)
# Enqueue(TheQueue, 6)
# Enqueue(TheQueue, 5)
# Enqueue(TheQueue, 4)
# Enqueue(TheQueue, 3)
# Enqueue(TheQueue, 2)
# Enqueue(TheQueue, 1)
# ReturnAllData()

def Dequeue():
	global TheQueue

	if TheQueue.HeadPointer == -1:
		return -1
	
	
	item = TheQueue.QueueArray[TheQueue.HeadPointer]
	print(item)
	TheQueue.HeadPointer += 1

	if TheQueue.HeadPointer == TheQueue.TailPointer:
		TheQueue.HeadPointer = 0
		TheQueue.TailPointer = -1

# Dequeue()
# Dequeue()
# ReturnAllData()



# Q3

HighScores = [["" for x in range(3)] for x in range(7)]

HighScores[0] = ["GFED", "5", "25"]
HighScores[1] = ["HJKM", "4", "21"]
HighScores[2] = ["RERR", "4", "19"]
HighScores[3] = ["TTYU", "4", "15"]
HighScores[4] = ["WSVG", "3", "20"]
HighScores[5] = ["PPTR", "3", "15"]
HighScores[6] = ["SNQT", "2", "10"]

def ReadData():
	global HighScores
	filename = "HighScoresTable.txt"

	try:
		file = open(filename, "r")
		data = file.readline().strip()
		index = 0
		while data != "":
			HighScores[index][0] = data
			HighScores[index][1] = file.readline().strip()
			HighScores[index][2] = file.readline().strip()
			index += 1
			data = file.readline().strip()

	except:
		pass

def OutputHighScores(array):
	for x in array:
		pID = x[0]
		pLevel = x[1]
		pScore = x[2]
		print(pID, "reached level", pLevel, "with a score of", pScore)

def SortScores():
	global HighScores
	NoSwaps = False
	Boundary = len(HighScores) - 1

	while NoSwaps == False:
		NoSwaps = True
		for x in range(0, Boundary):
			if HighScores[x][1] < HighScores[x + 1][1]:
				temp = HighScores[x]
				HighScores[x] = HighScores[x + 1]
				HighScores[x + 1] = temp
				NoSwaps = False
		Boundary -= 1

SortScores()
print(HighScores)


