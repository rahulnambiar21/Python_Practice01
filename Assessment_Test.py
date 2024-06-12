class FruitManager:
    print(" Fruit Market Manager")
    print("\n")
    
    def addFruit(self,fname,qty,prz,total):
        self.fname=fname
        self.qty=qty
        self.prz=prz
        self.total=total
    def checkStock(self):
        print("",str(self.fname)+" "+str(self.qty)+"kg "+"for Rs."+str(self.prz)+"per kg")
    def updateStock(self):
        print("",str(self.fname)+" "+str(self.qty)+"kg "+"for Rs."+str(self.prz)+"per kg")
        
b1=FruitManager()

while True:
    print("1. Add Fruit Stock")
    print("2. View Fruit Stock")
    print("3. Update Fruit Stock")
    print("4. Exit")

    print("*"*50)
    choice=int(input("Enter your Choice: "))
    user_dict={}

    if choice==1:
        fname=input("Enter Fruit Name : ")
        qty=int(input("Enter qty (in kg) : "))
        prz=int(input("Enter Price (per kg) : "))
        total=print("Total price is : Rs.",qty*prz)
        b1.addFruit(fname,qty,prz,total)
        print("*"*50)
    elif choice==2:
        user_dict={fname.title():["qty: "+str(qty),"Rs. "+str(prz)]}
        print(user_dict)
        print("*"*50)
    elif choice==3:
        
        print("*"*50)
    elif choice==4:
        print("Thank you for using our services.")
        break
    else:
        print("Invalid Choice.Please Try Again")
        print("*"*50)
        
