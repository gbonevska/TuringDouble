# turing double machine

''' instruction A 0:(0,s,R) 1:(0,B,R) '''
def instrA(num):
    if num == 0:
        return (0, 's', 'R')
    else:
        return (0, 'B', 'R')

''' instruction B 0:(1,C,L) 1:(1,B,R) '''
def instrB(num):
    if num == 0:
        return (1, 'C', 'L')
    else:        
        return (1, 'B', 'R')
        
''' instruction C 0:(1,A,L) 1:(1,C,L) '''
def instrC(num):
    if num == 0:
        return (1, 'A', 'L')
    else:
        return (1, 'C', 'L')

''' find last right 1 '''
def findLastOne(binarNumList):
    lastOneIndex = 0
    for index in range(0,len(binarNumList)):
        if int(binarNumList[index]) == 1:
            lastOneIndex = index

    return lastOneIndex
    
''' function applyInstuction
    INPUT parameters:
    currentPossition - index of current list posision
    instruction - string of instruction letter
    doubledNumList - list of binary number (will be changed in this func.)
    OUTPUT
    instructionCommandsTuple - tuple with next instruction
'''
def applyInstruction(currentPosition, instruction, doubledNumList):
    if instruction == 'A':
        instructionCommandsTuple = instrA(int(doubledNumList[currentPosition]))
    elif instruction == 'B':
        instructionCommandsTuple = instrB(int(doubledNumList[currentPosition]))
    elif instruction == 'C':
        instructionCommandsTuple = instrC(int(doubledNumList[currentPosition]))
    else:
        instructionCommandsTuple = ()    

    doubledNumList[currentPosition] = str(instructionCommandsTuple[0])

    return instructionCommandsTuple[1:]

''' main logic of turing double machine '''
def turing_double(binarNumString):
    doubledNumList = list(binarNumString) # ['0', '1', '1', '1', '0', '0', '0', '0']

    count = 0
    instruction = 'A'
    currentPosition = findLastOne(doubledNumList)

    while instruction != 's':
        resultTuple = applyInstruction(currentPosition, instruction, doubledNumList)
        
        if resultTuple == ():
            break

        instruction = resultTuple[0]

        if resultTuple[1] == 'R':
            currentPosition +=1
        else:
            currentPosition -=1
    
    return ''.join(doubledNumList)
 
#print(turing_double('01110000'))
num = str(input("Please enter binary number for doubled:")) 
print(turing_double(num))
