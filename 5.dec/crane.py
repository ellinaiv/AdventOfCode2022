

def reorderStacks(filename):


    with open(filename, "r") as f:
        data = f.readlines()


    stacks = []
    instructions = []

    
    
    i = 0
    while i < len(data):
        if "move" in data[i]:
            break
        i += 1
        
    instructions = data[i:]

    stackNums = len(data[i - 2].strip().replace(" ", ""))
    stacksData  = data[:i-2]

    for k in range(1, stackNums + 1):
        indexOfStackElements = list(data[i-2]).index(str(k))
        stack = []
        for line in stacksData:
            stackValue = list(line)[indexOfStackElements]
            if stackValue != " ":
                stack.append(stackValue)
        stacks.append(stack)
        
    print("stacknum: ", len(stacks), " -> ", stacks)
    
    for instruction in instructions:
        instruction = list(instruction.strip().replace("move", "").replace("from", ",").replace("to", ",").replace(" ", "").split(","))
        stackToMoveFrom = (stacks[int(instruction[1]) - 1])
        limit = int(instruction[0])
        
        elementsToMove = stackToMoveFrom[:limit]
        stackToMoveFrom = stackToMoveFrom[limit:]
        stacks[int(instruction[1]) - 1] = stackToMoveFrom
        stacks[int(instruction[2]) - 1] = elementsToMove + stacks[int(instruction[2]) - 1]

    res = ""
    for stack in stacks:
        res += stack[0] if len(stack) != 0 else ""
    print(res)

    
reorderStacks("input.txt")
reorderStacks("inputBasic.txt")
