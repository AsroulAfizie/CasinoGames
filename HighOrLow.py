import random

def inputValidation():
    allowedAnswer = ["H", "h", "L", "l"]
    while True:
        playerGuess = input("Guess High - H or Low - L : ")

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

def streakCounter(streak, guessRight):
    if guessRight:
        streak += 1
        print("STREAK ", streak , "X")
    return streak

cont = True
streak = 1
oldNum = random.randint(0,100)
print("Starting Number is ", oldNum)

while(cont):
    playerGuess = inputValidation()
    cont, oldNum = guess(oldNum, playerGuess)
    streak = streakCounter(streak, cont)

print("Your Streak is ", streak)
print("Thank You for Playing The Game")