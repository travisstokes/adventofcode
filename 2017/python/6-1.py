input = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]

class BankTreeNode:
    def __init__(self, array, isRoot = False):
        self.branches = {}
        self.isRoot = isRoot
        self.addNode(array)

    def addNode(self, array):
        if self.isRoot:
            array = array[:] # Copy the list if this is root, so this won't be destructive

        if len(array) == 0:
            return

        val = array.pop(0)

        if val in self.branches:
            return self.branches[val].addNode(array)

        self.branches[val] = BankTreeNode(array)

    def subTreeMatches(self, array):
        if self.isRoot:
            array = array[:] # Copy the list if this is root, so this won't be destructive

        if len(array) == 0:
            return True

        if len(array) == 1:
            return array[0] in self.branches

        if array[0] in self.branches:
            val = array.pop(0)
            return self.branches[val].subTreeMatches(array)
        
        return False

rootNode = BankTreeNode(input, True)
isLooping = False
numSteps = 0
numBlocks = len(input)

while not isLooping:
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

    isLooping = rootNode.subTreeMatches(input)
    if(not isLooping):
        rootNode.addNode(input)

print(numSteps)