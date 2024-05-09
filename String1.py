s=input(" Enter String :")

al=0
nu=0
sp=0
cap=0
low=0
spc=0


for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nu=nu+1
    elif i.isspace():
        sp=sp+1
    else:
        spc=spc+1
    if i.isupper():
        cap=cap+1
    elif i.islower():
        low=low+1
        
        

        
print("Total Alphabets :",al)
print("Total Numbers :",nu)
print("Total Space :",sp)
print("Total Capital :",cap)
print("Total Lower :",low)
print("Total Special Characters :",spc)


        

