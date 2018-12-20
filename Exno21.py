N= int(input("Please Enter First Number of an A.P Series: : "))
A= int(input("Please Enter the Total Numbers in this A.P Series: : "))
D= int(input("Please Enter the Common Difference : "))
total = (A * (2 * N + (A - 1) * D)) / 2
tn = N + (A - 1) * D
print("\nThe Sum of Arithmetic Progression Series = " , total)
print("The tn Term of Arithmetic Progression Series = " , tn)
