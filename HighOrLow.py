import random

def inputValidationContinuePlay():
    allowedAnswer = ["y", "n"]
    while True:
        answer = input("Continue Playing? y/n :").strip().lower()

        if answer not in allowedAnswer:
            print("Invalid Answer")
        else:
            if answer == "y":
                return True
            else:
                return False


def inputValidation():
    allowedAnswer = ["h", "l"]
    while True:
        playerGuess = input("Guess High - H or Low - L : ").lower().strip()

        if playerGuess not in allowedAnswer:
            print("Please Valid Answer [H, h, L, l]")
        else:
            return playerGuess

def guess(oldNum, playerGuess):
    newNum = random.randint(0,100)
    while newNum == oldNum:
        newNum = random.randint()

    print("New Number is ", newNum)

    if(oldNum > newNum):
        if playerGuess == "L" or playerGuess == "l":
            return True, newNum
        else:
            return False, newNum
    elif(oldNum < newNum):
        if playerGuess == "H" or playerGuess == "h":
            return True, newNum
        else:
            return False, newNum

# def streakPrint(streak, guessRight):
#     if guessRight:
#         streak += 1
#         print("STREAK ", streak , "X")
#     return streak

continuePlaying = True

while(continuePlaying):
    #INITIALIZE
    guessRight = True
    streak = 1
    oldNum = random.randint(0,100)
    print("Starting Number is ", oldNum)

    
    while(guessRight):
        playerGuess = inputValidation()
        guessRight, oldNum = guess(oldNum, playerGuess)

    continuePlaying = inputValidationContinuePlay()

# print("Your Streak is ", streak)
print("Thank You for Playing The Game")