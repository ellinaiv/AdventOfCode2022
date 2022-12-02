


def applyStrategy(filename):

    rock = ["A", "X"]
    paper = ["B", "Y"]
    scissors = ["C", "Z"]

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
        
        play = play[0:3]
        play = play.split(" ")
        
        #draw
        if play[0] in rock and play[1] in rock:
            myScores += drawScores

        if play[0] in paper and play[1] in paper:
            myScores +=	drawScores

        if play[0] in scissors and play[1] in scissors:
            myScores +=	drawScores

        #win
        if play[0] in rock and play[1] in paper:
            myScores +=	winScores

        if play[0] in paper and play[1] in scissors:
            myScores +=	winScores

        if play[0] in scissors and play[1] in rock:
            myScores +=	winScores

        #loss
        if play[1] in rock:
            myScores +=	rockScores
        if play[1] in paper:
            myScores += paperScores
        if play[1] in scissors:
            myScores += scissorsScores

    print(myScores)




applyStrategy("input.txt")
applyStrategy("inputBasic.txt")
        
