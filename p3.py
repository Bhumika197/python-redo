import random

a =random.randint(1, 100 )
print("Enter your number btw 1 to 100")
d = 5

while True: 
    b = int(input("Enter a number! "))
    d =d -1

    if d == 0:
        print(f"Your number was {a} \n You are out of moves! sorry start again  ")
        break


    if a > b: 
        print(f"you entered number {b}, is smaller")
    elif a < b: 
        print(f"you entered number {b}, is larger")
    elif a == b: 
        print(f"You guessed it , the number is {b}")
        break
    else: 
        print("Enter a valid input")

   