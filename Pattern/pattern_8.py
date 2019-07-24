n = int(input("Enter Number of Rows:- "))

for i in range(n):
    print((str(chr(64+n-i)+' '))*n)
    print()
