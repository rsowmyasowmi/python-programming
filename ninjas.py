import sys
 def getl():
	r1=[]
	r2=[]
	while(True):
		try:
a,b = map(int,sys.stdin.readline().split())
except ValueError:
break
r1.append(a)
r1.append(b)
r2.append(l1)
r1=[]
for i in r2:
    print(i[1]-i[0])
try:
getl1()
except:
    print('invalid')
