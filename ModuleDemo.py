import UDF

while True:
    print("*"*50)
    print("1. OddEven")
    print("2. MaxofTwo")
    print("3. MaxofThree")
    print("4. Exit")

    print("*"*50)
    choice=int(input("Enter your Choice : "))

    if choice==1:
        n1=int(input("Enter Number: "))
        UDF.oddeven(n1)
        print("*"*50)
    elif choice==2:
        n1=int(input("Enter Number: "))
        n2=int(input("Enter Number: "))
        UDF.maxoftwo(n1,n2)
        print("*"*50)
    elif choice==3:
        n1=int(input("Enter Number: "))
        n2=int(input("Enter Number: "))
        n3=int(input("Enter Number: "))
        UDF.maxofthree(n1,n2,n3)
        print("*"*50)
    elif choice==4:
        print("Thank you")
        break
    else:
        print("Invalid Choice. Please Try Again.")
        print("*"*50)
        
