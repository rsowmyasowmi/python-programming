st=input("Enter any String:")
vow=['a','e','i','o','u','A','E','I','O','U']
flag=0
for i in st:
	if i in vow:
		flag=1
if(flag==1):
	print("Vowel is present")
else:
	print("Vowel is not presented")
