k=int(input("enter the no"))
for i in range(1,k+1):
    if(k%i==0):
        print(i,end=',')
    else:
        print("invalid")
