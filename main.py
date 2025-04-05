import random
user1=int(input("lower value"))
user2=int(input("upper bound"))
com=random.randint(user1,user2)
print(com)
n=7
total_chances=n
print(f"you have only {total_chances} choices")
count = 0
flag = False
while count<total_chances:
    count+=1
    guess = int(input("enter your guess"))
    if com==guess:
        print("you got it right")
        flag=True
        break
    if com < guess:
        print("you got too high")
    elif com > guess:
        print("you got too less number")
