import random

UpperLimit = 100
LowerLimit = 0

answer = random.randint(0, 100)
while True:
    guessNumber = int(input('Enter the number you want to guess: '))
    if guessNumber == answer:
        print('Congrats, you made the correct guess!')
        break
    elif guessNumber > answer:
        UpperLimit = guessNumber
        print('Try Again! The correct number is between', LowerLimit, 'and', UpperLimit)
    else:
        LowerLimit = guessNumber
        print('Try Again! The correct number is between', LowerLimit, 'and', UpperLimit)
