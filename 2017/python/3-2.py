input = 277678
print("Finding first number larger than " + str(input))

class TrackingData:
    def __init__(self):
        self.lastRow = [1]
        self.currentRow = [1,2,4,5,10,11,23,25]
        self.currentValue = 24
        self.rowNumber = 2
        self.rowIndex = 8
        self.rowLength = 8
        self.corners = []

def startNewRow(data):
    print(data.currentRow)
    data.rowNumber += 1
    data.rowIndex = 0
    data.rowLength = (data.rowNumber - 1) * 8
    data.lastRow = data.currentRow
    data.currentRow = [0 for i in range(data.rowLength)]
    data.corners = list(map(lambda x: int(((data.rowLength / 4) * x - 1)), range(1, 5)))

def getLocCalculator(data):
    if data.rowIndex == 0:
        return calcFirst
    elif data.rowIndex in data.corners:
        return calcCorner
    elif data.rowIndex == 1:
        return calcSecond
    elif data.rowIndex + 1 in data.corners:
        return calcPreCorner
    elif data.rowIndex - 1 in data.corners:
        return calcPostCorner
    else:
        return calcSide

def calcFirst(data):
    val = data.lastRow[0]
    if len(data.lastRow) > 1:
        val += data.lastRow[len(data.lastRow) - 1]
    
    return val

def calcSecond(data):
    lenLastRow = len(data.lastRow)
    val = data.lastRow[0] + data.currentRow[0]

    if lenLastRow > 1:
        val += data.lastRow[1]

    if lenLastRow > 2:
        val += data.lastRow[lenLastRow - 1]
    
    return val

def calcCorner(data):
    cornerIndex = int(data.rowIndex - (2 * int(data.rowIndex / (data.rowLength / 4) + 1)))
    if cornerIndex < 0:
        cornerIndex = 0

    standardCorner = data.lastRow[cornerIndex] + data.currentRow[data.rowIndex - 1]

    if(data.rowIndex == data.rowLength - 1):
        standardCorner += data.currentRow[0] # adjust for the final corner having a diagonally adjacent value
    return standardCorner

def calcAdjacentIndex(data):
    return data.rowIndex - int((2 * int(data.rowIndex / (data.rowLength / 4))) + 1)

def calcPreCorner(data):
    adjacent = calcAdjacentIndex(data)

    standardCorner = data.lastRow[adjacent] + data.lastRow[adjacent - 1] + data.currentRow[data.rowIndex - 1]
    if(data.rowIndex == data.rowLength - 2):
        standardCorner += data.currentRow[0] # adjust for the final corner having a diagonally adjacent value
    return standardCorner

def calcPostCorner(data):
    adjacent = calcAdjacentIndex(data)
    return data.lastRow[adjacent + 1] + data.lastRow[adjacent] + data.currentRow[data.rowIndex - 1] + data.currentRow[data.rowIndex - 2]

def calcSide(data):
    adjacent = calcAdjacentIndex(data)
    return data.lastRow[adjacent + 1] + data.lastRow[adjacent] + data.lastRow[adjacent - 1] + data.currentRow[data.rowIndex - 1]

data = TrackingData()

while(data.currentValue < input):
    if(data.rowLength == data.rowIndex):
        startNewRow(data)

    calculator = getLocCalculator(data)
    data.currentValue = calculator(data)
    print(str(calculator) + ": " + str(data.currentValue) + ": " + str(data.rowIndex))
    data.currentRow[data.rowIndex] = data.currentValue
    # Last thing to do
    data.rowIndex += 1

print(data.currentRow)
print("Result: " + str(data.currentValue))