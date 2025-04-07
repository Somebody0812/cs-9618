
# 1. Stack: A list operating on the Last In First Out (LIFO) principle. Items can be added to the stack (Push) and removed from the
# stack (Pop). The first item added to the stack is the last item removed.

StackData = [-1 for x in range(10)]
stackPointer = 0 # Also known as Head/HeadPointer 
# stackPointer points towards the next free space or last value added (depending on the question)

def Push(value):
	global StackData, stackPointer # access them

	if stackPointer > len(StackData) - 1: # if stackPointer == len(StackData): return False
		print('Stack is full.')

	else:
		StackData[stackPointer] = value # Value is put first, pointer is updated after
		stackPointer += 1
		print('Value pushed to stack.')

def Pop():
	# In Pop(), the value isn't removed because that's not necessary. The HeadPointer is -1 though

	global stackPointer

	if stackPointer == 0:
		print('Stack is empty.')

	else:
		stackPointer -= 1
		print(StackData[stackPointer]) # Question usually asks to return last item. Pointer is updated before.