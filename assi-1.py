box_hold = 15 # initializing value of books hold by box 
user = float(input("Please enter the number of books: ")) # print the number of books from user
print('****SAMPLE OUTPUT FOR QUESTION 1****')
result = user / box_hold # calculating the result 
roundedResult = round(result,1) # rounded to 1 decimal point
total_round = round(roundedResult) # rounded to nearest integer
print("You will need ",result, "box(es) for your books.") # print the result with suitable message
print("You will need ",total_round,  "FULL box(es) for your books.") # print the result with suitable message


print('****SAMPLE OUTPUT FOR QUESTION 2****')
[Distance, Time] = 440 , 7 # initializing value of distance and time 
f1 = Distance/Time # calculating average speed in km/h and assign as f1
roundedResult1 = round(f1, 2) # rounded to 2 decimal points
f2 = f1/3.6 # calculating average speed in m/sec and assign as f2
roundedResult2 = round(f2) # rounded to nearest integer
print(" Your Speed is = ", roundedResult1,"km/h","or", roundedResult2,"m/sec" ) # print the result with a suitable message


print('****SAMPLE OUTPUT FOR QUESTION 3****')
[x,y,z] = 12.56, 7, 14.3015 # initializing value of x,y,z
print("x=",x ,"y=",y ,"z=",z) # print the value of x,y,z with a suitable message
f1 = 3**y - (x + y) # assign numerator as f1 
f2 = (x - y) * z # assign denomerator as f2
result = f1 / f2 # calculating the result
print(" Result = ", result) # print the result with a suitable message


