import re

class TowerNode:
    def __init__(self, name, weight, childNames):
        self.name = name
        self.weight = int(weight)
        self.childNames = childNames
        self.childNodes = []
        self.parent = None
        self.totalWeight = None
        self.childrenBalanced = True

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return other != None and self.name == other.name

    def assignChildren(self, nodeDictionary):
        if(self.childNames == None):
            return

        for name in self.childNames:
            self.childNodes.append(nodeDictionary[name])
            nodeDictionary[name].parent = self

    def findRoot(self):
        if self.parent == None:
            return self

        return self.parent.findRoot()

    def allChildrenHaveWeights(self):
        if(len(self.childNodes) == 0):
            return True

        return all(map(lambda x: x.totalWeight, self.childNodes));

    def calculateWeight(self):
        if(self.totalWeight != None):
            return self.totalWeight

        if(len(self.childNodes) > 0):
            weights = list(map(lambda node: int(node.totalWeight), self.childNodes))
            self.childrenBalanced = max(weights) == min(weights)
            self.totalWeight = self.weight + sum(weights)
            return

        self.totalWeight = self.weight

inputFile = open("../inputs/7.txt", "r")
input = inputFile.read()
lines = input.splitlines()

nodeDictionary = {}
leafNodes = set()
for lineIndex in range(0, len(lines)):
    match = re.search('([a-z]*)\s\(([0-9]*)\)(?:\s->\s([a-z,\s]*))?', lines[lineIndex])
    name = match.group(1)
    weight = match.group(2)
    childNames = match.group(3)

    if(childNames != None):
        childNames = childNames.split(", ")

    nodeDictionary[name] = TowerNode(name, weight, childNames)
    if(childNames == None):
        leafNodes.add(nodeDictionary[name])

for name, node in nodeDictionary.items():
    node.assignChildren(nodeDictionary)

parentNodes = set()
unbalancedNode = None
nodesChecked = 0
totalNodes = len(lines)
while(len(leafNodes) > 0 and unbalancedNode == None):
    for node in leafNodes:
        if(not node.allChildrenHaveWeights()):
            parentNodes.add(node) # push this up to the next iteration since it's children aren't done
            continue
        
        nodesChecked += 1
        node.calculateWeight()
        if(not node.childrenBalanced):
            unbalancedNode = node
            break
        
        if(node.parent != None):
            parentNodes.add(node.parent)

    leafNodes = parentNodes
    parentNodes = set()

badNode = None
goodNode = None

for node in unbalancedNode.childNodes:
    if(goodNode == None):
        goodNode = node
        continue

    if(node.totalWeight == goodNode.totalWeight):
        continue

    if(badNode == None):
        badNode = node
        continue

    if(node.totalWeight == badNode.totalWeight):
        badNode = goodNode
        goodNode = node
        break

neededNodeWeight = badNode.weight + (goodNode.totalWeight - badNode.totalWeight)

print(badNode.weight)
print(badNode.totalWeight)
print(goodNode.totalWeight)
print(neededNodeWeight)