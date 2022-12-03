
def findMaxCalories(filename):
    
    caloriesList = open(filename, "r")
    caloriesPerElf = 0
    caloriesTot = []
    
    for caloriesPerItem in caloriesList:
      
        if caloriesPerItem != "\n":
            caloriesPerElf += int(caloriesPerItem)
        else:
            caloriesTot.append(caloriesPerElf)
            caloriesPerElf = 0
    
    caloriesTot.sort()        
    print(sum(caloriesTot[-3:]))    


findMaxCalories("input.txt")
