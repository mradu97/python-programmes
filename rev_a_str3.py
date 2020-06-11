str=input("enter a string")
i=len(str)-1
target=''
while i>=0:
    target=target+str[i]
    i=i-1
print(target)
