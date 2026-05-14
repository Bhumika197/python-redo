import random
points_b = 0 
points_a = 0
count = 5

while True: 
    b = input("enter your choice (stone , paper , scissors): any one :  \n ")
    count = count - 1  
    
    a = random.randint(1,3)
    if (a == 1 and b == "stone") or (a == 2 and b == "paper") or (a== 3 and b =="scissor"):
        print("tie\n") 
   
    elif (a== 1 and b == "paper") or (a== 2 and b =='scissors') or (a == 3 and b == "stone"):
        points_b = points_b + 1
        print(f"B gets a point, A_point {points_a} and B_point {points_b}\n")


    elif (a== 1 and b== "scissors") or (a== 2 and b =='stone') or(a == 3 and b == "paper"):
        points_a = points_a + 1
        print(f"A gets a point, A_point {points_a} and B_point {points_b}\n")
    else:
        print("Enter a valid input")
   
    if count == 0:
        break

if points_b > points_a:
    print(f"B is the winner with total of : {points_b} points ")
elif points_b < points_a:
    print(f"A is the winner with total of : {points_a} points ")
else: 
    print(f"its a tie and both of you have: {points_a} points  ")




