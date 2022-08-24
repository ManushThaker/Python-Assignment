x=int(input("Enter a positive integer between 0 to 8 :")) # asking user to enter integer from range 0 to 8
count=0 # initializing count 

# using while loop  
while x < 50: # condition for while loop
    print("x :", x) # print suitable message
    count += 1 # count increase every time entering loop
    if (x  % 9 == 0): # condition for if statement
       print("Found Multiple of 9 ") # print suitable message
       break # exit loop when condition statisfy
    x += 10 # x increase by 10 
    
    
print("The final value of x is", x) # print suitable message
print("The loop was entered",count ) # print suitable message