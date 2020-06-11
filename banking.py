import sys
class customer:
   
    bankname='SBI'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("balance after deposit:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insuffecient funds...cannot perform this operation")
            sys.exit()
        self.balance=self.balance-amount
        print("balance after withdraw:",self.balance)


print("welcome to:",customer.bankname)

name=input("enter your name:")
c=customer(name)

while True:
    print("d-deposit\nw-withdraw\ne-exit")
    option=input("choose your option:")
    if option=='d' or option == 'D':
        amount = float(input("enter th amount"))
        c.deposit(amount)
    elif option=='w' or option=='W':
        amount= float(input("enter amount"))
        c.withdraw(amount)
    elif option=='e' or option =='E':
        print('thanks for banking')
        sys.exit()
    else:
        print("invalid option..plz choose valid option")
                       
