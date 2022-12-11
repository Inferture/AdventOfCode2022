#Utilities

from parse import *
import numpy as np

def getInput(day):
    f = open("./input_" + str(day) + ".txt")
    return f.read()

def getInputSplit(day):
    return getInput(day).strip().split('\n')


#Day 1

def solveDay1A():
    lines = getInputSplit(1)
    maximum=0
    currentSum=0
    for line in lines:
        if len(line) > 0 :
            currentSum = currentSum + int(line)
        else:
            maximum=max(maximum, currentSum)
            currentSum=0
    return maximum

def solveDay1B():
    lines = getInputSplit(1)
    maxima=[0,0,0]
    currentSum=0
    for line in lines:
        if len(line) > 0:
            currentSum = currentSum + int(line)
        else:
            place = -1
            i=0
            while i < len(maxima) and currentSum > maxima[i] :
                place = i
                i = i + 1
            if place >= 0:
                for i in range(0,place):
                    maxima[i]=maxima[i+1]
                maxima[place]=currentSum
            currentSum=0
    return sum(maxima)


#Day 2

def solveDay2A():
    lines = getInputSplit(2)
    totalScore=0
    for line in lines:
        advPlay = line.split(' ')[0]
        yourPlay = line.split(' ')[1]
        advPoints = 1 if advPlay=="A" else (2 if advPlay == "B" else 3)
        yourPoints = 1 if yourPlay=="X" else (2 if yourPlay == "Y" else 3)
        totalScore = totalScore + yourPoints + 3 * ((yourPoints - advPoints  + 4) % 3)
    return totalScore

def solveDay2B():
    lines = getInputSplit(2)
    totalScore=0
    for line in lines:
        advPlay = line.split(' ')[0]
        yourPlay = line.split(' ')[1]
        advPoints = 1 if advPlay=="A" else (2 if advPlay == "B" else 3)
        outcomePointsThird = 0 if yourPlay=="X" else (1 if yourPlay == "Y" else 2)
        totalScore = totalScore + 3 * outcomePointsThird + ((advPoints + outcomePointsThird  + 1) % 3 + 1)
    return totalScore


#Day 3

def charValue(c):
    return ord(c) - 38 if ord(c) < 91 else ord(c) - 96

def solveDay3A():
    lines = getInputSplit(3)
    totalPriority=0
    for line in lines:
        line1 = line[:int(len(line)/2)]
        line2 = line[int(len(line)/2):]
        totalPriority = totalPriority + sum(dict.fromkeys([charValue(c) for c in line1 if c in line2]))
    return totalPriority

def solveDay3B():
    lines = getInputSplit(3)
    totalPriority=0
    for i in range(int(len(lines)/3)):
        line1 = lines[3*i]
        line2 = lines[3*i+1]
        line3 = lines[3*i+2]
        totalPriority = totalPriority + sum(dict.fromkeys([charValue(c) for c in line1 if c in line2 and c in line3]))
    return totalPriority


#Day 4

def solveDay4A():
    lines = getInputSplit(4)
    total=0
    for line in lines:
        line1, line2 = line.split(',')[0], line.split(',')[1]
        a,b,c,d=int(line1.split('-')[0]), int(line1.split('-')[1]), int(line2.split('-')[0]), int(line2.split('-')[1])
        if (a >= c and b <= d) or (c >= a and d <= b):#a-b,c-d
            total = total + 1
    return total


def solveDay4B():
    lines = getInputSplit(4)
    total=0
    for line in lines:
        line1, line2 = line.split(',')[0], line.split(',')[1]
        a,b,c,d=int(line1.split('-')[0]), int(line1.split('-')[1]), int(line2.split('-')[0]), int(line2.split('-')[1])
        if (a >= c and a <= d) or (c >= a and c <= b): #a-b,c-d
            total = total + 1
    return total


#Day 5

