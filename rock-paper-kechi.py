
import random

def gamewin(comp,you):
    if comp=='r':
        if you == 'p':
            print("you Won")
        elif you == 's':
            print("computer won")
    elif comp=='s':
        if you == 'p':
            print("computer Won")
        elif you == 'r':
            print("you won")
    elif comp=='p':
        if you == 'r':
            print("computer Won")
        elif you == 's':
            print("you won")
    if comp == you:
        print("It's a tie")

wtp = int(input("Decide how much do you want to play= "))    

for i in range(wtp):
    comp = random.randint(1,3)
    if comp == 1:
        comp = 'r'
    elif comp == 2:
        comp = 'p'
    elif comp == 3:
        comp = 's'
    you = input("enter your turn : rock(r) , Paper(p) , Scissor(s): ")

    print(f'computer chose {comp}')  


    gamewin(comp,you)




