fname = input("Enter file name: ")
n=0
with open(fname, 'r') as f:
for line in f:
   words = line.split()
     for i in words:
        for letter in i:
           if(letter.isspace):
             n=n+1
    print("Occurrences of blank spaces:")
    print(n)
