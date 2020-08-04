import random
print("Higher - Lower, guess the Number!")
def checkInputNumber(right_Number, guess_number, tries):
    tries = tries + 1
    if(right_Number == guess_number):
        print("Gratulation, you guessed it in", tries, "tries!")
        pass
    elif(guess_number == 0):
        guess_number = int(input("Guess your first number: "))
        checkInputNumber(right_Number, guess_number, tries)
    elif(right_Number < guess_number):
        guess_number = int(input("Lower! Guess again: "))
        checkInputNumber(right_Number, guess_number, tries)
    elif (right_Number > guess_number):
        guess_number = int(input("Higher! Guess again: "))
        checkInputNumber(right_Number, guess_number, tries)
    else:
        pass
checkInputNumber(random.randint(0, 100), 0, -1)
