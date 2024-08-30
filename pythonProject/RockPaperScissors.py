import random

rock = "rock"
paper = "paper"
scissors = "scissors"

foo = ['rock', 'paper', 'scissors']
p2 = (random.choice(foo))
print(p2)

p1 = input("rock, paper, scissors?")


if p1 == p2:
    print("Draw!")
else:
    if (p1=="rock") and (p2=="paper"):
        print("rock wins!")
    elif (p1=="rock") and (p2=="scissors"):
        print("scissors wins!")
    elif (p1 == "paper") and (p2 == "scissors"):
        print("scissors wins!")
    elif (p1=="paper") and (p2=="rock"):
        print("paper wins!")
    elif (p1=="scissors") and (p2=="rock"):
        print("scissors wins!")
    elif (p1=="scissors") and (p2=="paper"):
        print("scissors wins!")

