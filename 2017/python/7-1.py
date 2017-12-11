import re

class TowerNode:
    def __init__(self, name, weight, childNames):
        self.name = name
        self.weight = weight
        self.childNames = childNames
        self.childNodes = []
        self.parent = None

    def assignChildren(self, nodeDictionary):
        if(self.childNames == None):
            return

        for index in range(0, len(self.childNames)):
            self.childNodes.append(nodeDictionary[self.childNames[index]])
            nodeDictionary[self.childNames[index]].parent = self

    def findRoot(self):
        if self.parent == None:
            return self

        return self.parent.findRoot()

inputFile = open("../inputs/7.txt", "r")
input = inputFile.read()
lines = input.splitlines()

nodeDictionary = {}

for lineIndex in range(0, len(lines)):
    match = re.search('([a-z]*)\s\(([0-9]*)\)(?:\s->\s([a-z,\s]*))?', lines[lineIndex])
    name = match.group(1)
    weight = match.group(2)
    childNames = match.group(3)

    if(childNames != None):
        childNames = childNames.split(", ")

    nodeDictionary[name] = TowerNode(name, weight, childNames)

for name, node in nodeDictionary.items():
    node.assignChildren(nodeDictionary)

rootNode = nodeDictionary.popitem()[1].findRoot()

print(rootNode.name)

