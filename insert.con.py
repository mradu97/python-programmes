import mysql.connector
int(input("enter  in which it is to be update")),a=int(input("enter the sno"))
b=input("enter name")
c=input("enter the city")
val=(a,b,c)
sql="insert into student values(%s,%s,%s)"

mycursor.execute(sql, val)
mycon.commit()
print(mycursor.rowcount,"record updated")
mycursor.close()
mycon.close()
