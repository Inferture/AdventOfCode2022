#Utilities

from parse import *
import numpy as np
from numpy.linalg import inv

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


# Day 12

def getNewPoints(heightMap, grid, i, j, v):
    return [(m,n) for (m,n) in [(i+1, j), (i-1,j), (i,j-1), (i,j+1)] if 0<=m<len(grid) \
                  and 0<=n<len(grid[0]) and grid[m][n]> v and heightMap[m][n] <= heightMap[i][j] + 1]

def solveDay12A():
    start = (-1,-1)
    end = (-1,-1)
    lines = getInputSplit(12)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if(lines[i][j]=='E'):
                       end = (i,j)
            if(lines[i][j]=='S'):
                       start = (i,j)
    heightMap = [[charValue(c) for c in line.replace("S", "a").replace("E", "z")] for line in lines]
    distanceGrid = [[float('inf') for c in line] for line in lines]
    distanceGrid[start[0]][start[1]] = 0
    currentDistance = 0
    reachedPoints = [start]
    lastPoints = [start]
    while not end in reachedPoints:
        newPoints = []
        currentDistance += 1
        for (i,j) in lastPoints:
            newPoints = newPoints + getNewPoints(heightMap, distanceGrid, i, j, currentDistance)
        for (m,n) in newPoints:
            distanceGrid[m][n] = currentDistance
        reachedPoints = reachedPoints + newPoints
        lastPoints = list(dict.fromkeys(newPoints))
    return currentDistance
    
def solveDay12B():
    start = (-1,-1)
    end = (-1,-1)
    lines = getInputSplit(12)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if(lines[i][j]=='E'):
                       end = (i,j)
            if(lines[i][j]=='S'):
                       start = (i,j)
    heightMap = [[charValue(c) for c in line.replace("S", "a").replace("E", "z")] for line in lines]
    distanceGrid = [[float('inf') for c in line] for line in lines]
    distanceGrid[start[0]][start[1]] = 0
    currentDistance = 0
    reachedPoints = [(i,j) for i in range(len(heightMap)) for j in range(len(heightMap[0])) if heightMap[i][j] == charValue('a')]
    lastPoints = reachedPoints + []
    while not end in reachedPoints:
        newPoints = []
        currentDistance +=1
        for (i,j) in lastPoints:
            newPoints = newPoints + getNewPoints(heightMap, distanceGrid, i, j, currentDistance)
        for (m,n) in newPoints:
            distanceGrid[m][n] = currentDistance
        reachedPoints = reachedPoints + newPoints
        lastPoints = list(dict.fromkeys(newPoints))
    return currentDistance


# Day 13

def parseList(line):
    currentList=[]
    listsHierarchy=[currentList]
    currentNum = 0
    browsingNumber=False
    for c in line:
        if browsingNumber and (c == ']' or c == ','):
            currentList.append(currentNum)
            currentNum = 0
            browsingNumber=False
        if c == '[':
            newList=[]
            currentList.append(newList)
            currentList = newList
            listsHierarchy.append(newList)
        elif c == ']':
            listsHierarchy = listsHierarchy[:len(listsHierarchy)-1]
            currentList = listsHierarchy[len(listsHierarchy)-1]
        elif c != ',':
            currentNum = currentNum * 10 + int(c)
            browsingNumber=True
    return currentList

def compareLists(list1, list2):
    if(len(list1) == 0 or len(list2) == 0):
        return 0 if len(list1) == len(list2) == 0 else 1 if len(list2) == 0 else -1
    if(type(list1[0]) == int and type(list2[0]) == list):
        list1[0] = [list1[0]]
    if(type(list1[0]) == list and type(list2[0]) == int):
        list2[0] = [list2[0]]
    if(type(list1[0]) == list):
        comp = compareLists(list1[0], list2[0])
        return comp if comp != 0 else compareLists(list1[1:], list2[1:])
    if(type(list1[0]) == int):
        return list1[0] - list2[0] if list1[0] != list2[0] else compareLists(list1[1:], list2[1:])

def solveDay13A():
    blocks = getInput(13).strip().split('\n\n')
    total=0
    for i in range(len(blocks)):
        list1 = parseList(blocks[i].split('\n')[0])
        list2 = parseList(blocks[i].split('\n')[1])
        if(compareLists(list1, list2) <= 0):
            total += i + 1
    return total

def solveDay13B():
    lists = [parseList(line) for line in getInputSplit(13) if len(line.strip())>0]
    index1=1
    index2=2
    for listToSort in lists:
        if(compareLists(listToSort, [[2]]) <= 0):
            index1+=1
            index2+=1
        elif(compareLists(listToSort, [[6]]) <= 0):
            index2+=1
    return index1 * index2


#Day 14

def getGrid14():
    lines = getInputSplit(14)
    minx, maxx, miny, maxy = float('inf'),0,0,0
    for line in lines:
        for s in line.split("->"):
            [x,y] = s.split(',')
            minx, maxx = min(minx, int(x.strip())), max(maxx, int(x.strip()))
            maxy =  max(maxy, int(y.strip()))
    grid = [["." for i in range(minx, maxx + 1)] for j in range(miny, maxy + 1)]
    grid[0][500-minx] = "+"
    for line in lines:
        rockPoints = line.split("->")
        for i in range(len(rockPoints) - 1):
            x0 = int(rockPoints[i].split(',')[0].strip())
            y0 = int(rockPoints[i].split(',')[1].strip())
            x1 = int(rockPoints[i+1].split(',')[0].strip())
            y1 = int(rockPoints[i+1].split(',')[1].strip())
            x0,x1=min(x0,x1),max(x0,x1)
            y0,y1=min(y0,y1),max(y0,y1)
            for y in range(y0, y1+1):
                    for x in range(x0, x1+1):
                        grid[y-miny][x-minx] = "#"
    return grid, minx, maxx, miny, maxy

def solveDay14A():
    grid, minx, maxx, miny, maxy = getGrid14()
    filled = False
    sandGrains=-1
    while not filled:
        sand = (500 - minx,0)
        sandGrains +=1
        falling=True
        while sand[0] in range(0, len(grid[0])) and sand[1] in range(0, len(grid)) and falling:
            if(len(grid)<=sand[1] + 1):
                filled=True
                break
            if(grid[sand[1] + 1][sand[0]] in ('o', '#')):
                if(sand[0] - 1 < 0):
                    filled=True
                    break
                if(grid[sand[1] + 1][sand[0] - 1] in ('o', '#')):
                    if(sand[0] + 1 >= len(grid[0])):
                        filled=True
                        break
                    if(grid[sand[1] + 1][sand[0] + 1] in ('o', '#')):
                        grid[sand[1]][sand[0]]="o"
                        falling=False
                    else:
                        sand = (sand[0] + 1,sand[1] + 1)
                else:
                    sand = (sand[0] - 1,sand[1] + 1)
            else:
                sand = (sand[0],sand[1] + 1)
    return sandGrains

