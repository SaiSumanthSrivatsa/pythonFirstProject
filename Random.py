import random
name=input("enter u r name")
print('Hi '+name+' Lets play a game of random guessing')
print('The computer guesses a number from 1-20 and u have to find it')
guessComputer=random.randint(1,20)
for a in range(1,3):
    guessUser=int(input('take a guess'))
    if(guessUser<guessComputer):
        print('The guess is too Low')
    elif(guessUser>guessComputer):
        print('The guess is too High')
    else:
        break
if(guessUser==guessComputer):
    print('Congrats u have guessed it right')
else:
    print('The number i was thinking was'+guessComputer+'')