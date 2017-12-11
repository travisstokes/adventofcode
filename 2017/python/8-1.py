import re

class Processor:
    
    #comparators
    comparators = {
        '<': lambda l, r: l < r,
        '>': lambda l, r: l > r,
        '==': lambda l, r: l == r,
        '!=': lambda l, r: l != r,
        '<=': lambda l, r: l <= r,
        '>=': lambda l, r: l >= r
    }

    #operators
    operators = {
        'inc': lambda l,r: l + r,
        'dec': lambda l,r: l - r
    }

    def __init__(self):
        self.registers = {}

    def getRegisterValue(self, name):
        if name not in self.registers:
            self.registers[name] = 0

        return self.registers[name]

    def execCommand(self, targetRegisterName, operator, opValue, compareRegisterName, compareOperator, compareValue):
        compareRegisterValue = self.getRegisterValue(compareRegisterName)
        if(self.comparators[compareOperator](compareRegisterValue, compareValue)):
            targetRegisterValue = self.getRegisterValue(targetRegisterName)
            self.registers[targetRegisterName] = self.operators[operator](targetRegisterValue, opValue)

    def executeLine(self, line):
        print(line)
        match = re.search('([a-z]*)\s(inc|dec)\s([-]?[0-9]*)\sif\s([a-z]*)\s([!<>=]*)\s([-]?[0-9]*)', line)
        targetRegisterName = match.group(1)
        operator = match.group(2)
        opValue = int(match.group(3))
        compareRegisterName = match.group(4)
        compareOperator = match.group(5)
        compareValue = int(match.group(6))

        self.execCommand(targetRegisterName, operator, opValue, compareRegisterName, compareOperator, compareValue)

inputFile = open("../inputs/8.txt", "r")
input = inputFile.read()
lines = input.splitlines()

processor = Processor()

for lineIndex in range(0, len(lines)):
    processor.executeLine(lines[lineIndex])

maxValue = max(list(processor.registers.values()))

print(maxValue)