def solveDay14B():
    grid, minx, maxx, miny, maxy = getGrid14()
    newLength = len(grid) + 2
    for i in range(len(grid)):
        grid[i] = newLength * ["."] + grid[i] + newLength * ["."]
    grid.append(['.'] * len(grid[0]))
    grid.append(['#'] * len(grid[0]))
    minx, maxx, miny, maxy =  minx - newLength, maxx + newLength, miny - newLength, maxy + newLength
    filled = False
    sandGrains=0
    while not filled:
        sand = (500 - minx,0)
        sandGrains +=1
        falling=True
        while sand[0] in range(0, len(grid[0])) and sand[1] in range(0, len(grid)) and falling:
            if(len(grid)<=sand[1] + 1):
                filled=True
                break
            if(grid[sand[1] + 1][sand[0]] in ('o', '#')):
                if(sand[0] - 1 < 0):
                    filled=True
                    break
                if(grid[sand[1] + 1][sand[0] - 1] in ('o', '#')):
                    if(sand[0] + 1 >= len(grid[0])):
                        filled=True
                        break
                    if(grid[sand[1] + 1][sand[0] + 1] in ('o', '#')):
                        grid[sand[1]][sand[0]]="o"
                        if(sand == (500 - minx, 0)):
                           filled=True
                        falling=False
                    else:
                        sand = (sand[0] + 1,sand[1] + 1)
                else:
                    sand = (sand[0] - 1,sand[1] + 1)
            else:
                sand = (sand[0],sand[1] + 1)
    return sandGrains


#Day 15

def solveDay15A():
    lines = getInputSplit(15)
    checkY = 2000000
    beaconsAtCheckY = []
    forbiddenSegments = []
    for line in lines:
        parsed = parse("Sensor at x={sx:d}, y={sy:d}: closest beacon is at x={bx:d}, y={by:d}", line)
        sx,sy,bx,by = parsed["sx"], parsed["sy"], parsed["bx"], parsed["by"]
        if by == checkY:
            beaconsAtCheckY.append(bx)
        distance = abs(sx-bx)+abs(sy-by)
        if(abs(sy - checkY) < distance):
            forbiddenSegments.append((sx - distance + abs(sy - checkY), sx + distance - abs(sy - checkY)))
    
    xmin = min([x0 for (x0,x1) in forbiddenSegments])
    xmax = max([x1 for (x0,x1) in forbiddenSegments])
    forbiddenPositionCount = 0
    for x in range(xmin, xmax+1):
        if not x in beaconsAtCheckY:
            for (x0,x1) in forbiddenSegments:
                if(x0<=x<=x1):
                    forbiddenPositionCount += 1
                    break
    return forbiddenPositionCount

def solveDay15B():
    lines = getInputSplit(15)
    checkY = 2000000
    size=20
    size=4_000_000
    candidatesSegments = []
    xmin, xmax, ymin, ymax=0, size, 0, size
    sensorDistances=[]
    beacons =[]
    for line in lines:
        parsed = parse("Sensor at x={sx:d}, y={sy:d}: closest beacon is at x={bx:d}, y={by:d}", line)
        sx,sy,bx,by = parsed["sx"], parsed["sy"], parsed["bx"], parsed["by"]
        distance = abs(sx-bx)+abs(sy-by)
        sensorDistances.append((sx, sy, distance))
        beacons.append((bx,by))
        y0 = sy - distance - 1
        y1 = sy + distance + 1
        x0 = sx - distance - 1
        x1 = sx + distance + 1
        candidatesSegments.append((x0,sy,sx,y0))
        candidatesSegments.append((x0,sy,sx,y1))
        candidatesSegments.append((sx,y0,x1,sy))
        candidatesSegments.append((sx,y1,x1,sy))
        
    for i in range(len(candidatesSegments)):
        c=candidatesSegments[i]
        s= sign((c[0]-c[2])*(c[1] -c[3]))
        for j in range(i+1, len(candidatesSegments)):
            c1=c
            c2=candidatesSegments[j]
            if s != sign((c2[0]-c2[2])*(c2[1] - c2[3])):
                if s<0:
                    c1,c2 =c2,c1
                x = int( (c1[0] + c2[0] + c2[1] - c1[1]) / 2 )
                y = c1[1] + (x - c1[0])
                if max(xmin, c1[0], c2[0]) <= x <= min(xmax, c1[2], c2[2]) and max(ymin, c1[1], c2[3]) <= y <= min(ymax, c1[3], c2[1]):
                    isForbidden = False
                    for sen in sensorDistances:
                        distance = abs(x -sen[0]) + abs(y -sen[1])
                        if distance <= sen[2]:
                            isForbidden = True
                            break
                    if not isForbidden and not (x,y) in beacons:
                        return 4000000 * x + y


#Day 16

def parse16():
    lines = getInputSplit(16)
    rates={}
    connections={}
    for line in lines:
        parsed=parse("Valve {valve} has flow rate={rate:d}; {}valv{} {connections}", line)
        valve=parsed["valve"]
        rate=parsed["rate"]
        links = [link.strip() for link in parsed["connections"].split(',')]
        rates[valve]=rate
        connections[valve]=links
    return rates, connections


def testRoom(room, rates, distances, time, visitedRooms):
    visitedRooms.sort()
    if(time<=1):
        return 0
    potentialNextRooms = [nextRoom for nextRoom in rates if nextRoom not in visitedRooms + [room] and distances[(room, nextRoom)] + 2 < time and rates[nextRoom] > 0]
    return rates[room] * (time - 1) + (0 if len(potentialNextRooms) == 0 else max([testRoom(nextRoom, rates, distances, time - 1 - distances[(room, nextRoom)], visitedRooms + [room]) for nextRoom in potentialNextRooms]))

