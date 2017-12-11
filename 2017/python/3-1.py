input = 277678
print("Finding location of input " + str(input))

print("Finding square")
square = 1

while square*square < input:
    square += 1

brVal = square * square

print("Square: " + str(square))
print("Bottom Right: " + str(brVal))

centerAdjust = ((square - 1) / 2)

centers = [4];
currCenter = brVal - centerAdjust;
minCenterSteps = abs(currCenter - input); 
for index in range(1, 3):
    currCenter = currCenter - (centerAdjust*2)
    currSteps = abs(currCenter - input)
    if currSteps < minCenterSteps:
        minCenterSteps = currSteps

steps = minCenterSteps + ((square - 1) / 2)
print("Total Steps: " + str(steps))