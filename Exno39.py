num1 = 10
num2 = 14
num3 = 12
num4 = 10
num5 = 14
num6 = 12
num7 = 10
num8 = 14
num9 = 10
num10 = 14
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
num5 = float(input("Enter fifth number: "))
num6 = float(input("Enter sixth number: "))
num7 = float(input("Enter seventh number: "))
num8 = float(input("Enter eight number: "))
num9 = float(input("Enter nine number: "))
num10 = float(input("Enter ten number: "))
if (num1 >= num2) and (num1 >= num10):
   largest = num1
elif (num2 >= num1) and (num2 >= num10):
   largest = num2
elif (num2 >= num1) and (num3 >= num10):
   largest = num3
elif (num2 >= num1) and (num4 >= num10):
   largest = num4
elif (num2 >= num1) and (num5 >= num10):
   largest = num5
elif (num2 >= num1) and (num6 >= num10):
   largest = num6
elif (num2 >= num1) and (num7 >= num10):
   largest = num7
elif (num2 >= num1) and (num8 >= num10):
   largest = num8
elif (num2 >= num1) and (num9 >= num10):
   largest = num9

else:
   largest = num10

print("The largest number
between",num1,",",num2,",",num3,",",num4,",",num5,",",num6,",",num7,",",num8,",",num9,",",num10,",",is",largest)
     