def testRoomTeamSlow(room1, room2, rates, distances, time1, time2, visitedRooms):
    
    potentialNextRooms1 = [nextRoom for nextRoom in rates if nextRoom not in visitedRooms + [room1, room2] and distances[(room1, nextRoom)] + 2 < time1 and rates[nextRoom] > 0]
    potentialNextRooms2 = [nextRoom for nextRoom in rates if nextRoom not in visitedRooms + [room1, room2] and distances[(room2, nextRoom)] + 2 < time2 and rates[nextRoom] > 0]
    
    if(room1 == "**"):
        return testRoom(room2, rates, distances, time2, visitedRooms)
    if(room2 == "**"):
        return testRoom(room1, rates, distances, time1, visitedRooms)
    gain = rates[room1] * (time1 - 1) + rates[room2] * (time2 - 1)
    if(len(potentialNextRooms1) == len(potentialNextRooms2) == 0):
        return gain
    potentialNextRooms1 += ["**"]
    potentialNextRooms2 += ["**"]
    if(len(potentialNextRooms1) == 0 or len(potentialNextRooms2) == 0):
        potentialNextRooms, room, time = (potentialNextRooms1, room1, time1) if len(potentialNextRooms2) == 0 else (potentialNextRooms2, room2, time2)
        return gain + max([testRoom(nextRoom, rates, distances, time - 1 - distances[(room, nextRoom)], visitedRooms + [room1, room2]) for nextRoom in potentialNextRooms])
    potentialCouples = [(nextRoom1, nextRoom2) for nextRoom1 in potentialNextRooms1 for nextRoom2 in potentialNextRooms2 if nextRoom1 != nextRoom2
                        and ("**" in (nextRoom1, nextRoom2)
                             or not(time1 - 1 - distances[(room1, nextRoom1)] < time2 - 1 - distances[(room2, nextRoom1)]
                                and time2 - 1 - distances[(room2, nextRoom2)] <= time1 - 1 - distances[(room1, nextRoom2)]))]
    couplesToPop=[]
    for i in range(len(potentialCouples)):
        (nextRoom1, nextRoom2) = potentialCouples[i]
        if not "**" in  (nextRoom1, nextRoom2):
            newTime1 = time1 - 1 - distances[(room1, nextRoom1)]
            newTime2 = time2 - 1 - distances[(room2, nextRoom2)]
            newTime21 = time1 - 1 - distances[(room1, nextRoom2)]
            newTime12 = time2 - 1 - distances[(room2, nextRoom1)]
            
            if newTime1 < newTime12 and newTime2 <= newTime21 or newTime1 <= newTime12 and newTime2 < newTime21 or newTime1 == newTime12 and newTime2 == newTime21 and nextRoom1<nextRoom2:
                couplesToPop.append(i)
    for i in couplesToPop[::-1]:
        potentialCouples.pop(i)
    return gain + max([testRoomTeamSlow(nextRoom1, nextRoom2, rates, distances, time1 - 1 - distances[(room1, nextRoom1)], time2 - 1 - distances[(room2, nextRoom2)], visitedRooms + [room1, room2])\
                for nextRoom1, nextRoom2 in potentialCouples])


def solveDay16A():
    rates, connections = parse16()
    distances = {}
    for room in rates:
        reached=[room]
        lastReached = [room]
        currentDistance=0
        while len(lastReached)>0:
            currentDistance+=1
            newlyReached=[]
            for room2 in lastReached:
                for newRoom in connections[room2]:
                    if newRoom not in reached:
                        distances[(room, newRoom)] = currentDistance
                        newlyReached.append(newRoom)
                        reached.append(newRoom)
            lastReached = newlyReached
    return testRoom("AA", rates, distances, 31, [])
    

def solveDay16B():
    rates, connections = parse16()
    distances = {}
    for room in rates:
        reached=[room]
        lastReached = [room]
        currentDistance=0
        while len(lastReached)>0:
            currentDistance+=1
            newlyReached=[]
            for room2 in lastReached:
                for newRoom in connections[room2]:
                    if newRoom not in reached:
                        distances[(room, newRoom)] = currentDistance
                        newlyReached.append(newRoom)
                        reached.append(newRoom)
            lastReached = newlyReached
    
    rates["**"]=0
    for room in rates:
        distances[(room, "**")] = 0
        distances[("**", room)] = 0
    return testRoomTeamSlow("AA", "AA", rates, distances, 27, 27, [])
    #return testRoomTeam("AA", "AA", rates, distances, 27, 27, [], [], 0, 0, {})


#Day 17

def printTerrain(terrain, shape, pos, direction):
    print(pos)
    s=""
    for i in range(len(terrain)-1,-1,-1):
        for j in range(len(terrain[i])):
            s += "#" if terrain[i][j] else "o" if pos[1]<=i<pos[1]+len(shape) and  pos[0]<=j<pos[0]+len(shape[0]) and shape[i - pos[1]][j - pos[0]] else "."
        s+="\n"
    print(s)
    s+="~~~~~~~\n"
    print(direction)
                   
def solveDay17A():
    winds = getInput(17).strip()
    shapeDrawings = ["####", ".#._###_.#.", "..#_..#_###", "#_#_#_#", "##_##"]
    shapes = []
    for shapeDrawing in shapeDrawings:
        shapeDrawingLines = shapeDrawing.split("_")
        shapeLines = [[False for j in range(len(shapeDrawingLines[0]))] for i in range(len(shapeDrawingLines))]
        for i in range(len(shapeDrawingLines)-1,-1, -1):
            for j in range(len(shapeDrawingLines[i])):
                shapeLines[i][j] = shapeDrawingLines[-i-1][j] == "#"
        shapes.append(shapeLines)
    altitude=0
    terrain=[[False for i in range(7)] for j in range(4)]

    shapeCounter=0
    windIndex = 0
    while shapeCounter < 2022:
        shapeStopped=False
        shape = shapes[shapeCounter%len(shapes)]
        pos =  [2, altitude + 3]
        shapeCounter+=1
        while not shapeStopped:
            wind = winds[windIndex%len(winds)]
            windIndex+=1
            delta = 1 if wind == '>' else -1
            collision=False
            if delta > 0 and pos[0] + len(shape[0]) > 6:
                collision=True
            if delta < 0 and pos[0] <= 0:
                collision=True
            for i in range(len(shape)):
                if collision:
                   break
                for j in range(len(shape[i])):
                    if shape[i][j] and  pos[1] + i < len(terrain) and terrain[pos[1] + i][pos[0] + j + delta]:
                        collision=True
                        break
            if not collision:
                pos = [pos[0] + delta, pos[1]]
            
            collision=pos[1]==0
            for i in range(len(shape)):
                if collision:
                   break
                for j in range(len(shape[i])):
                    if shape[i][j] and pos[1] + i - 1< len(terrain) and terrain[pos[1] + i - 1][pos[0] + j]:
                        collision=True
                        break
            if not collision:
                pos = [pos[0], pos[1] - 1]
            else:
                shapeStopped=True
                newAltitude = max(altitude, pos[1] + len(shape))
                if(newAltitude > altitude):
                    terrain += [[False for i in range(7)] for j in range(newAltitude - altitude)]
                altitude = newAltitude
                for i in range(len(shape)):
                    for j in range(len(shape[0])):
                        terrain[pos[1]+i][pos[0]+j] = terrain[pos[1]+i][pos[0]+j] or shape[i][j]
    return altitude

