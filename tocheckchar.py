str=input("enter a single character")
if str.isalnum():
    print("the character is alphanumeric")
    if str.isalpha():
        print("the character is alphabetic")
        if str.islower():
            print("the character is lower case")
        else:
            print("the character is a upper case")
            
    else:
        print("the character is a number")
elif str.isspace():
    print("the character is a space")
else:
    print("the character is a special character")
           
    
 
