def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    return len(final)

wordlist = ['hat', 'book', 'house', 'flower', 'tree', 'grass', 'cheetah', 'lion', 'tiger', 'car', 'boat'] 
print("wordlist", wordlist)

vowels = "AaEeIiOoUu" 
count = 0
VowCount = 0
 
for word in wordlist[10]: 
    
    VowCount = Check_Vow(wordlist[count], vowels)
    
    if len(wordlist) < 11:
        print("Error. list length must be grater than 10")
        break
    
    print("The string %s contains %d vowel(s)" % (wordlist[count], VowCount))
    
    if (VowCount >= 3) :
        print('Found string with 3 or more vowels!')
        break 
    
    count = count + 3 
 

print("***SAMPLE OUTPUT B***")
total = 0 # initializing total
while True: # while condition
  num = float(input("Please Enter a number:")) # asking user to enter a number 
  total += num # adding num to total
  print("Current total:",total) # printing suitable message
  if total > 100: # if statement condition
      print("total:", total) # printing suitable message
      break # exit loop when total exceed 100
x = pow(total, 2) # calculating square and assign to variable x
x = round(x, 1) # rounded x to 1 decimal integer
print("The sqrt of", total, "is",x) # printing suitable message



print("***SAMPLE OUTPUT C***")
def fibonacci_series():  # define function
    fs = [] # funtion to return list
# define the first two numbers of the Fibonacci sequence    
    First_num = 0
    Second_num = 1
# using for loop to find first 20 fibonacci numbers           
    for i in range(0, 20): 
       if(i <= 1):
        subsequent_num = i
       else:
        subsequent_num = First_num + Second_num
        First_num = Second_num
        Second_num = subsequent_num
       fs.append(subsequent_num) # using append to the list fs, and returns the list to the caller of the function
    return fs    

num = fibonacci_series() # store the resulting list in the variable num
print("The first 20 numbers in the Fibonacci number are=",num) # printing suitable message 

    