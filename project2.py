import random

randNum = random.randint(1,100)
print("Guess a Number between 1 to 100 ")
userGuess = None
Guess = 0 

while(userGuess!=randNum):
    userGuess = int(input("Enter your guess : "))
    if(userGuess == randNum):
        print(f"Yayyyy....... You Guess it right! the number is {randNum} ")
    else:
        if(userGuess>randNum):
            print("You guesses it wrong!! Enter a smaller number")
        else:
            print("You guesses it wrong!! Enter a larger number")
    Guess += 1
    
print(f"You guesses the number in {Guess} guesses" )

with open("highscoree.txt", 'r') as f:
    hiscore = int(f.read())
if(Guess<hiscore):
    with open("highscoree.txt", 'w') as f:
        f.write(str(Guess))

with open("highscoree.txt", 'r') as f:
    hiscore = int(f.read()) 