f = open("stud.txt","a")
ch = "y"
while ch !="n":
    nm = input("Enter student name ")
    age = input("Enter age")

    f.write(nm+"\n")
    f.write(age+"\n")
    ch = input("Want any more y/n : ")
    
f.close()
