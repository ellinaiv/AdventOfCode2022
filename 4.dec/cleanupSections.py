
def findOverlap(filename):

    pairs = open(filename, "r")
    fullOverlap = 0

    for pair in pairs:
        pair = pair.strip().split(",")
        firstRange = pair[0].split("-")
        secondRange = pair[1].split("-")

        firstSet = set([i for i in range(int(firstRange[0]),int(firstRange[1]) + 1)])
        secondSet = set([i for i in range(int(secondRange[0]), int(secondRange[1]) + 1)])

        if firstSet & secondSet:
            fullOverlap += 1

    print(fullOverlap)


findOverlap("inputBasic.txt")
findOverlap("input.txt")
