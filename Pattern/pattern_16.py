n = int(input('Please Enter Number of Rows ---'))
print()
for i in range(n):
    for j in range(n-i):
         print(chr(65+j), end=' ')
    print()
