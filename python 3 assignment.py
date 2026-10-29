Python 3.13.11 (tags/v3.13.11:6278944, Dec  5 2025, 16:26:58) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # number guessing game
>>> import random
>>> secret_number = random.randint(1,10)
>>> 
>>> attempts=3
>>> guess = int(input("guess 1-10: "))
guess 1-10: 7
>>> if guess ==secret_number:
...     print("correct")
... else:
...     print("wrong,secret was",secret_number)
... 
...     
wrong,secret was 9
>>> 
>>> 
>>> import random
>>> secret_number = random.randint(1,10)
>>> attempts=3
>>> 
>>> while attempts>0:
...     guess = int(input("guess 1-10: "))
...     if guess < 1 or guess >10:
...         print("1 to 10 only")
...     elif guess > secret_number:
...         print("too high")
...         attempts -=1
...     elif guess < secret_number:
...         print("too low")
...         attempts -=1
...     else:
...         print("correct")
...         break
... 
...     
guess 1-10: 4
too low
guess 1-10: 6
too low
guess 1-10: 9
too high
>>> ig attempts==0:
...     
SyntaxError: invalid syntax
>>> if attempts==0
SyntaxError: expected ':'
if attempts==0:
    print("game over,secret was",secret_number)

    
game over,secret was 8


import random
secret_number = random.randint(1,10)
attempts = 3

while attempts>0:
    guess = int(input("guess the number (between 1 and 10): "))

    
guess the number (between 1 and 10): 5
guess the number (between 1 and 10): 
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    guess = int(input("guess the number (between 1 and 10): "))
KeyboardInterrupt
while attempts>0:
    guess = int(input("guess the number (between 1 and 10): "))
    if guess < 1 or guess > 10:
        print("your guess is out of range.please guess a number between 1 and 10.")
        continue
    elif guess > secret_number:
        print("too high.try again.")
        attempts-=1
    elif guess < secret_number:
        print("too low.try again.")
        attempts-=1
    else:
        print("congratulations! you gussed the correct number.")
        break
else:
    print("better luck next time! secret was",secret_number)

    
guess the number (between 1 and 10): 6
too high.try again.
guess the number (between 1 and 10): 4
too low.try again.
guess the number (between 1 and 10): 5
congratulations! you gussed the correct number.


#for loop
n=int(input("enter the number: "))
enter the number: 5
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

    
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

# function
def calculate_bmi(weight,height):
    return weight / (height ** 2)

weight = float(input("enter your weight in kg: "))
enter your weight in kg: 58
height = float(input("enter your height in meters: "))
enter your height in meters: 1.62
bmi = calculate_bmi(weight,height)
print(f"your bmi is: {bmi:.2f}")
your bmi is: 22.10
