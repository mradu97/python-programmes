class mathe:
    
    def add(self, a=None,b=None,c=None, d=None):
        if a != None and b!= None and c != None and d !=None:
            print("Sum is ", a + b+ c+d)
        elif a != None and b!= None and c != None:
            print("Sum is ", a + b+ c)
        elif a != None and b!= None:
            print("Sum is ", a + b)
        

m1 = mathe()

m1.add(3,4)
m1.add(3,4,4)
m1.add(3,4,5,3)
