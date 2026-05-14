a = 4 
print("enter a number btw 1-10")
d = 10 

while True:
   b = int(input("Enter a number: ")) 
   d = d-1

   if a == b:
      print("Correct")
      break
   
   if d == 0: 
        print("Your chances are over. You loose! ")
        break
   
   print("Incorrect guess")

