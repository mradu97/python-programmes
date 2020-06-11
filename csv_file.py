import csv
with open("emp.csv","w",newline='')as f:
    w = csv.writer(f)
    w.writerow(["eno","ename","esal","eaddr"])
    n=int(input("enter no of emplyoees"))
    for i in range (n):
        eno=input("enter employee no:")
        ename=input("enter name")
        esal=input("enter salary")
        eaddr=input("enter address")
        w.writerow([eno,ename,esal,eaddr])
                     
print("total emplyoees data written to csv file")
