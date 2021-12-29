import random

def gamewin(comp,player):
    if comp==player:
        return None
    if comp=='s':
        if player=='w':
            return False
        elif player=='g':
            return True
    elif comp=='w':
        if player=='s':
            return True
        elif player=='g':
            return False
    elif comp=='g':
        if player=='s':
            return False
        elif player=='w':
            return True

print("Comp Turn : Snake(s) water(w) or gun(g)  ???")
randNo = random.randint(1,3)
if randNo==1:
    comp = 's'
elif randNo==2:
    comp = 'w'
elif randNo==3:
    comp = 'g'
player = input("Your turn : Snake(s) water(w) or gun(g)  ???  ")
print("Computer chose : " + comp)
# print("You choose : " + player)
a = gamewin(comp,player)
if a==None:
    print("The game is a tie!!")
elif a==True:
    print("Hurray!!! You won :)")
elif a==False:
    print("You lose.. Better luck next time")