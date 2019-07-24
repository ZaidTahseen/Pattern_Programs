n = int(input('Please Enter Number of Rows ---'))
print()

for i in range(n):
    print((str(chr(64+n-i)+' '))*(n-i))
