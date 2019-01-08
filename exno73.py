x=int(input("Enter X value:"))
y=int(input("Enter Y value:"))
z=int(input("Enter Z value:"))
flag=0
for i in range(l,z+1):
	if i==x:
		flag=1
if(flag==1):
	print("X is present")
else:
	print("X is not presented")
