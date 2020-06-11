file= open("data.txt","w")
name=input("enter name")
age=input("enter age")
address=input("enter address")
file.write(name+"\n")
file.write(age+"\n")
file.write(address+"\n")
file.close()
f=open("stud.txt","r")
lns=f.readlines()
for l in lns:
    print(l,end="")
    
f.close()
