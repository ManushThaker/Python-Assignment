#A
list1 = ['windsor', 'toronto', 'ottawa', 'montreal', 'vancouver'] # initializing list1
print(list1) # printing list1

#B
print("The last 3 characters of the first element of list1 are:",list1[0][4:]) # printing last 3 characters of first element of list1 with suitable message 

#C
city_lowercase= input("Enter name of city in lowercase:") # asking user to enter cityname in lowercase
city_uppercase=city_lowercase.upper() # converting cityname to uppercase
print("cityname=",city_uppercase) # printing cityname with suitable message

#D
list1.append("waterloo") # appending cityname to end of list1
print("The updated list1 after appending item is: ",list1) # printing updated list1 with suitable message

#E
city=min(list1) # determining minimum value(alphabaticaly) in list1
print(city) # printing cityname 
item_to_replaced=list1[(list1.index(min(list1)))]='minval' # replacing minimum value(alphabaticaly) with minval in list1
print("The updated list1 after replacing item is: ",list1) # printing updated list1 with suitable message

#F
yearofbirth=int(input("Enter your year of birth (yyyy):")) # asking user to enter birth  year and converting to integer
print("year =",yearofbirth) # printing yearofbirth with suitable message 

#G
lenght=len(list1) # measure list1 lenght
print("Number of elements in list1:",lenght) # printing number of elements in list1 with suitable message
sum= yearofbirth + lenght # adding yearofbirth and lenght, storing as variable sum
print("sum =",sum) # printing sum with suitable message