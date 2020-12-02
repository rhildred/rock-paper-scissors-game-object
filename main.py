from RockPaperScissors import RockPaperScissors

oGame = RockPaperScissors()

while True:
    sInput = input("> ")
    sReturn = oGame.takeTurn(sInput)
    print(sReturn)
