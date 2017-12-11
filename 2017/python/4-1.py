inputFile = open("../inputs/4.txt", "r")
input = inputFile.read()

lines = input.splitlines()

invalids = 0
for lineIndex in range(0, len(lines)):
    vals = lines[lineIndex].split()
    valDict = {}
    for valIndex in range(0, len(vals)):
        vals[valIndex]
        if(vals[valIndex] in valDict):
            print(lines[lineIndex])
            invalids += 1
            break
        valDict[vals[valIndex]] = 1

print(invalids)
print(len(lines)-invalids)