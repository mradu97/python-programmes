l1=[[0,0],[0,0]]
l2=[[0,0],[0,0]]
l3=[[0,0],[0,0]]


i=0
while(i<=1):
    j=0
    while(j<=1):
        l1[i][j] =int(input("Enter value"))
        j = j + 1
        
    i = i +1






i=0
while(i<=1):
    j=0
    while(j<=1):
        l2[i][j] =int(input("Enter value"))
        j = j + 1
        
    i = i +1

i=0
while(i<=1):
    j=0
    while(j<=1):
        print(l1[i][j],end=" ")
        j = j + 1
    print("")
    i = i +1

k=0
while(k<=1):
    m=0
    while(m<=1):
        print(l2[k][m],end=" ")
        m = m + 1
    print("")
    k = k +1

i=0
while(i<=1):
    j=0
    while(j<=1):
        k=0
        while(k<=1):
            l3[i][j]+=l1[i][k]*l2[k][j]
            k=k+1
        j=j+1

    i=i+1

i=0
while(i<=1):
    j=0
    while(j<=1):
        print(l3[i][j],end=" ")
        j=j+1
    print("")
    i=i+1
