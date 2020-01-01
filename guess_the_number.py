import os
import random
# using for taking a random no
a = random.randint(0, 100)
print("Welcome to word gussing game. Guss a no between 0 to 100.")
b = int(input('Enter No: '))
while b != a:
    if b < a:
        print(b, ' is less then the no by', a - b)
        b = int(input('Enter No: '))
    elif b > a:
        print(b, ' is greater then the no by', b - a)
        b =int(input('Enter No: '))
print('You WON!!     The No is ', a)
os.system("pause")
