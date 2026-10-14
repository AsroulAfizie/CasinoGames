import random

def inputValidationDifficulty():
    while True:
        answer = input("Choose Your Difficulty (E-Easy||M-Medium||H-Hard) :").lower().strip()

        if answer == "e":
            return 1000
        elif answer == "m":
            return 100
        elif answer == "h":
            return 10
        else:
            print("Invalid Input") 

def inputValidationBet(balance):
    while True:
        answer = input("How Much You Want To Bet?")

        if not answer.isdigit() or answer > balance or answer < 0:
            print("Enter Value Between 0 and ", balance)
        else:
            return answer

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

def inputValidationPlayerGuess():
    allowedAnswer = ["h", "l", "q"]
    while True:
        playerGuess = input("Guess High - h or Low - l or Quit - q : ").lower().strip()

        if playerGuess not in allowedAnswer:
            print("Please Valid Answer [h, l, q]")
        else:
            return playerGuess

def guess(oldNum, playerGuess, maxNum):
    newNum = random.randint(0,maxNum)
    while newNum == oldNum:
        newNum = random.randint(0,maxNum)

    print("New Number is ", newNum)

    if newNum > oldNum:
        correct = (playerGuess == "h")
    else:
        correct = (playerGuess == "l")

    if correct:
        print("CORRECT!!!")
    else:
        print("WRONG!!!")

    return correct, newNum

def streakCounter(streak, guessRight):
    if guessRight:
        streak += 1
    return streak

def highestStreakFunc(streak, highest):
    if streak > highest:
        highest = streak
    return highest

continuePlaying = True
highestStreak = 0
balance = 1000
maxNumber = inputValidationDifficulty()

while(continuePlaying and balance > 0):
    print("================")
    print("  GAME START")
    print("================")
    #INITIALIZE
    guessRight = True
    streak = 0
    oldNum = random.randint(0,maxNumber)
    print("Starting Number is ", oldNum)

    while(guessRight):
        playerGuess = inputValidationPlayerGuess()
        if playerGuess == "q":
            break
        guessRight, oldNum = guess(oldNum, playerGuess, maxNumber)
        streak = streakCounter(streak, guessRight)

    print("Your Streak is ", streak)
    highestStreak = highestStreakFunc(streak, highestStreak)
    continuePlaying = inputValidationContinuePlay()

print("Your Highest Streak is " , highestStreak)
print("Thank You for Playing The Game")