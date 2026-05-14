t = 0
while True: 
    a = input("Enter d for a deposit and w for a withdrawl and E to exit : ")


    if a == "d":
        if t >= 10000:
            print(f"you have exeded the limit and your deposit is {t}.")
            break
            
        else: 
            d = int(input("Enter the amount you want to deposit: "))
            t = d + t
            

    elif a == "w":
        amt = int(input("enter the withdrawl amount: "))
        if amt > t: 
            print(f"Your bank acc doesn't have the desired balance rn")
            
        else: 
            t = t - amt
            print(f"Your current balance is {t}.")
            if t == 0:
                break

    
    elif a == "E":
        break
    else: 
        print("enter a valid function to perform! ")

