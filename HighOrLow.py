import random

def guess(oldNum, playerGuess):
    newNum = random.randint(0,100)
    print(newNum)

    if(oldNum > newNum):
        if playerGuess == "L":
            return True, newNum
        else:
            return False, newNum
    else:
        if playerGuess == "H":
            return True, newNum
        else:
            return False, newNum

cont = True

oldNum = random.randint(0,100)
print("Starting Number is ", oldNum)

while(cont):
    playerGuess = input("Guess High - H or Low - L : ")
    cont, oldNum = guess(oldNum, playerGuess)

print("Thank You for Playing The Game")