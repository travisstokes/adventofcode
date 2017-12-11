input = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]

class BankTreeNode:
    def __init__(self, array, isRoot = False, firstSeen = 0):
        self.branches = {}
        self.isRoot = isRoot
        self.firstSeen = firstSeen
        self.addNode(array, firstSeen)

    def addNode(self, array, firstSeen):
        if self.isRoot:
            array = array[:] # Copy the list if this is root, so this won't be destructive

        if len(array) == 0:
            return

        val = array.pop(0)

        if val in self.branches:
            return self.branches[val].addNode(array, firstSeen = firstSeen)

        self.branches[val] = BankTreeNode(array, isRoot = False, firstSeen = firstSeen)

    def findSubTree(self, array):
        if self.isRoot:
            array = array[:] # Copy the list if this is root, so this won't be destructive

        if len(array) == 0:
            return self
        
        if len(array) == 1 and array[0] in self.branches:
            return self.branches[array[0]]
        elif array[0] in self.branches:
            val = array.pop(0)
            return self.branches[val].findSubTree(array)
        
        return None

rootNode = BankTreeNode(input, isRoot=True, firstSeen=0)
numSteps = 0
numBlocks = len(input)
match = None

while match == None:
    numSteps += 1
    maxVal = max(input)
    maxIndex = input.index(maxVal)
    input[maxIndex] = 0
    while maxVal > 0:
        maxIndex += 1
        if(maxIndex >= numBlocks):
            maxIndex = 0

        input[maxIndex] += 1
        maxVal -= 1

    match = rootNode.findSubTree(input)
    if(match == None):
        rootNode.addNode(input, numSteps)

print("Number of Steps: " + str(numSteps))
print("Match first seen at: " + str(match.firstSeen))
print("Steps til repetition: " + str(numSteps - match.firstSeen))