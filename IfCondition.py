'''
IF Condition

1. Simple If

    if condition:
        statement

2. If/Else

    if condition:
        statement
    else:
        statement

3. Ladder If

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement

4. Nested If

    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement

'''

a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a>b:
    if a>c:
        print("A is Max number")
    else:
        print("C is Max number")
elif b>c:
    print("B is Max number")
else:
    print("C is Max number")
