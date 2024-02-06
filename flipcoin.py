import random as ra

num=(int)(input("Enter the number of times to flip coin"))
heads=0
tails=0
total=num
while(num!=0):
    ran=ra.uniform(0,1)
    print(ran)
    if(ran<0.5):
        heads+=1
    else:
        tails+=1
    num-=1

# print(heads)
# print(tails)
heads_per = (heads/total)*100
tails_per = (tails/total)*100
print(f"heads==>{heads_per}%")
print(f"tails==>{tails_per}%")

