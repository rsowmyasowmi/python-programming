def odddig():
a=int(input())
b=[]
while(a!=0):
b.append(a%10)
a//=10
for i in range(len(b)-1,-1,-1):
if b[i]%2!=0:
    print(b[i])
try:
odddig()
except:
    print('invalid')
