import Assessment_Test

while True:
    print("1. Fruit Market Manager")
    print("2. Customer")
    print("*"*50)

    choice=int(input("Enter your Choice : "))

    if choice==1:
        Assessment_Test.addFruit()

