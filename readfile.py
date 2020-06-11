f = open("stud.txt","r")
ch = "y"
lns = f.readlines()
for l in lns:
    print(l,end="")
f.close()
