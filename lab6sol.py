def multiply_lists(list1, list2): # define function
    product = [] # funtion to return list
# using nested for loop to find product of list1 and list2 
    for i in list1:
        for j in list2:
            k = i*j; 
            product.append(k) # using append to the list product, and returns the list to the caller of the function  
    return product
    
list1 = [4,2,7] # define list1
list2 = [3,1,9,2] # define list2
print("list1= ", list1,"list2 =",list2) # printing with suitable message 

prod_list = multiply_lists(list1, list2) # store the resulting list in the variable prod_list
print("prod_list =", prod_list) # printing suitable message

Sum = sum(prod_list) # calculating sum of element of prod_list
print("Sum =",Sum) # printing suitable message

count = prod_list.count(4) # counting occcurence of 4 in prod_list
print("Number of times 4 occurs =",count) # printing suitable message

# using if-else statement to check element 72 is in prod_list or not
if (72 in prod_list):
    print(f"{72} occurs in prod_list: True") # printing suitable message
else:
    print(f"{72} does not occurs in prod_list: False") # printing suitable message
    
prod_list.sort() # sort prod_list
print("sorted list =",prod_list) # printing suitable message 