def solveDay5A():
    lines = getInput(5).split('\n')
    total=0
    reverseCrates = []
    for line in lines[:8]:
        reverseCrates.append(line[1::4])

    crates = [[reverseCrates[i][j] for i in range(len(reverseCrates)) if len(reverseCrates[i][j].strip()) > 0] for j in range(len(reverseCrates[0]))]

    for line in lines[10:]:
        if(len(line.split(' '))>5):
            num = int(line.split(' ')[1])
            fro = int(line.split(' ')[3])
            to = int(line.split(' ')[5])
            for i in range(num):
                if(len(crates[fro - 1])>0):
                    crates[to - 1] = [crates[fro - 1][0]] + crates[to - 1]
                    crates[fro - 1] = crates[fro - 1][1:]
    s=""
    for crate in crates:
        if len(crate)>0:
            s = s + crate[0]
                      
    return s

def solveDay5B():
    lines = getInput(5).split('\n')
    total=0
    reverseCrates = []
    for line in lines[:8]:
        reverseCrates.append(line[1::4])   
    crates = [[reverseCrates[i][j] for i in range(len(reverseCrates)) if len(reverseCrates[i][j].strip()) > 0] for j in range(len(reverseCrates[0]))]

    for line in lines[10:]:
        if(len(line.split(' '))>5):
            num = int(line.split(' ')[1])
            fro = int(line.split(' ')[3])
            to = int(line.split(' ')[5])

            num = min(num, len(crates[fro - 1]))
            crates[to - 1] = crates[fro - 1][:num] + crates[to - 1]
            crates[fro - 1] = crates[fro - 1][num:]
    s=""     
    for crate in crates:
        if len(crate)>0:
            s = s + crate[0]
                      
    return s


# Day 6

def solveDay6A():
    text = getInput(6)
    for i in range(len(text) - 4):
        if len(dict.fromkeys([c for c in text[i:i+4]])) == 4:
            return i+4

def solveDay6B():
    text = getInput(6)
    for i in range(len(text) - 14):
        if len(dict.fromkeys([c for c in text[i:i+14]])) == 14:
            return i+14


# Day 7

def getFolderSize(folder, children, parents, sizesNonRec, sizes):
    if(folder in sizes):
        return sizes[folder]
    if not folder in sizesNonRec:
        size=0
    else:
        size = sizesNonRec[folder]
    if folder in children:
        for child in children[folder]:
            size = size + getFolderSize(child, children, parents, sizesNonRec, sizes)
    sizes[folder]=size
    return size


def solveDay7():
    lines=getInputSplit(7)
    currentFolder= "/"
    children={}
    parents = {}
    sizesNonRec={}
    sizes={}
    for line in lines:
        if line.startswith("$ cd"):
            dest = line.split(' ')[2]
            if dest == '..' and currentFolder in parents:
                currentFolder = parents[currentFolder]
            elif dest=='/':
                currentFolder='/'
            else:
                currentFolder = currentFolder + '/' +dest
        if line.startswith('dir'):
            newDir=currentFolder + '/' + line.split(' ')[1]
            parents[newDir] = currentFolder
            if currentFolder in children:
                children[currentFolder].append(newDir)
            else:
                children[currentFolder]=[newDir]
        elif not line.startswith('$'):
            size = int(line.split(' ')[0])
            if currentFolder in sizesNonRec:
                sizesNonRec[currentFolder] = sizesNonRec[currentFolder] + size
            else:
                sizesNonRec[currentFolder] = size
    getFolderSize('/', children, parents, sizesNonRec, sizes)
    return sum([sizes[f] for f in sizes if sizes[f]<100000]), min([sizes[file] for file in sizes if sizes[file] > sizes['/'] - 40000000 ])


#Day 8

def isTreeVisible(grid,i,j):
    n = len(grid)
    m = len(grid[0])
    grid[i][j] = grid[i][j]-1
    answer = grid[i][j] in (max([grid[i][k] for k in range(j+1)]),
                            max([grid[i][k] for k in range(j,m)]),
                            max([grid[k][j] for k in range(i+1)]),
                            max([grid[k][j] for k in range(i,n)]))
    grid[i][j] = grid[i][j] + 1
    return answer

def scenicScore(grid, i, j):
     n = len(grid)
     m = len(grid[0])
     vn, ve, vw, vs = 0,0,0,0
     for k in range(i-1, -1,-1):
         if grid[k][j] < grid[i][j]:
             vw = vw + 1
         else:
             vw = vw + 1
             break
     for k in range(i+1, n):
         if grid[k][j] < grid[i][j]:
             ve = ve+ 1
         else:
             ve = ve+ 1
             break
     for k in range(j-1, -1,-1):
         if grid[i][k] < grid[i][j]:
             vn = vn+ 1
         else:
             vn = vn+ 1
             break
     for k in range(j+1, m):
         if grid[i][k] < grid[i][j]:
             vs = vs+ 1
         else:
             vs = vs+ 1
             break
     
      
     return (vs*ve*vn*vw)

