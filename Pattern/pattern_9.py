n = int(input("Enter Number of Rows:-"))
print()

for i in range(n):
    for i in range(n):
        print(str(chr(64+n-i)) ,end=' ')
    print()
