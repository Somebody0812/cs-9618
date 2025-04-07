# Q1 

StackVowel = [] # string 100 
StackConsonant = [] # string 100

VowelTop = 0 # DECLARE VowelTop : INTEGER
ConsonantTop = 0 # DECLARE ConsonantTop : INTEGER

def PushData(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter.lower() in vowels:
        if VowelTop <= 99:
            StackVowel.append(letter)
            VowelTop += 1
            return

        else:
            print("Vowel stack is full.")
            return

    if ConsonantTop <= 99:
        StackConsonant.append(letter)
        ConsonantTop += 1
    
    else:
        print("Consonant stack is full")


def ReadData():
    filename = "StackData.txt"
    try:
        file = open(filename, "r")
        letter = file.readline().strip()
        while letter != "":
            PushData(letter)
            letter = file.readline.strip()

    except:
        print("Could not find file.")

def PopVowel():
    if VowelTop > 0:
        TopVowel = StackVowel[VowelTop]
        StackVowel.pop(VowelTop)
        VowelTop -= 1
        return TopVowel

    else:
        return "No data"
    
def PopConsonant():
    if ConsonantTop > 0:
        TopConsonant = StackConsonant[ConsonantTop]
        ConsonantTop.pop(ConsonantTop)
        ConsonantTop -= 1
        return ConsonantTop

    else:
        return "No data"
    
# ReadData()
# choice = input("Vowel or Consonant?")
# out_string = ""
# if choice.lower() == "vowel":
#     out_string += PopVowel()

# else:
#     out_string += PopConsonant()

# print(out_string)



# Q2

def IterativeCalculate(num: int):
    ToFind = num
    Total = 0
    while num != 0:
        if (ToFind % num) == 0:
            Total += num
        
        num -= 1
    
    return Total

print(IterativeCalculate(10))

def RecursiveValue(num, ToFind: int):
    if num == 0:
        return 0
    
    else:
        if ToFind % num == 0:
            return num + RecursiveValue(num-1, ToFind)
        
        else:
            return RecursiveValue(num-1, ToFind)
        
print(RecursiveValue(50, 50))



# Q3

class Character():
    def __init__(self, cName, dob, intel, spd):
        self.__CharacterName = cName
        self.__DateOfBirth = dob
        self.__Intelligence = intel
        self.__Speed = spd

    def GetName(self):
        return self.__CharacterName
    
    def GetIntelligence(self):
        return self.__Intelligence

    def SetIntelligence(self, value):
        self.__Intelligence = value

    def Learn(self):
        self.__Intelligence += (self.__Intelligence * 0.1)

    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year
    
import datetime
FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)

FirstCharacter.Learn()
print(FirstCharacter.GetName(), "is", FirstCharacter.ReturnAge(), "years old and has intelligence" , FirstCharacter.GetIntelligence())

class MagicCharacter(Character):
    def __init__(self, ElementP, cName, dob, intel, spd):
        super().__init__(cName, dob, intel, spd)
        self.__Element = ElementP

    def Learn(self):
        if(self.__Element == "fire" or self.__Element == "water"):
            super().SetIntelligence(super().GetIntelligence() * 1.2)
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence() * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.1)


FirstMagic = MagicCharacter("fire", "Light", datetime.datetime(2018, 3, 3), 75, 22)

FirstMagic.Learn()
print(FirstMagic.GetName(), "is", FirstMagic.ReturnAge(), "years old and has intelligence", FirstMagic.GetIntelligence())
