a=input()
def pal(x):
	b=x[::-1]
	return b
x=pal(b)
if a.isalpha():
	if(x==a):
		print("YES a Palindrome")
	else:
		print("Not a palindrome")
else:
	print("INVALID INPUT")
