import random

data=open("data.txt","w")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
prime=open("prime.txt","w")
l=data.read().split(",")[:-1]
for i in l:
        if int(i)%2==0:
            even.write(i+",")
        else:
            odd.write(i+",")
        if int(i)%2!=0:
            for j in range(3,int(int(i)/2)+1,2):
                if int(i)%j==0:
                    break
            else:
                prime.write(i+",")

even.close()
odd.close()
prime.close()
data.close()

print("Data file content")
data=open("data.txt","r")
print(data.read())
data.close()

print("Even file content")
even=open("even.txt","r")
print(even.read())
even.close()

print("Odd file content")
odd=open("odd.txt","r")
print(odd.read())
odd.close()

print("Prime file content")
prime=open("prime.txt","r")
print(prime.read())
prime.close()
