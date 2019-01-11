a=int(input("enter the no"))
b=int(input("enter the no"))
flag=0
c=a*b
for i in range(0,c+1):
    if(i**2==c):
      flag=flag+1
if(flag==1):
    print("yes")
else:
    print("no")
