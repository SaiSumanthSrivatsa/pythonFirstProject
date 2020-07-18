import random
print('Welcome to Rock Paper Scissors game')
user=0
computer=0
selection=['Rock','Paper','Scissors']
for n in range(1,3):
    computerChoice=random.choice(selection)
    userChoice=input('Enter u r choice')
    if computerChoice=='Rock' and userChoice=='Rock':
        print('Both chosen the same')
    elif computerChoice=='Rock' and userChoice=='Scissors':
        print('The computer has chosen'+computerChoice+'')
        print('User points:'+str(user)+'')
        computer=computer+1
        print('Computer Points:'+str(computer)+'')
    elif computerChoice=='Rock' and userChoice=='Paper':
        print('The computer has chosen'+computerChoice+'')
        user=user+1
        print('User points:'+str(user)+'')
        print('Computer Points:'+str(computer)+'')
    elif computerChoice=='Paper' and userChoice=='Rock':
        print('The computer has chosen'+computerChoice+'')
        print('User points:'+str(user)+'')
        computer=computer+1
        print('Computer Points:'+str(computer)+'')
    elif computerChoice=='Paper' and userChoice=='Paper':
        print('Both chosen the same')
        print('User points:'+str(user)+'')
        print('Computer Points:'+str(computer)+'')
    elif computerChoice=='Paper' and userChoice=='Scissors':
        print('The computer has chosen'+computerChoice+'')
        user=user+1
        print('User points:'+str(user)+'')
        print('Computer Points:'+str(computer)+'')
    elif computerChoice=='Scissors' and userChoice=='Rock':
        print('The computer has chosen'+computerChoice+'')
        user=user+1
        print('User points:'+str(user)+'')
        print('Computer Points:'+str(computer)+'')
    elif computerChoice=='Scissors' and userChoice=='Paper':
        print('The computer has chosen'+computerChoice+'')
        user=user+1
        print('User points:'+str(user)+'')
        print('Computer Points:'+str(computer)+'')
    elif computerChoice=='Scissors' and userChoice=='Scissors':
        print('Both chosen the same')
        print('User points:'+str(user)+'')
        print('Computer Points:'+str(computer)+'')
    else:
        print('Do not enter anything other than RPS')
        break
if user>computer:
    print('User wins')
elif user<computer:
    print('Computer wins')
else:
    print('Draw')
