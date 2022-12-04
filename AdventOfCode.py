#Utilities

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
        if len(line.split(' '))>1:
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
        if len(line.split(' '))>1:
            advPlay = line.split(' ')[0]
            yourPlay = line.split(' ')[1]
            advPoints = 1 if advPlay=="A" else (2 if advPlay == "B" else 3)
            outcomePointsThird = 0 if yourPlay=="X" else (1 if yourPlay == "Y" else 2)
            totalScore = totalScore + 3 * outcomePointsThird + ((advPoints + outcomePointsThird  + 1) % 3 + 1)
    return totalScore

#Day 3

def charValue(c):
    return ord(c)-38 if ord(c)<91 else ord(c) - 96

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
        line1 = line.split(',')[0]
        line2 = line.split(',')[1]
        if ((int(line1.split('-')[0]) <= int(line2.split('-')[0]) and int(line1.split('-')[1]) >= int(line2.split('-')[1]))
        or (int(line1.split('-')[0]) >= int(line2.split('-')[0]) and int(line1.split('-')[1]) <= int(line2.split('-')[1]))):  
            total = total + 1
    return total

def solveDay4B():
    lines = getInputSplit(4)
    total=0
    for line in lines:
        line1 = line.split(',')[0]
        line2 = line.split(',')[1]
        if ((int(line1.split('-')[0]) <= int(line2.split('-')[0]) and int(line1.split('-')[1]) >= int(line2.split('-')[0]))
        or (int(line1.split('-')[0]) >= int(line2.split('-')[0]) and int(line1.split('-')[0]) <= int(line2.split('-')[1]))):  
            total = total + 1
    return total

print("1A:", solveDay1A())
print("1B:", solveDay1B())
print("2A:", solveDay2A())
print("2B:", solveDay2B())
print("3A:", solveDay3A())
print("3B:", solveDay3B())
print("4A:", solveDay4A())
print("4B:", solveDay4B())


