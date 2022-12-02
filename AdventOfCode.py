def getInput(day):
    f = open("./input_" + str(day) + ".txt")
    return f.read()

def getInputSplit(day):
    return getInput(day).split('\n')

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

print("1A:", solveDay1A())
print("1B:", solveDay1B())
print("2A:", solveDay2A())
print("2B:", solveDay2B())
