myint=int(input("Enter a positive integer between 20 and 50:")) # ask user to enter a integer from given range and converting to int  
print("myint:",myint) # print myint with suitable message
remainder=myint%5 # calculating remainder 
# using nested if statement to check integer is in given range or not and then printing suitable message 
if myint < 20: 
    print(f"{myint} is less than minimum acceptable value.") # printing suitable message
elif myint > 50:
    print(f"{myint} is higher than maximum acceptable value.") # printing suitable message
elif myint in range(20,51):
    print(f"{myint} is within the acceptable range.") # printing suitable message
    result=(myint**3)/7.351
    print("result:",result) # printing suitable message
    result2=int(result)
    print("result2:",result2) # printing suitable message
print(f"The remainder obtained after dividing {myint} by 5 =", remainder) # printing suitable message