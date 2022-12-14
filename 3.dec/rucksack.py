

def findPriorities(filename):

    with open(filename, "r") as f:
        data = f.readlines()
    sumPriorities = 0
    alphaCodes = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    i = 0
    while i < len(data):
        rucksack1 = set(data[i].strip())
        rucksack2 = set(data[i+1].strip())
        rucksack3 = set(data[i+2].strip())
        intersection = rucksack1 & rucksack2 & rucksack3
        sumPriorities += alphaCodes.index(intersection.pop()) + 1
        i = i + 3
    print(sumPriorities)


findPriorities("inputBasic.txt")
findPriorities("input.txt")