def solveDay8A():
    lines = getInputSplit(8)
    grid =[[int(c) for c in line] for line in lines]
    return len([(grid,i,j) for i in range(len(grid)) for j in range(len(grid[0])) if isTreeVisible(grid,i,j)])
    
    
def solveDay8B():
    lines = getInputSplit(8)
    grid =[[int(c) for c in line] for line in lines]
    return max([scenicScore(grid,i,j) for i in range(len(grid)) for j in range(len(grid[0]))])


#Day 9

def sign(v):
    return 1 if v > 0 else -1 if v < 0 else 0

def solveDay9A():
    lines = getInputSplit(9)
    headPosition = np.array((0,0))
    tailPosition = np.array((0,0))
    visitedPositions=[(0,0)]
    normDeltaPerDirection = {"U": np.array((0,1)), "D": np.array((0,-1)), "R": np.array((1,0)), "L": np.array((-1,0))}
    for line in lines:
        normDelta = normDeltaPerDirection[line.split(' ')[0]]
        length = int(line.split(' ')[1])
        for i in range(length):
            lastHeadPosition = headPosition
            headPosition = headPosition + normDelta
            ropeDiff = headPosition - tailPosition
            if abs(ropeDiff[0]) + abs(ropeDiff[1]) > 2 or abs(ropeDiff[0]) > 1 or abs(ropeDiff[1]) > 1:
                tailPosition = lastHeadPosition
                visitedPositions.append(tuple(tailPosition))
    return len(dict.fromkeys(visitedPositions))    


def solveDay9B():
    lines = getInputSplit(9)
    knotPositions = [np.array((0,0)) for i in range(10)]
    visitedPositions=[(0,0)]
    normDeltaPerDirection = {"U": np.array((0,1)), "D": np.array((0,-1)), "R": np.array((1,0)), "L": np.array((-1,0))}
    for line in lines:
        normDelta = normDeltaPerDirection[line.split(' ')[0]]
        length = int(line.split(' ')[1])
        for i in range(length):
            lastKnotPosition = knotPositions[0]
            knotPositions[0] = knotPositions[0] + normDelta
            for i in range(len(knotPositions)-1):
                ropeDiff = knotPositions[i] - knotPositions[i+1]
                if abs(ropeDiff[0]) + abs(ropeDiff[1]) > 2 or abs(ropeDiff[0]) > 1 or abs(ropeDiff[1]) > 1:
                    knotPositions[i+1] += np.array((sign(ropeDiff[0]), sign(ropeDiff[1])))
                    if i == len(knotPositions) - 2:
                        visitedPositions.append(tuple(knotPositions[-1]))
                else:
                    break
    return len(dict.fromkeys(visitedPositions))


# Day 10

def solveDay10A():
    lines = getInputSplit(10)
    curInstrIndex = 0
    X = 1
    flaggedInstr = [20 + 40 * i for i in range(6)]
    curFlagInstrIndex = 0
    signal = 0
    for line in lines:
        instr = line.split(' ')[0]
        if instr == "noop":
            curInstrIndex += 1
            if curInstrIndex >= flaggedInstr[curFlagInstrIndex]:
                signal += flaggedInstr[curFlagInstrIndex] * X
                curFlagInstrIndex += 1
        if instr == "addx":
            num = int(line.split(' ')[1])
            curInstrIndex += 2
            if curInstrIndex >= flaggedInstr[curFlagInstrIndex]:
                signal += flaggedInstr[curFlagInstrIndex] * X
                curFlagInstrIndex += 1
            X += num
        if curFlagInstrIndex >= len(flaggedInstr):
            break
    return signal

