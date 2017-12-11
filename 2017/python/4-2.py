inputFile = open("../inputs/4.txt", "r")
input = inputFile.read()

lines = input.splitlines()

invalids = 0
for lineIndex in range(0, len(lines)):
    vals = lines[lineIndex].split()
    valDict = {}
    for valIndex in range(0, len(vals)):
        sortedVal = ''.join(sorted(vals[valIndex]))
        if(sortedVal in valDict):
            invalids += 1
            break
        valDict[sortedVal] = 1

print(invalids)
print(len(lines)-invalids)