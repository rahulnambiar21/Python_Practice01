def oddeven(a):
    if a%2==0:
        print(a," Is Even")
    else:
        print(a," Is Odd")

def maxoftwo(a,b):
    if a>b:
        print(a," Is Max")
    else:
        print(b," Is Max")

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a," Is Max")
        else:
            print(c," Is Max")
    elif b>c:
        print(b," Is Max")
    else:
        print(c," Is Max")
