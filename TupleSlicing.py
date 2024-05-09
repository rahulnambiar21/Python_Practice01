d={101:"Akshay",345:"Jeet",909:"Nishant",876:"Raj",900:"Rahul",567:"Pritesh"}

print(d)
print(d[345])
print(d.get(909))
print(d.items())
print(d.keys())
print(d.values())
d.pop(900)
print(d)
d.popitem()
print(d)
d1={900:"Rahul",567:"Pritesh",432:"Nandini",898:"Urvi"}
d.update(d1)
print(d)
d[111]="Jigar"
print(d)

for i in d:
    print(i," : ",d(i))
