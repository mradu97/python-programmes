s=input("enter a string")
i=0
print("characters at even position:")
while i<len(s):
    print(s[i])
    i=i+2
print()
print("characters at odd position")
i=1
while i<len(s):
    print(s[i],end=',')
    i=i+2
