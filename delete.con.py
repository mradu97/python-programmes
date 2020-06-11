import mysql.connector
mycon =mysql.connector.connect(host="localhost",user="root",passwd="mradu",database="school")
mycursor=mycon.cursor()

val=(int(input("enter serial no")),)

sql="select * from student WHERE Sno >= %s"

mycursor.execute(sql, val)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
    
mycursor.close()
mycon.close()

