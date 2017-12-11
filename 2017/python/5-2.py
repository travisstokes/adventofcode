inputFile = open("../inputs/5.txt", "r")
input = inputFile.read()

jumps = list(map(lambda x: int(x), input.splitlines()))

curIndex = 0;
jumpsMade = 0;
while curIndex < len(jumps) and curIndex >= 0:
    offset = jumps[curIndex]
    change = 1
    if(offset >= 3):
        change = -1
    jumps[curIndex] += change
    curIndex += offset
    jumpsMade += 1

print(jumpsMade)