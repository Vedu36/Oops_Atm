class Atm():

    #Static/Class variable
    __count=1

    def __init__(self):
        #instance vaiable
        self.__name=""
        self.__pin=""
        self.__balance=0
        self.so=Atm.__count
        Atm.__count=Atm.__count+1
        self.menu()

    @staticmethod
    def get_count():
        return Atm.__count
    
    staticmethod
    def set_count():
        temp=int(input("type the count number"))
        Atm.__count=temp
        print("Done")
        
    def get_name(self):
        return self.__name

    def get_pin(self):
        return self.__pin

    def set_name(self):
        temp=input("Type the pin ")
        if temp==self.__pin:
            new=input("Type the new name ")
            self.__name=new
            print("new name Set")
        else:
            print("Wrong pin")

    def set_pin(self):
        temp=input("Type the name ")
        if temp==self.__name:
            new=input("Type the new pin ")
            self.__pin=new
            print("new pin Set")
        else:
            print("Wrong name")

    def menu(self):
        user_input=input('''
                        Enter 1 to create name and pin
                        Enter 2 to deposit
                        Enter 3 to withdraw
                        Enter 4 to checkbalance
                        Enter 5 to exit
''')
        if user_input=="1":
            self.create_name()
        elif user_input=="2":
            self.deposit()
        elif user_input=="6":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("exit")
    
    def create_name(self):
        self.__name=input("type the name ")
        print("name created")
        self.__pin=input("type the pin ")
        print("pin created")
        
    def deposit(self):
        temp=input("enter name ")
        if temp==self.__name:
            temp1=input("enter pin ")
            if temp1==self.__pin:
                amount=int(input("Type the amount "))
                self.__balance=self.__balance + amount
                print(self.__balance)
            else:
                print("invalad pin")
        else:
            print ("invalad name")
        
    def withdraw(self):
        temp=input("enter name ")
        if temp==self.__name:
            temp1=input("enter pin ")
            if temp1==self.__pin:
                amount=int(input("typr the amout "))
                if self.__balance>amount: 
                    self.__balance=self.__balance-amount
                    print(self.__balance)
                else:
                    print("balance not sufficient")
            else:
                print("invalad pin")
        else:
            print ("invalad name")

    def check_balance(self):
        temp=input("enter name ")
        if temp==self.__name:
            temp1=input("enter pin ")
            if temp1==self.__pin:
                print(self.__balance)
            else:
                print("invalad pin")
        else:
            print ("invalad name")