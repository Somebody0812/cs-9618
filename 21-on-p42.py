# Q1

def Unknown(x, y: int): # RETURNS integer
    if x < y:
        print(x+y)
        return (Unknown(x+1, y) * 2)
    else:
        if x == y:
            return 1
        
        else:
            print(x+y)
            return int(Unknown(x-1, y) / 2)

print("Parameters: 10 and 15")
print(Unknown(10, 15))

print("Parameters: 10 and 10")
print(Unknown(10, 10))

print("Parameters: 15 and 10")
print(Unknown(15, 10))

def IterativeUnknown(x, y:int): # DIDNT KNOW THIS. LEARN ITERATIVE VS RECURSIVE
    total = 1
    while x != y:
        print(x+y)
        if x < y:
            x += 1
            total *= 2
        else:
            x -= 1
            total = int(total / 2)
    return total

print("Parameters: 10 and 15")
print(IterativeUnknown(10, 15))

print("Parameters: 10 and 10")
print(IterativeUnknown(10, 10))

print("Parameters: 15 and 10")
print(IterativeUnknown(15, 10))


# Q2

class Picture():
    # Private Description: String
    # Private Width : Integer
    # Private Height : Integer
    # Private FrameColour : String
    def __init__(self, pDesc, pWidth, pHeight, pColour):
        self.__Description = pDesc
        self.__Width = pWidth
        self.__Height = pHeight
        self.__FrameColour = pColour

    def GetDescription(self):
        return self.__Description
    
    def GetWidth(self):
        return self.__Width
    
    def GetHeight(self):
        return self.__Height
    
    def getColour(self):
        return self.__FrameColour
    
    def SetDescription(self, newDesc):
        self.__Description = newDesc

PicturesArray = []
for i in range(100):
    PicturesArray.append(Picture("", 0, 0, ""))

def ReadData(PicturesArray):
    filename = "Pictures.txt"
    count = 0
    try:
        file = open(filename, "r")
        dataRead = file.readline().strip()
        while dataRead != "":
            desc = dataRead.lower()
            width = int(file.readline().strip())
            height = int(file.readline().strip())
            colour = (file.readline().strip()).lower()
            obj = Picture(desc, width, height, colour)
            PicturesArray[count] = obj
            dataRead = file.readline().strip()
            count += 1
        file.close()
    except IOError:
        print("Could not open file.")
    
    return count, PicturesArray

ReadData(PicturesArray)
colour = (input("Please enter a frame colour")).lower()
max_width = int(input("Please enter the width"))
max_height = int(input("Please enter the height"))

for i in PicturesArray:
    if ((PicturesArray[3]).lower() == colour) and (PicturesArray[1] <= max_width) and (PicturesArray[2] <= max_height):
        output = f"Description: {PicturesArray[0]}\nWidth: {PicturesArray[1]}\nHeight: {PicturesArray[2]}\nColour: {PicturesArray[3]}"



# Q3

ArrayNodes = [[0 for x in range(3)] for y in range(20)]
RootPointer = -1 # DECLARE RootPointer : Integer
FreeNode = 0 # DECLARE FreeNode : Integer

def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the data: "))

    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1

        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]

                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode 

def PrintAll(ArrayNodes):
    for X in range(0, 20):
         print(str(ArrayNodes[X][0]), " ", str(ArrayNodes[X][1])," ", str(ArrayNodes[X][2])) 



for i in range(10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)

PrintAll(ArrayNodes)


# PART E LEFT BRUHHHHHHHHHHHHHHHHHH