def ascii_sum(mystr1):   #define function
    ascii_sum = sum(ord(ch) for ch in mystr1)
    print("The ASCII value of characters:", ascii_sum)
    ascii_sum = []
    
    
mystr1 = input("Enter any string: ")
mySum = ascii_sum(mystr1)