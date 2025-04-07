# Q1
Jobs = []
NumberOfJobs = 0

def Initialise():
    global Jobs
    global NumberOfJobs
    for x in range(0, 100):
        Jobs.append([-1, -1])
    NumberOfJobs = 0

def AddJob(JobNumber, JobPriority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs == 100: # Check if full, if not then add it
        print("Not added.")
        return
    Jobs[NumberOfJobs] = [JobNumber, JobPriority]
    print('Added.')
    NumberOfJobs += 1

def InsertionSort(): # MISTAKE: Insertion Sort
    global Jobs
    global NumberOfJobs
    for i in range(1, NumberOfJobs):
        One = Jobs[i][0]
        Two = Jobs[i][1]
        while i > 0 and Jobs[i-1][1] > Two:
            Jobs[i][0] = Jobs[i-1][0]
            Jobs[i][1] = Jobs[i-1][1]
            i -= 1
        Jobs[i][0] = One
        Jobs[i][1] = Two

def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(0, NumberOfJobs):
        print(str(Jobs[i][0]) + ' priority ' + str(Jobs[i][1]))

Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)
InsertionSort()
PrintArray()


# Q2

class Character:
    def __init__(self, SName, SX, SY):
        self.__Name = SName
        self.__XCoordinate = SX
        self.__YCoordinate = SY

    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
    
    def GetY(self):
        return self.__YCoordinate
    
    def ChangePosition(self, Xadd, Yadd):
        self.__XCoordinate += Xadd
        self.__YCoordinate += Yadd


CharacterArray = []
try:
    CharInfo = open('Characters.txt', 'r')
    for i in range(0, 10):
        Name = CharInfo.readline().strip()
        x = int(CharInfo.readline().strip())
        y = int(CharInfo.readline().strip())
        CharacterArray[i] = Character(Name, x, y)

except:
    print('File not found.')

# I CANT DO PART E AAAAAAAAA



# Q3

Queue = [-1 for i in range(100)]
HeadPointer = -1
TailPointer = 0

def Enqueue(Value):
    global Queue
    global HeadPointer
    global TailPointer
    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = Value
        TailPointer += 1
        return True
    return False

def RecursiveOutput(start):
    if start == 0:
        return Queue[start]
    else:
        return Queue[start] + RecursiveOutput(start - 1)
for i in range(1, 21):
    value = Enqueue(i)
    if value:
        print('Successful')
    else:
        print('Unsuccessful')

print(RecursiveOutput(19))
    
    