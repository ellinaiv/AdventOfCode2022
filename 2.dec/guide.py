


def applyStrategy(filename):

    rock = "A"
    paper = "B"
    scissors = "C"

    loos = "X"
    draw = "Y"
    win = "Z"

    #scores
    myScores = 0
    rockScores = 1
    paperScores= 2
    scissorsScores= 3
    lossScores = 0 
    drawScores = 3
    winScores = 6
    
    rounds = open(filename, "r")

    
    for play in rounds:
        
        play = play.strip().split(" ")
        
        #draw
        if play[1] == draw:
            if play[0] == rock:
                myScores += rockScores + drawScores

            if play[0] == paper:
                myScores += paperScores + drawScores

            if play[0] == scissors:
                myScores += scissorsScores + drawScores

        #win
        if play[1] == win:
            if play[0] ==  rock:
                myScores += paperScores + winScores

            if play[0] == paper:
                myScores += scissorsScores + winScores

            if play[0] == scissors:
                myScores += rockScores + winScores

        #loss
        if play[1] == loos:
            if play[0] == rock:
                myScores += scissorsScores

            if play[0] == paper:
                myScores += rockScores

            if play[0] == scissors:
                myScores += rockScores
    print(myScores)




applyStrategy("input.txt")
applyStrategy("inputBasic.txt")
        
