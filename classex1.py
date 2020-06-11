class student:
    
    def __init__(self,nam,roll,mrks):
        self.name = nam
        self.rollno = roll
        self.marks = mrks

    def talk(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)

s1 =student("MOhan",123,79)
s1.talk()
print(s1)
