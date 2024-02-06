N= (int)(input("Enter the value of N"))
if(N!=0):
    sum=0.0
    for i in range(1,(N+1)):
        sum = sum + (1/i)
    
    print(sum)
