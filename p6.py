c = 0
d = 0
sum =0
for s in [20,40,50,60,44]:
    sum =sum + s
    
    if s >= 40:
        print(f"student has passed")
        c = c+1
        
    else: 
        print(f"Sorry you failed")
        d =d+1
    
avg = sum / (c+d)
    
print(f"Total number of passed students are {c}")
print(f"Avg is {avg}. ")
