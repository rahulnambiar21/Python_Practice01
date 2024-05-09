import random

l=[]
lucky=[]


for i in range(1,101):
    if i%2!=0:
        l.append(i)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)
    

print(l)
print(lucky)


