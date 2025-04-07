# Q1

Animals = [] # 10 string

Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

def SortDescending():
	global Animals
	ArrayLength = len(Animals)
	for x in range(0, ArrayLength-1):
		for y in range(0, ArrayLength-x-1):
			if Animals[y][0] < Animals[y+1][0]:
				temp = Animals[y]
				Animals[y] = Animals[y+1]
				Animals[y+1] = temp

SortDescending()
for i in Animals:
	pass
	#print(i)



# Q2

class SaleData:
	def __init__(self, sID, sQuantity):
		self.SaleID = sID
		self.Quantity = sQuantity

CircularQueue =[SaleData("", -1) for i in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(value):
	global Tail
	global CircularQueue
	global NumberOfItems

	if NumberOfItems >= 5:
		return -1
	
	CircularQueue[Tail]  = value
	if Tail >= 4:
		Tail = 0

	else:
		Tail += 1

	NumberOfItems += 1
	return 1

def Dequeue():
	global NumberOfItems
	global Head
	if NumberOfItems == 0:
		return "Queue is empty"
	ret = CircularQueue[Head]
	Head += 1
	if Head > 5:
		Head = 0

	NumberOfItems -= 1
	return ret.SaleID, ret.Quantity

def EnterRecord(aID, aQnt):
	inputID = aID #input("Enter the ID: ")
	quantity = aQnt #input("Enter the quantity: ")

	stored = Enqueue(SaleData(str(inputID), int(quantity)))

	if stored == -1:
		print("Full")

	else:
		print("Stored")

# EnterRecord("ADF", 10)
# EnterRecord("OOP", 1)
# EnterRecord("BXW", 5)
# EnterRecord("XXZ", 22)
# EnterRecord("HQR", 6)
# EnterRecord("LLP", 3)
# print(Dequeue())
# EnterRecord("LLP", 3)
# for i in CircularQueue:
# 	print(i.SaleID, i.Quantity)



# Q3

class Employee():
	def __init__(self, hourlyP, employeeN, jobT):
		self.__HourlyPay = hourlyP
		self.__EmployeeNumber = employeeN
		self.__JobTitle = jobT
		self.__PayYear2022 = []
		for x in range(0, 52):
			self.__PayYear2022.append(0.00)

	def GetEmployeeNumber(self):
		return self.__EmployeeNumber
	
	def SetPay(self, weekNum, noOfHours):
		week_pay = weekNum * noOfHours
		self.__PayYear2022[weekNum] = week_pay

	def GetTotalPay(self):
		total = 0
		for i in self.__PayYear2022:
			total += i

		return total
	
class Manager(Employee):
	def __init__(self, hourlyP, employeeN, jobT, BonusP):
		super().__init__(hourlyP, employeeN, jobT)
		self.__BonusValue = BonusP

	def SetPay(self, weekNum, noOfHours):
		noOfHours += noOfHours * (self.__BonusValue / 100)
		super().SetPay(weekNum, noOfHours)