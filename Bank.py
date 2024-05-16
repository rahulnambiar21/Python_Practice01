class Bank:
    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello ",cname,", Your Account Number is : ",str(acno)," is Opened with balance of Rs. ",str(balance))
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("You need another Rs. ",str(amount-self.balance))
    def checkBalance(self):
        print("Your Balance is : Rs.",self.balance)

b1=Bank()
b1.openAccount("Rahul",2129,20000)

while True:
    print("*"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*50)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount: "))
        b1.withdraw(amount)
        print("*"*50)
    elif choice==3:
        b1.checkBalance()
        print("*"*50)
    elif choice==4:
        print("Thank you for using our Services")
        break
    else:
        print("Invalid choice. Please Try Again")
        