def solveDay10B():
    output = "\n"
    lines = getInputSplit(10)
    curInstrIndex = 0
    X = 1
    for line in lines:
        instr = line.split(' ')[0]
        if instr == "noop":
            output += "#" if abs(curInstrIndex % 40 - X) <= 1 else "."
            curInstrIndex += 1
            if curInstrIndex % 40 == 0:
                output += "\n"
            
        if instr == "addx":
            num = int(line.split(' ')[1])
            for i in range(2):
                output += "#" if abs(curInstrIndex % 40 - X) <= 1 else "."
                curInstrIndex += 1
                if curInstrIndex % 40 == 0:
                    output += "\n"
            X += num
    return output


#Day 11

class Monkey:
    def __init__(self, parsed):
        self.num = parsed["monkeyNum"]
        self.items = [int(d.strip()) for d in parsed["startingItems"].split(",")]
        self.operation = parsed["operation"]
        self.operand = parsed["operand"]
        self.divisor = parsed["divisor"]
        self.monkeyTrue = parsed["monkeyTrue"]
        self.monkeyFalse = parsed["monkeyFalse"]

    def handleItems(self, monkeys, divide, prod):
        for worry in self.items:
            numOperand = worry if self.operand == "old" else int(self.operand)
            newWorry = worry * numOperand if self.operation == "*" else worry + numOperand
            if divide:
                newWorry = int(newWorry/3)
            else:
                newWorry = int(newWorry % prod)
            newMonkey = self.monkeyTrue if newWorry % self.divisor == 0 else self.monkeyFalse
            monkeys[newMonkey].items.append(newWorry)
        self.items=[]
        
def solveDay11A():
    blocks = getInput(11).strip().split('\n\n')
    monkeys = {}
    for block in blocks:
        parsed = parse("""Monkey {monkeyNum:d}:
  Starting items: {startingItems}
  Operation: new = old {operation} {operand}
  Test: divisible by {divisor:d}
    If true: throw to monkey {monkeyTrue:d}
    If false: throw to monkey {monkeyFalse:d}""", block)
        monkey = Monkey(parsed)
        monkeys[monkey.num] = monkey
    timeCountedItem = {monkeyNum: 0 for monkeyNum in monkeys}
    monkeyNums = list(monkeys.keys())
    monkeyNums.sort()
    for i in range(20):
        for monkeyNum in monkeyNums:
            monkey = monkeys[monkeyNum]
            #print(monkey)
            timeCountedItem[monkey.num] += len(monkey.items)
            monkey.handleItems(monkeys, True, 1)
    listCountedItems = list(timeCountedItem.values())
    listCountedItems.sort()
    return listCountedItems[-1] * listCountedItems[-2]
    
def solveDay11B():
    blocks = getInput(11).strip().split('\n\n')
    monkeys = {}
    prod = 1
    for block in blocks:
        parsed = parse("""Monkey {monkeyNum:d}:
  Starting items: {startingItems}
  Operation: new = old {operation} {operand}
  Test: divisible by {divisor:d}
    If true: throw to monkey {monkeyTrue:d}
    If false: throw to monkey {monkeyFalse:d}""", block)
        monkey = Monkey(parsed)
        monkeys[monkey.num] = monkey
        prod *= monkey.divisor
    timeCountedItem = {monkeyNum: 0 for monkeyNum in monkeys}
    monkeyNums = list(monkeys.keys())
    monkeyNums.sort()
    for i in range(10000):
        for monkeyNum in monkeyNums:
            monkey = monkeys[monkeyNum]
            timeCountedItem[monkey.num] += len(monkey.items)
            monkey.handleItems(monkeys, False, prod)
    listCountedItems = list(timeCountedItem.values())
    listCountedItems.sort()
    return listCountedItems[-1] * listCountedItems[-2]


print("1A:", solveDay1A())
print("1B:", solveDay1B())
print("2A:", solveDay2A())
print("2B:", solveDay2B())
print("3A:", solveDay3A())
print("3B:", solveDay3B())
print("4A:", solveDay4A())
print("4B:", solveDay4B())
print("5A:", solveDay5A())
print("5B:", solveDay5B())
print("6A:", solveDay6A())
print("6B:", solveDay6B())
print("7A:", solveDay7()[0])
print("7B:", solveDay7()[1])
print("8A:", solveDay8A())
print("8B:", solveDay8B())
print("9A:", solveDay9A())
print("9B:", solveDay9B())
print("10A:", solveDay10A())
print("10B:", solveDay10B())
print("11A:", solveDay11A())
print("11B:", solveDay11B())
