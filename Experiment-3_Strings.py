str1 = str(input("Enter 1st string :: ")) 
str2 = str(input("Enter 2nd string :: "))
print("The 1st String you entered is :: ",str1) 
print("The 2nd String you entered is :: ",str2)
str3=str1 #copy string
b = str1 [ 0 : : 2 ] #string slicing
reverse_str = str1 [-1 : : -1] #reverse
addstrs = str1 + " " + str2 #concatenation of string
len_of_str = len(str1) #length of string
if str1 is str2 or str1 == str2:
    print("String 2 is equal to string 1") #equality else:
    print("String 2 is not equal to Str 1 ")
if(str2 in str1):
    print("String 2 is a substring of 1st string") #check substring else:
    print("String 2 is not a substring of 1st string")
    print("The concatenation of string 1 and string 2 is :: ",addstrs) #concatenation of string
    print("The length of String 1 is :: ",len_of_str) #length of string
    print("The reverse of 1st is :: ",reverse_str) #reverse
    print("The sliced version of 1st String from 0th index with step of 2 :: ",b)
#string slicing
    print("The Copy of 1st String is :: ",str3)