def solveDay17B():
    winds = getInput(17).strip()
    shapeDrawings = ["####", ".#._###_.#.", "..#_..#_###", "#_#_#_#", "##_##"]
    shapes = []
    looped = False
    for shapeDrawing in shapeDrawings:
        shapeDrawingLines = shapeDrawing.split("_")
        shapeLines = [[False for j in range(len(shapeDrawingLines[0]))] for i in range(len(shapeDrawingLines))]
        for i in range(len(shapeDrawingLines)-1,-1, -1):
            for j in range(len(shapeDrawingLines[i])):
                shapeLines[i][j] = shapeDrawingLines[-i-1][j] == "#"
        shapes.append(shapeLines)
    altitude=0
    minAltitude=0
    maximums=[0 for i in range(7)]
    terrain=[[False for i in range(7)] for j in range(4)]

    shapeCounter=0
    windIndex = 0
    terrainAtFirstWind = []
    rocksNumber = 1000000000000
    while shapeCounter < rocksNumber:
        shapeStopped=False
        shape = shapes[shapeCounter%len(shapes)]
        pos =  [2, altitude + 3]
        shapeCounter+=1
        while not shapeStopped:
            wind = winds[windIndex%len(winds)]
            if windIndex % len(winds) == 0 and not looped:
                for i in range(len(terrainAtFirstWind)):
                    if terrain == terrainAtFirstWind[i][0] and pos == terrainAtFirstWind[i][1] and shapeCounter % len(shapes) == terrainAtFirstWind[i][2] % len(shapes):
                        loopLength = shapeCounter - terrainAtFirstWind[i][2]
                        altitudeGain = minAltitude - terrainAtFirstWind[i][3]
                        loopsLeft = (rocksNumber - shapeCounter) // loopLength
                        minAltitude += altitudeGain * loopsLeft
                        shapeCounter += loopsLeft * loopLength
                        looped = True
                terrainAtFirstWind.append(([v + [] for v in terrain], pos + [], shapeCounter, minAltitude))
                
            windIndex+=1
            delta = 1 if wind == '>' else -1
            collision=False
            if delta > 0 and pos[0] + len(shape[0]) > 6:
                collision=True
            if delta < 0 and pos[0] <= 0:
                collision=True
            for i in range(len(shape)):
                if collision:
                   break
                for j in range(len(shape[i])):
                    if shape[i][j] and  pos[1] + i < len(terrain) and terrain[pos[1] + i][pos[0] + j + delta]:
                        collision=True
                        break
            if not collision:
                pos = [pos[0] + delta, pos[1]]
            
            collision=pos[1]==0
            for i in range(len(shape)):
                if collision:
                   break
                for j in range(len(shape[i])):
                    if shape[i][j] and pos[1] + i - 1< len(terrain) and terrain[pos[1] + i - 1][pos[0] + j]:
                        collision=True
                        break
            if not collision:
                pos = [pos[0], pos[1] - 1]
            else:
                shapeStopped=True
                newAltitude = max(altitude, pos[1] + len(shape))
                if(newAltitude > altitude):
                    terrain += [[False for i in range(7)] for j in range(newAltitude - altitude)]
                altitude = newAltitude
                for i in range(len(shape)):
                    for j in range(len(shape[0])):
                        terrain[pos[1]+i][pos[0]+j] = terrain[pos[1]+i][pos[0]+j] or shape[i][j]

                accurate=True#Put to False to significantly reduce time, might give the wrong answer though
                linesToRemove = 0
                if accurate:
                    k = len(terrain)-1
                    reacheableCoords = [(k,j) for j in range(len(terrain[0]))]
                    newCoords = reacheableCoords+[]
                    while len(newCoords)>0:
                        nextCoords=[]
                        for (u,v) in newCoords:
                            nextCoords += [(m,n) for (m,n) in [(u+1,v),(u-1,v),(u,v+1), (u,v-1)] if 0<=m<len(terrain) and 0<=n<len(terrain[0]) and (m,n) not in reacheableCoords and not terrain[m][n]]
                            reacheableCoords = list(dict.fromkeys(reacheableCoords + nextCoords))
                        newCoords = list(dict.fromkeys(nextCoords + []))
                    linesToRemove = min(m for (m,n) in reacheableCoords)
                else:
                    maximums = [ ( 0 if len([terrain[i][j] for i in range(len(terrain)) if terrain[i][j]]) == 0 else max([i for i in range(len(terrain)) if terrain[i][j]])) for j in range(len(terrain[0]))]
                    linesToRemove = min(maximums) - 2 #Decrease further to increase the probability of having the right answer
                
                if linesToRemove>0:
                    terrain = terrain[linesToRemove:]
                    minAltitude+=linesToRemove
                    altitude -= linesToRemove
    return altitude + minAltitude


#Day 18

def solveDay18A():
    lines = getInputSplit(18)
    cubes = []
    for line in lines:
        cubes.append((int(line.split(',')[0]),int(line.split(',')[1]),int(line.split(',')[2])))
    cubes.sort()
    coveredSides=0
    for i in range(len(cubes)):
        for j in range(i+1, len(cubes)):
            ci, cj = cubes[i], cubes[j]
            if(abs(ci[0]-cj[0]) + abs(ci[1]-cj[1]) + abs(ci[2]-cj[2]) == 1):
                coveredSides+=2
    return len(cubes) * 6 - coveredSides

def solveDay18B():
    lines = getInputSplit(18)
    cubes = []
    for line in lines:
        cubes.append((int(line.split(',')[0]),int(line.split(',')[1]),int(line.split(',')[2])))
    cubes.sort()
    bounds =(min([x for (x,y,z) in cubes])-1, min([y for (x,y,z) in cubes])-1, min([z for (x,y,z) in cubes])-1),(max([x for (x,y,z) in cubes])+1,max([y for (x,y,z) in cubes])+1,max([z for (x,y,z) in cubes])+1)
    start = bounds[0]
    newPoints = [start]
    reachedPoints = [start]
    while len(newPoints)>0:
        reachedPoints.sort()
        nextPoints=[]
        for (u,v,w) in newPoints:
            pointsToAdd = [ (x,y,z) for (x,y,z) in [(u+1,v,w),(u-1,v,w),(u,v+1,w),(u,v-1,w),(u,v,w+1),(u,v,w-1)] if (x,y,z) not in reachedPoints and (x,y,z) not in cubes and bounds[0][0]<=x<=bounds[1][0] and bounds[0][1]<=y<=bounds[1][1] and bounds[0][2]<=z<=bounds[1][2]]
            reachedPoints = list(dict.fromkeys(reachedPoints + pointsToAdd))
            nextPoints+=pointsToAdd
        newPoints = list(dict.fromkeys(nextPoints))
    newCubes=[]
    for x in range(bounds[0][0]+1, bounds[1][0]):
        for y in range(bounds[0][1]+1, bounds[1][1]):
            for z in range(bounds[0][2]+1, bounds[1][2]):
                if(x,y,z) not in reachedPoints:
                    newCubes.append((x,y,z))
    coveredSides=0
    for i in range(len(newCubes)):
        for j in range(i+1, len(newCubes)):
            ci, cj = newCubes[i], newCubes[j]
            if(abs(ci[0]-cj[0]) + abs(ci[1]-cj[1]) + abs(ci[2]-cj[2]) == 1):
                coveredSides+=2
    return len(newCubes) * 6 - coveredSides


#Day 19

