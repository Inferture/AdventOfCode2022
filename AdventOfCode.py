#Utilities
from parse import *
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

