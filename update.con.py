import mysql.connector
mycon= mysql.connector.connect(host="localhost", user="root", passwd="mradu", database="school")
mycursor=mycon.cursor()
val=(input("enter which city to update"),input("enter  in which it is to be update"),)

sql="update student SET city=%s WHERE Sno=%s"
mycursor.execute(sql,val)
mycon.commit()
print(mycursor.rowcount,"record updated")
mycursor.close()
mycon.close()
