import random

#print(random.randint(1,20)
#print(random.choice([])

num=random.randint(1,20)

while True:
    guess=int(input("Guess a Number Between 1 to 20 :"))
    if guess==num:
        print("You guessed a Correct Number")
        break
    elif guess>num:
        print("You guessed a Higher Number")
    elif guess<num:
        print("You guessed a Smaller Number")
