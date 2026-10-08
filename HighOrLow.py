import random

def inputValidation():
    allowedAnswer = ["H", "h", "L", "l"]
    while True:
        playerGuess = input("Guess High - H or Low - L : ")

        if playerGuess not in allowedAnswer:
            print("Please Valid Answer [ H, h, L, l]")
        else:
            return playerGuess

def guess(oldNum, playerGuess):
    newNum = random.randint(0,100)
    print("New Number is ", newNum)

    if(oldNum > newNum):
        if playerGuess == "L" or playerGuess == "l":
            return True, newNum
        else:
            return False, newNum
    else:
        if playerGuess == "H" or playerGuess == "h":
            return True, newNum
        else:
            return False, newNum

cont = True

oldNum = random.randint(0,100)
print("Starting Number is ", oldNum)

while(cont):
    playerGuess = inputValidation()
    cont, oldNum = guess(oldNum, playerGuess)

print("Thank You for Playing The Game")