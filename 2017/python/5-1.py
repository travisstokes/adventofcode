inputFile = open("../inputs/5.txt", "r")
input = inputFile.read()

jumps = list(map(lambda x: int(x), input.splitlines()))

curIndex = 0;
jumpsMade = 0;
while curIndex < len(jumps) and curIndex >= 0:
    jumps[curIndex] = jumps[curIndex] + 1
    curIndex += jumps[curIndex] - 1
    jumpsMade += 1

print(jumpsMade)