blueprintsText="""Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

def domComp(a,b):
    aDom = True
    bDom = True
    for i in range(len(a)):
        if a[i]<b[i]:
            aDom = False
        if a[i]>b[i]:
            bDom=False
    return 1 if aDom else -1 if bDom else 0

class Blueprint:
    
    def __init__(self, parsed):
        self.num = parsed["num"]
        self.ore_ore = parsed["ore_ore"]
        self.clay_ore = parsed["clay_ore"]
        self.obsidian_ore = parsed["obsidian_ore"]
        self.obsidian_clay = parsed["obsidian_clay"]
        self.geode_ore = parsed["geode_ore"]
        self.geode_obsidian = parsed["geode_obsidian"]

    def maxGeodes(self, turn):
        ore_bots, clay_bots, obsidian_bots, geode_bots=1,0,0,0
        ore,clay,obsidian,geode=0,0,0,0
        max_geodes=0
        ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = self.ore_ore, self.clay_ore, self.obsidian_ore, self.obsidian_clay, self.geode_ore, self.geode_obsidian
        states = [[(ore,clay,obsidian,geode), (ore_bots, clay_bots, obsidian_bots, geode_bots), (False, False, False, False)]]
        
        maxOre = max(obsidian_ore, clay_ore, geode_ore)
        maxClay = obsidian_clay
        maxObsidian = geode_obsidian
        for i in range(turn):
            nextStates = []
            for state in states:
                
                ore,clay,obsidian,geode = state[0]
                ore_bots, clay_bots, obsidian_bots, geode_bots = state[1]
                alreadyRefused = state[2]
                
                orePossible = ore  >= ore_ore
                clayPossible = ore  >= clay_ore
                obsidianPossible = ore  >= obsidian_ore and clay >= obsidian_clay
                geodePossible = ore  >= geode_ore and obsidian >= geode_obsidian
                
                ore += ore_bots
                clay += clay_bots
                obsidian += obsidian_bots
                geode += geode_bots
                
                if geodePossible and not alreadyRefused[3]:
                    nextStates.append([(ore - geode_ore,clay,obsidian - geode_obsidian,geode), (ore_bots, clay_bots, obsidian_bots, geode_bots + 1), (False, False, False, False)])
                if obsidianPossible and obsidian_bots + obsidian // (turn - i) < maxObsidian and not alreadyRefused[2] :
                    nextStates.append([(ore - obsidian_ore,clay - obsidian_clay,obsidian,geode), (ore_bots, clay_bots, obsidian_bots + 1, geode_bots), (False, False, False, False)])
                if  clayPossible and clay_bots + clay // (turn - i) < maxClay and obsidian_bots + obsidian // (turn - i) < maxObsidian and not alreadyRefused[1]:
                    nextStates.append([(ore - clay_ore,clay,obsidian,geode), (ore_bots, clay_bots + 1, obsidian_bots, geode_bots), (False, False, False, False)])
                if orePossible and ore_bots + ore // (turn - i) < maxOre and not alreadyRefused[0] :
                    nextStates.append([(ore - ore_ore,clay,obsidian,geode), (ore_bots + 1, clay_bots, obsidian_bots, geode_bots), (False, False, False, False)])

                if False in (orePossible, clayPossible, obsidianPossible, geodePossible):
                    nextStates.append([(ore,clay,obsidian,geode), (ore_bots, clay_bots, obsidian_bots, geode_bots), (orePossible, clayPossible, obsidianPossible, geodePossible)])

            states = nextStates + []
        
        return max([end_geode for ((end_ore,end_clay,end_obsidian,end_geode), bots, refused) in states])
    
def solveDay19A():
    lines = blueprintsText.split('\n')
    lines = getInputSplit(19)
    blueprints = []
    for line in lines:
        parsed = parse("Blueprint {num:d}: Each ore robot costs {ore_ore:d} ore. Each clay robot costs {clay_ore:d} ore. Each obsidian robot costs {obsidian_ore:d} ore and {obsidian_clay:d} clay. Each geode robot costs {geode_ore:d} ore and {geode_obsidian:d} obsidian.", line)
        blueprints.append(Blueprint(parsed))
    s=0
    return sum([blueprint.num * blueprint.maxGeodes(24) for blueprint in blueprints])


def solveDay19B():
    lines = blueprintsText.split('\n')
    lines = getInputSplit(19)
    blueprints = []
    for line in lines:
        parsed = parse("Blueprint {num:d}: Each ore robot costs {ore_ore:d} ore. Each clay robot costs {clay_ore:d} ore. Each obsidian robot costs {obsidian_ore:d} ore and {obsidian_clay:d} clay. Each geode robot costs {geode_ore:d} ore and {geode_obsidian:d} obsidian.", line)
        blueprints.append(Blueprint(parsed))
    s=0
    return blueprints[0].maxGeodes(32) * blueprints[1].maxGeodes(32) * blueprints[2].maxGeodes(32)


# Day 20

def getInRange(n, length):
    k = n
    if n < 0:  
        k=((abs(n) // (length - 1) + 2) * (length-1)+n) % (length - 1)
    elif n>=length:
        k = (n-1) % (length -1) + 1
    return k

def simpleRange(a,b,length):
    a,b=min(a,b),max(a,b)
    r=[i for i in range(a,b)]
    for i in range(len(r)): 
        r[i]=getInRange(r[i], length)
    return r

def solveDay20A():
    lines = getInputSplit(20)
    file = []
    length = len(lines)
    order = [ i for i in range(len(lines))]
    invOrder = [i for i in range(len(lines))]
    pos0=0
    for i in range(len(lines)):        
        file.append(int(lines[i]))
        if(file[i]==0):
            pos0=i
    for i in range(len(lines)):
        pos = order[i]
        move = file[i]
        newPos = getInRange(pos + move, length)
        v = (pos, newPos)
        delta = 1 if newPos < pos else -1
        for j in range(min(v), max(v) + 1):
            if invOrder[j] != i:
                order[invOrder[j]] +=delta
        order[i] = newPos
        
        newInvOrder = invOrder + []
        for j in range(min(v), max(v) + 1):
            if newInvOrder[j] != i:
                invOrder[order[newInvOrder[j]]] = newInvOrder[j]
        invOrder[order[i]] = i
            
    encryptedFile = [file[invOrder[i]] for i in range(length)]
    startPos = order[pos0]
    return sum([encryptedFile[(startPos + 1000 * i) % length] for i in range(1,4)])

def solveDay20B():
    lines = getInputSplit(20)
    file = []
    length = len(lines)
    order = [ i for i in range(len(lines))]
    invOrder = [i for i in range(len(lines))]
    pos0=0
    for i in range(len(lines)):        
        file.append(811589153 * int(lines[i]))
        if(file[i]==0):
            pos0=i
    for t in range(10):
        for i in range(len(lines)):
            pos = order[i]
            move = file[i]
            newPos = getInRange(pos + move, length)
            v = (pos, newPos)
            delta = 1 if newPos < pos else -1
            for j in range(min(v), max(v) + 1):
                if invOrder[j] != i:
                    order[invOrder[j]] +=delta
            order[i] = newPos
            
            newInvOrder = invOrder + []
            for j in range(min(v), max(v) + 1):
                if newInvOrder[j] != i:
                    invOrder[order[newInvOrder[j]]] = newInvOrder[j]
            invOrder[order[i]] = i

    encryptedFile = [file[invOrder[i]] for i in range(length)]
    startPos = order[pos0]
    return sum([encryptedFile[(startPos + 1000 * i) % length] for i in range(1,4)])


#Day 21

def addToDictList(dict, key, x):
    if key in dict:
        dict[key].append(x)
    else:
        dict[key]=[x]
        
def calc(m,n,op):
    return (m + n) if op == '+' else (m-n) if op == '-' else (m*n) if op == '*' else m//n

def solveDay21A():
    values={}
    clients = {}
    lines = getInputSplit(21)
    for line in lines:
        s0=line.strip().split(':')
        s = s0[1].strip().split(' ')
        result = None
        id=s0[0]
        if len(s)>1:
            m,n=None,None
            op = s[1]
            waiting = [s0[0]] + s
            if s[0] in values:
                m=values[s[0]]
            else :
                addToDictList(clients, s[0], waiting)
            if s[2] in values:
                n=values[s[2]]
            else:
                addToDictList(clients, s[2], waiting)
            if m != None and n != None:
                result = calc(m,n,op)
        else:
            result = int(s[0])
            
            
        if result != None:
            values[id]=result
            lastMonkeys=[id]
            while len(lastMonkeys)>0:
                newMonkeys=[]
                for monkey in lastMonkeys:
                    if monkey in clients:
                        for waiting in clients[monkey]:
                            k1, k2= waiting[1], waiting[3]
                            if k1 in values and k2 in values:
                                v = calc(values[k1], values[k2], waiting[2])
                                values[waiting[0]]=v
                                newMonkeys.append(waiting[0])
                lastMonkeys=newMonkeys + []
                
    return values['root']
    
def invOp(op):
    return '+' if op == '-' else '-' if op =='+' else '/' if op == '*' else '*'

def solveDay21B():
    values={}
    clients = {}
    revClients ={}
    lines = getInputSplit(21)
    rootEquals =(None,None)
    for line in lines:
        s0=line.strip().split(':')
        s = s0[1].strip().split(' ')
        result = None
        id=s0[0]
        if id == 'humn':
            continue
        if id == 'root':
            rootEquals=(s[0], s[2])
        if len(s)>1:
            m,n=None,None
            op = s[1]
            
            waiting = [s0[0]] + s
            wait1 = [s[0], id, invOp(op), s[2]]
            wait2 = [s[2], id, invOp(op), s[0]] if op in ('+', '*') else [s[2], s[0], op, id]
            if s[0] in values:
                m=values[s[0]]
            else :
                addToDictList(clients, s[0], waiting)
                addToDictList(revClients, s0[0], wait1)
                addToDictList(revClients, s[2], wait1)
            if s[2] in values:
                n=values[s[2]]
            else:
                addToDictList(clients, s[2], waiting)
                addToDictList(revClients, s0[0], wait2)
                addToDictList(revClients, s[0], wait2)
            if m != None and n != None:
                result = calc(m,n,op)
        else:
            result = int(s[0])
            
        if result != None:
            values[id]=result
            lastMonkeys=[id]
            while len(lastMonkeys)>0:
                newMonkeys=[]
                for monkey in lastMonkeys:
                    if monkey in clients:
                        for waiting in clients[monkey]:
                            k1, k2= waiting[1], waiting[3]
                            if k1 in values and k2 in values:
                                v = calc(values[k1], values[k2], waiting[2])
                                values[waiting[0]]=v
                                newMonkeys.append(waiting[0])
                lastMonkeys=newMonkeys + []
    
    lastMonkeys=[]
    if rootEquals[0] in values:
        values[rootEquals[1]] = values[rootEquals[0]]
        lastMonkeys.append(rootEquals[1])
    elif rootEquals[1] in values:
        values[rootEquals[0]] = values[rootEquals[1]]
        lastMonkeys.append(rootEquals[0])
    
    while len(lastMonkeys)>0:
        newMonkeys=[]
        for monkey in lastMonkeys:
            if monkey in revClients:
                for waiting in revClients[monkey]:
                    if waiting[0] not in values:
                        k1, k2= waiting[1], waiting[3]
                        if k1 in values and k2 in values:
                            v = calc(values[k1], values[k2], waiting[2])
                            values[waiting[0]]=v
                            newMonkeys.append(waiting[0])
        lastMonkeys=newMonkeys + []
        
    return values['humn']


#Day 22

def solveDay22A():
    lines = getInput(22).rstrip().split('\n')
    
    width = max([len(line) for line in lines[:len(lines)-2]])
    for i in range(len(lines) - 2):
        lines[i] = lines[i] + (width - len(lines[i])) * ' '
    start = [0, min([i for i in range(len(lines[0]))  if lines[0][i] == '.'])]
    dirs=[(0,1), (1,0), (0,-1), (-1,0)]
    path = lines[len(lines)-1]
    ranges = [int(r) for r in path.strip().replace('R','L').split('L')]
    turns = [s for s in path if s in "RL"]
    curDir=0
    terrain = [[c for c in line] for line in lines[0:len(lines)-2]]
    pos = start
    for i in range(len(ranges)):
        nextPos=pos+[]
        dir = dirs[curDir]
        for j in range(ranges[i]):
            moved=False
            while(not moved or terrain[nextPos[0]][nextPos[1]] == ' '):
                moved = True
                nextPos=[(nextPos[0] + dir[0] + len(terrain)) % len(terrain), (nextPos[1] + dir[1] + len(terrain[0]))  % len(terrain[0])]
            if terrain[nextPos[0]][nextPos[1]] == '#':
                break
            else:
                pos = nextPos+[]
        if i < len(turns):
            curDir = (curDir +( 1 if turns[i] == 'R' else -1)) % len(dirs)
            lastDir = curDir
    return (curDir) + 1000 * (pos[0] + 1) + 4 * (pos[1] +1)


def getFace(vec):
    face = 3 if vec[0]<0 else 6 if vec[0]>0 else 2 if vec[1]<0 else 4 if vec[1] > 0 else 5 if vec[2] > 0 else 1
    return face-1

def solveDay22B():
    #1:facing, 2:top, 3:left, 4:bottom, 5:behind, 6:right
    lines = getInput(22).rstrip().split('\n')
    width = max([len(line) for line in lines[:len(lines)-2]])
    area = 0
    for i in range(len(lines) - 2):
        lines[i] = lines[i] + (width - len(lines[i])) * ' '
        area += len([c for c in lines[i] if c != ' '])
    
    side = int((area//6)**0.5)
    start = [0, min([i for i in range(len(lines[0]))  if lines[0][i] == '.'])]
    dirs=[(0,1), (1,0), (0,-1), (-1,0)]
    dirsIndex = {(0,1): 0, (1,0):1, (0,-1):2, (-1,0):3}
    path = lines[len(lines)-1]
    ranges = [int(r) for r in path.strip().replace('R','L').split('L')]
    turns = [s for s in path if s in "RL"]
    curDir=0
    terrain = [[c for c in line] for line in lines[0:len(lines)-2]]
    pos = start
    lastDir = curDir

    oneMat = np.array([[1,0,0], [0,1,0],[0,0,1]])
    upMat = np.array([[1,0,0], [0,0,-1],[0,1,0]])
    downMat = np.array([[1,0,0], [0,0,1],[0,-1,0]])
    leftMat = np.array([[0,0,-1], [0,1,0],[1,0,0]])
    rightMat = np.array([[0,0,1], [0,1,0],[-1,0,0]])

    faces = [(start[1] // side, start[0]//side)] + [None] * 5
    matrixes = [oneMat] + [None] * 5
    baseInvRotationMatrixes = [oneMat, downMat, rightMat, upMat, rightMat.dot(rightMat), leftMat]
    newFaces = [0]
    while(len(newFaces) > 0):
        nextFaces = []
        for faceIndex in newFaces:
            left = np.array([-1,0,0]).dot(matrixes[faceIndex])
            leftIndex = getFace(left)
            if faces[leftIndex] == None:
                x = (faces[faceIndex][0] - 1) * side
                y = (faces[faceIndex][1]) * side
                if 0<=x<len(terrain[0]) and terrain[y][x] in ".#":
                    faces[leftIndex] = (x // side, y // side)
                    matrixes[leftIndex] =leftMat.dot(matrixes[faceIndex])
                    nextFaces.append(leftIndex)
            
            right = np.array([1,0,0]).dot(matrixes[faceIndex])
            rightIndex = getFace(right)
            if faces[rightIndex] == None:
                x = (faces[faceIndex][0] + 1) * side
                y = faces[faceIndex][1] * side
                if 0<=x<len(terrain[0]) and terrain[y][x] in ".#":
                    faces[rightIndex] = (x // side, y // side)
                    matrixes[rightIndex] = rightMat.dot(matrixes[faceIndex])
                    nextFaces.append(rightIndex)

            up = np.array([0,-1,0]).dot(matrixes[faceIndex])
            upIndex = getFace(up)
            if faces[upIndex] == None:
                x = (faces[faceIndex][0]) * side
                y = (faces[faceIndex][1] - 1) * side
                if 0<=y<len(terrain) and terrain[y][x] in ".#":
                    faces[upIndex] = (x // side, y // side)
                    matrixes[upIndex] = upMat.dot(matrixes[faceIndex])
                    nextFaces.append(upIndex)

            down = np.array([0,1,0]).dot(matrixes[faceIndex])
            downIndex = getFace(down)
            if faces[downIndex] == None:
                x = (faces[faceIndex][0]) * side
                y = (faces[faceIndex][1] + 1) * side
                if 0<=y<len(terrain) and terrain[y][x] in ".#":
                    faces[downIndex] = (x // side, y // side)
                    matrixes[downIndex] = downMat.dot(matrixes[faceIndex])
                    nextFaces.append(downIndex)
                    
        newFaces = nextFaces + []
            
    invMatrixes = []
    for m in matrixes:
        invMatrixes.append(inv(m))

    #Path
    for i in range(len(ranges)):
        nextPos=pos+[]
        for j in range(ranges[i]):
            y,x = pos
            currentFace=-99
            for k in range(len(faces)):
                if(faces[k] == (x//side,y//side)):
                    currentFace=k
            dir = dirs[curDir]
            nextPos=[(pos[0] + dir[0]), (pos[1] + dir[1])]
            
            if nextPos[1] // side != x // side or nextPos[0] // side != y // side:
                #Face change
                centerSide = (side-1)/2
                facePos = [[0,0,-1],[0,-1,0],[-1,0,0],[0,1,0],[0, 0, 1],[1,0,0]]
                vec = np.array([dir[1], dir[0], 0]).dot(matrixes[currentFace])
                newFace = getFace(vec)
                centeredPos = np.array([x % side, y % side, 0]) - np.array([(side-1)/2, (side-1)/2, 0])
                
                currentFacePos = centeredPos.dot(matrixes[currentFace])  + centerSide * np.array(facePos[currentFace])
                newFacePos = currentFacePos.dot(invMatrixes[newFace])
                
                dirToFace = -np.array(facePos[currentFace]).dot(invMatrixes[newFace])
                
                nextPos = [int(faces[newFace][1] * side + newFacePos[1] + (side-1)/2), int(faces[newFace][0] * side + newFacePos[0] + (side-1)/2) ]
                curDir = dirsIndex[(dirToFace[1], dirToFace[0])]
                
            if terrain[nextPos[0]][nextPos[1]] == '#':
                curDir = lastDir
                break
            else:
                pos = nextPos+[]
                lastDir =  curDir
        if i < len(turns):
            curDir = (lastDir +( 1 if turns[i] == 'R' else -1) + len(dirs)) % len(dirs)
            lastDir = curDir
            
    return (lastDir) + 1000 * (pos[0] + 1) + 4 * (pos[1] +1)
    
    
#Day 23

def print_terrain(elves):
    minX, maxX, minY, maxY = min([x for (x,y) in elves]), max([x for (x,y) in elves]), min([y for (x,y) in elves]), max([y for (x,y) in elves])
    for y in range(minY, maxY+1):
        s=""
        for x in range(minX, maxX +1):
            if (x,y) in elves:
                s+="#"
            else:
                s+="."
        print(s)
    print('\n')

def solveDay23A():
    lines = getInputSplit(23)
    terrain = [[c == '#' for c in line] for line in lines]
    elves = [(x,y) for y in range(len(terrain)) for x in range(len(terrain[0])) if terrain[y][x]]
    dirs = ( (0,-1),(0,1),(-1,0),(1,0))
    curDirStart = 0
    for turn in range(10):
        claimedSpots = {}
        for j in range(len(elves)):
            elf = elves[j]
            adjElf=False
            for elf2 in elves:
                if max(abs(elf[0]-elf2[0]), abs(elf[1] - elf2[1])) == 1:
                    adjElf = True
                    break
                
            if adjElf:
                for i in list(range(curDirStart, len(dirs))) + list(range(0,curDirStart)):
                    dir = dirs[i]
                    spot = (elf[0] + dir[0], elf[1] + dir[1])
                    if spot not in elves:
                        if dir[0] == 0 and (elf[0] + 1, elf[1] + dir[1]) not in elves and (elf[0] - 1, elf[1] + dir[1]) not in elves or \
                        dir[1] == 0 and (elf[0] + dir[0], elf[1] + 1) not in elves and (elf[0] + dir[0], elf[1] - 1) not in elves:
                            if spot in claimedSpots:
                                claimedSpots[spot] = None
                            else:
                                claimedSpots[spot] = j
                            break
                        
        for spot in claimedSpots:
            if claimedSpots[spot] != None:
                elves[claimedSpots[spot]] = spot
        curDirStart = (curDirStart + 1) % len(dirs)
    minX, maxX, minY, maxY = min([x for (x,y) in elves]), max([x for (x,y) in elves]), min([y for (x,y) in elves]), max([y for (x,y) in elves])
    return (maxX - minX + 1) * (maxY - minY + 1) - len(elves)
        

def solveDay23B():
    lines = getInputSplit(23)
    terrain = [[c == '#' for c in line] for line in lines]
    elves = [(x,y) for y in range(len(terrain)) for x in range(len(terrain[0])) if terrain[y][x]]
    dirs = ( (0,-1),(0,1),(-1,0),(1,0))
    curDirStart = 0
    turn = 0
    while True:
        turn +=1
        claimedSpots = {}
        for j in range(len(elves)):
            elf = elves[j]
            adjElf=False
            for elf2 in elves:
                if max(abs(elf[0]-elf2[0]), abs(elf[1] - elf2[1])) == 1:
                    adjElf = True
                    break
            if adjElf:
                for i in list(range(curDirStart, len(dirs))) + list(range(0,curDirStart)):
                    dir = dirs[i]
                    spot = (elf[0] + dir[0], elf[1] + dir[1])
                    if spot not in elves:
                        if dir[0] == 0 and (elf[0] + 1, elf[1] + dir[1]) not in elves and (elf[0] - 1, elf[1] + dir[1]) not in elves or \
                        dir[1] == 0 and (elf[0] + dir[0], elf[1] + 1) not in elves and (elf[0] + dir[0], elf[1] - 1) not in elves:
                            if spot in claimedSpots:
                                claimedSpots[spot] = None
                            else:
                                claimedSpots[spot] = j
                            break
        moved = False 
        for spot in claimedSpots:
            if claimedSpots[spot] != None:
                elves[claimedSpots[spot]] = spot
                moved = True
        if not moved:
            return turn
            
        curDirStart = (curDirStart + 1) % len(dirs)


# Day 24

def solveDay24A():
    lines = getInputSplit(24)
    terrain = [[c for c in line] for line in lines]
    start = (0,0)
    end = (len(terrain)-1, 0)
    for i in range(len(terrain[0])):
        if terrain[0][i] == '.':
            start = (0, i)
        if terrain[len(terrain)-1][i]=='.':
            end = (len(terrain) - 1, i)
    blizzards = []
    blizzardsDirs = []
    for i in range(len(terrain)):
        for j in range(len(terrain[i])):
            c = terrain[i][j]
            if c in "v^<>":
                delta = (1,0) if c == 'v' else (-1,0) if c == '^' else (0,-1) if c == '<' else (0,1)
                blizzards.append([i,j])
                blizzardsDirs.append(delta)
    pos = (start[0], start[1])
    turns = 0
    possiblePos = [pos]
    while len(possiblePos)>0:
        
        turns +=1
        for i in range(len(blizzards)):
            moved=False
            while not (moved and 0 <= blizzards[i][0] < len(terrain) and 0<=blizzards[i][1] < len(terrain[0]) and terrain[blizzards[i][0]][blizzards[i][1]] != '#'):
                blizzards[i] = [(blizzards[i][0] + len(terrain) + blizzardsDirs[i][0]) % len(terrain), (blizzards[i][1] + blizzardsDirs[i][1] + len(terrain[0])) % len(terrain[0])]
                moved=True
        newPossiblePos =[]
        for p in possiblePos:
            newPossiblePos += [newPos for newPos in (p, (p[0] + 1, p[1]), (p[0] - 1, p[1]),(p[0], p[1] - 1),(p[0], p[1] + 1)) if newPos[0]>=0 and newPos[0] < len(terrain) and newPos[1]>=0 and newPos[1]<len(terrain[0]) and terrain[newPos[0]][newPos[1]] != '#' and not list(newPos) in blizzards]
        if end in newPossiblePos:
            return turns
        else:
            possiblePos = list(dict.fromkeys(newPossiblePos))


def solveDay24B():
    lines = getInputSplit(24)
    terrain = [[c for c in line] for line in lines]
    start = (0,0)
    end = (len(terrain)-1, 0)
    for i in range(len(terrain[0])):
        if terrain[0][i] == '.':
            start = (0, i)
        if terrain[len(terrain)-1][i]=='.':
            end = (len(terrain) - 1, i)
    blizzards = []
    blizzardsDirs = []
    for i in range(len(terrain)):
        for j in range(len(terrain[i])):
            c = terrain[i][j]
            if c in "v^<>":
                delta = (1,0) if c == 'v' else (-1,0) if c == '^' else (0,-1) if c == '<' else (0,1)
                blizzards.append([i,j])
                blizzardsDirs.append(delta)
    pos = (start[0], start[1])
    turns = 0
    possiblePos = [pos]
    steps = (end, start, end)
    stepIndex = 0
    while len(possiblePos)>0:
        turns +=1
        for i in range(len(blizzards)):
            moved=False
            while not (moved and 0 <= blizzards[i][0] < len(terrain) and 0<=blizzards[i][1] < len(terrain[0]) and terrain[blizzards[i][0]][blizzards[i][1]] != '#'):
                blizzards[i] = [(blizzards[i][0] + len(terrain) + blizzardsDirs[i][0]) % len(terrain), (blizzards[i][1] + blizzardsDirs[i][1] + len(terrain[0])) % len(terrain[0])]
                moved=True
        newPossiblePos =[]
        for p in possiblePos:
            newPossiblePos += [newPos for newPos in (p, (p[0] + 1, p[1]), (p[0] - 1, p[1]),(p[0], p[1] - 1),(p[0], p[1] + 1)) if newPos[0]>=0 and newPos[0] < len(terrain) and newPos[1]>=0 and newPos[1]<len(terrain[0]) and terrain[newPos[0]][newPos[1]] != '#' and not list(newPos) in blizzards]
        if steps[stepIndex] in newPossiblePos:
            stepIndex+=1
            if stepIndex>=len(steps):
                return turns
            
            possiblePos = [steps[stepIndex - 1]]
        else:
            possiblePos = list(dict.fromkeys(newPossiblePos))


#Day 25

def snafuToDecimal(s):
    decs = {'=':-2, '-':-1,'0':0, '1':1, '2':2}
    num=0
    for i in range(len(s[::-1])):
        num += decs[s[i]] * 5 ** (len(s)- 1 - i)
    return num
        
def decimalToSnafu(n):
    decs = ['0', '1', '2', '=', '-']
    powerMax = 0
    s=""
    m = n
    while(5 ** powerMax < n):
        powerMax+=1
    powerMax+=1
    for i in range(powerMax):
        k = m % (5 ** (i + 1)) // (5**i)
        if k >=3:
            m += 5 ** (i + 1)
        s = decs[k] + s
    if(s[0] == '0'):
        s=s[1:]
    return s


def solveDay25():
    inputs = getInputSplit(25)
    totalFuel=0
    for s in inputs:
        totalFuel += snafuToDecimal(s)
    totalFuelSnafu = decimalToSnafu(totalFuel)
    return totalFuelSnafu



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
print("12A:", solveDay12A())
print("12B:", solveDay12B())
print("13A:", solveDay13A())
print("13B:", solveDay13B())
print("14A:", solveDay14A())
print("14B:", solveDay14B())
print("15A:", solveDay15A())
print("15B:", solveDay15B())
print("16A:", solveDay16A())
#print("16B:", solveDay16B()) #Warning: extremely slow
print("17A:", solveDay17A())
print("17B:", solveDay17B())
print("18A:", solveDay18A())
print("18B:", solveDay18B())
print("19A:", solveDay19A())
print("19B:", solveDay19B())
print("20A:", solveDay20A())
print("20B:", solveDay20B())
print("21A:", solveDay21A())
print("21B:", solveDay21B())
print('22A:', solveDay22A())
print('22B:', solveDay22B())
print('23A:', solveDay23A())
#print('23B:', solveDay23B()) #Warning: extremely slow
print('24A:', solveDay24A())
print('24B:', solveDay24B())
print('25:', solveDay25())
