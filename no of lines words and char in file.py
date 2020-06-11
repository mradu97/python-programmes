import os,sys
fname=input("enter file name")
f=open(fname,"r")
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
print("the no of lines:",lcount)
print("the no of characters:",ccount)
print("the no of words:",words)
