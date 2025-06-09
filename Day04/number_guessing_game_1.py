import random
number = random.randint(1,20)
print("The computer chose a number between 1 and 20.")
turns=0
while True:
    guess=int(input("Guess a number between 1 and 20 ="))
    if(guess==number):
        print("Congratulations, you are right!")
        break
    elif(guess<number):
        print("Sorry, your number is too small. Try again.")
        turns+=1
    elif(guess>number):
        print("Sorry, your number is too big. Try again.")
        turns+= 1