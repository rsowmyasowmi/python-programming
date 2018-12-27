hname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as h:
    for line in h:
        num_lines += 1
print("Number of lines:")
print(num_lines)
