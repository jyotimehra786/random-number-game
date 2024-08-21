import random
lower=int(input("enter the lower value"))
print(f"the lower value is :{lower}")
upper=int(input("enter the upper value"))
print(f"the upper value is : {upper}")
for chance in range(2,-1,-1):
    guess=int(input("guess a number"))
    print(f"the guess number : {guess}")
    x=random.randint(lower,upper)
    if x==guess:
        print(f"you guess a lucky number .\n you are winner.you have  {chance} chance")
        print("you are winner....")
    else:
        print(f"you guess a wrong . \n the lucky number is {x}. you have {chance} chance")
        print("you are losser....")
       

