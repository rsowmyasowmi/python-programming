n=100/110
op=['%','/']
for i in n :
	if i in op:
		if(i=='%'):
			k1=int(n.split(i)[0])
			k2=int(n.split(i)[1])
			ans=k1%k2
		elif(i=='/'):
			k1=int(n.split(i)[0])
			k2=int(n.split(i)[1])
			ans=k1//k2
print(ans)

