import random

class RockPaperScissors:
    def __init__(self):
        self.__state = "init"
    def takeTurn(self, sInput):
        if self.__state == "init":
            self.__state = "playing"
            return "this is a game of rock paper scissors ... you know what to do"
        else:
            aChoices = ["rock", "paper", "scissors"]
            nComputer = random.randint(0, len(aChoices) - 1)
            sComputer = aChoices[nComputer]
            sReturn = "you chose " + sInput + " the computer chose " + sComputer + "\n"
            if sInput not in aChoices:
                sReturn += "please enter rock, paper or scissors"
            elif sInput == sComputer:
                sReturn += "tie"
            elif sInput == "rock" and sComputer == "scissors":
                sReturn += "You win ... rock smashes scissors"
            elif sInput == "paper" and sComputer == "rock":
                sReturn += "You win ... paper smothers rock"
            elif sInput == "scissors" and sComputer == "paper":
                sReturn += "You win ... scissors cut paper"
            else:
                sReturn += "Computer wins"
        return sReturn
