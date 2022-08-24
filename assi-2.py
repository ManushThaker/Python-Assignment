print("****SAMPLE SOLUTION A****")
name=input("Enter your name:") # asking user to enter their name
print(name) # printing name 
# using if-else statement to check name start with vowel or consonant
if(name[0]=='A' or name[0]=='a' or name[0]=='E' or name[0] =='e' or name[0]=='I'
 or name[0]=='i' or name[0]=='O' or name[0]=='o' or name[0]=='U' or name[0]=='u'): 
  print("Your name starts with a vowel")
else:
  print( "Your name starts with a consonant")
name_uppercase=name[0].upper()  # changing first letter of name to uppercase
print("The first letter of your name is:",name_uppercase) # printing first letter in uppercase with suitable message

print("****SAMPLE SOLUTION B****")
integer_input=input("Enter a positive integer (digits only):") # asking user to enter positive integer
# using if statement to check entered integer is positive or not
if (integer_input.isdigit()):
    integer = int(integer_input)
    
# using elif statement to check integer is valid or not, even, multiple of 7 or not      
if (integer_input.isdigit() == False):
    print ("You did not enter a valid input!") # printing suitable message
elif (integer % 2 == 0):
    print(" You entered an even number ") # printing suitable message
 
elif (integer % 7 == 0):
    print("You entered an odd number that is a multiple of 7 ") # printing suitable message
   
elif (integer % 7 !=0):
    print(" You entered an odd number that is NOT a multiple of 7 ") # printing suitable message
  
    
print("****SAMPLE SOLUTION C****")
L1 = [5, -34, 0, 98, -11, 244, 193, 28, -10, -20, 45, 67]
print(L1) # printing list1
x=int(input("Enter an integer x in the range 0 to 11:")) # asking user to enter integer from range 0 to 11
out=int (1) # condition to exit 

# using if statement to check integer is in range or not
if (x in range(0,12)):
  print(f"The {x} element of L1 is: {L1[x]} ") # printing suitable message

# using elif statement for what if integer is not in range, if integer in list then print its position 
if (x not in range(0,12)):
 print("You did not enter a valid input!") # printing suitable message
 out=int (0) # condition to exit 
elif (x in L1):
    print(f"{x} occurs at position:{L1.index(x)}") # printing suitable message
else:
    print(f"{x} does not occurs in L1") # printing suitable message
 
# using nested if statement to check integer is even or odd  or zero 
if out != 0: # condition to exit    
 if ((x > 0) and (x % 2 == 0)):
    print(f"First {x} elements of L1 {L1[0:-7]}") # printing suitable message
 if ((x % 2 !=0 ) and (x >0)):
    print(f"Last {x} element of L1 {L1[7:]}") # printing suitable message   
 if (x == 0): 
    print(f"empty list:{L1.clear()}, {L1}") # printing suitable message
    