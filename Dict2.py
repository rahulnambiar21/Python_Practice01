d={1:"Jigar",2:"Ajay",3:"Kamal",4:"Ketan",5:"Sunil"}

value=input("Enter Value to search from dictionary:")
flag=False
for i in d:
    if d[i]==value:
        flag=True
        break
if flag==True:
    print(value,"Present in Dictionary")
else:
    print(value,"Not Present in Dictionary")
