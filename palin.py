str = input("any word")
str2 = "".join(reversed(str))

print(str2)
if str == str2 :
    print( str , " : is palindrome")
else:
    print( str , " : is not palindrome")
