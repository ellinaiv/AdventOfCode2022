


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
        opponent = play[0]
        me = play[1]

        #draw
        if me == draw:
            myScores += drawScores

            if opponent == rock:
                myScores += rockScores

            if opponent == paper:
                myScores += paperScores

            if opponent == scissors:
                myScores += scissorsScores
            continue

        #win
        if me == win:
            myScores += winScores

            if opponent ==  rock:
                myScores += paperScores

            if opponent == paper:
                myScores += scissorsScores

            if opponent == scissors:
                myScores += rockScores
            continue
        
        #loss
        if me == loos:
            if opponent == rock:
                myScores += scissorsScores

            if opponent == paper:
                myScores += rockScores

            if opponent == scissors:
                myScores += paperScores

    print(myScores)




applyStrategy("input.txt")
applyStrategy("inputBasic.txt")
        
