StackData = [-1 for x in range(10)]
StackPointer = 0

def OutputStack():
    global StackData
    global StackPointer

    for i in range(0, 10):
        print(StackData[i])
    print("Stack Pointer:", StackPointer)

def Push(value: int):
    global StackData
    global StackPointer

    if StackPointer == 10:
        return False
    
    StackData[StackPointer] = value
    StackPointer += 1
    return True

def Pop():
    global StackData
    global StackPointer

    if StackPointer == 0:
        return -1
    
    StackPointer -= 1
    item = StackData[StackPointer]
    return item

# Push(11)
# Push(12)
# Push(13)
# Push(14)
# Push(15)
# Push(16)
# Push(17)
# Push(18)
# Push(19)
# Push(20)
# Push(21)
# OutputStack()
# Pop()
# Pop()
# OutputStack()



# Q2 

import random
ArrayData = [[random.randint(2, 99) for x in range(10)] for y in range(10)]
ArrayData[0][3] = 21
# print(ArrayData)
# print('')
ArrayLength = 10
for x in range(0, ArrayLength): # MADE MISTAKE WITH THE ARRAYLENGTH RANGES HERE
    for y in range(0, ArrayLength):
        for z in range(0, ArrayLength - y -1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = TempValue

# print(ArrayData)
# print('')
def OutputArray():
    global ArrayData

    out_string = ''
    for i in range(10):
        for y in range(10):
            out_string += str(ArrayData[i][y]) + ' '
        
        print(out_string)
        out_string = ""

# OutputArray()

def BinarySearch(SearchArray, lower, upper, searchval):
    
    if upper >= lower:
        mid = int((lower + (upper-1)) / 2)
        if SearchArray[0][mid] == searchval:
            return mid
        
        elif SearchArray[0][mid] > searchval:
                return BinarySearch(SearchArray, lower, mid-1, searchval)

        else:
            return BinarySearch(SearchArray, mid+1, upper, searchval)
                
    return -1

# print(BinarySearch(ArrayData, 0, 10, 21))



# Q3

class Card:
    def __init__(self, cNumber, cColour):
        self.__Number = cNumber
        self.__Colour = cColour

    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
    
CardArray = [0 for x in range(30)]
filename = 'CardValues.txt'

try:
    file = open(filename, "r")
    data = file.readline().strip()
    index = 0
    while data != '' and data != 0:
        number = data
        colour = file.readline().strip()
        CardArray[index] = Card(number, colour)

        data = file.readline().strip()


except:
    print("could not open file")

Selected = []

def ChooseCard():
    found = False
    while found == False:
        value = int(input("Enter a number between 0 and 29: "))
        if value <= 29 and value >= 0:
            card = CardArray[value]
            if card not in Selected:
                Selected.append(card)
                found = True
                return value

Player1 = []
card1 = ChooseCard()
card2 = ChooseCard()
card3 = ChooseCard()
card4 = ChooseCard()

Player1.append(CardArray[card1])
Player1.append(CardArray[card2])
Player1.append(CardArray[card3])
Player1.append(CardArray[card4])

for x in range(4):
    print(Player1[x].GetColour())
    print(Player1[x].GetNumber())