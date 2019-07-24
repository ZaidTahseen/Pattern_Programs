n = int(input("Enter Number of Rows --"))
print()
for i in range(n):
    print("  "*i,end='' )
    for j in range(n-i):
        print(str(n-i-j)+' ',end='')
    print()
