n = int(input("Enter Number of Rows:-- "))
print()
for i in range(1,n+1):
    for j in range(i):
        print((j+1) , end=' ')
    print()
