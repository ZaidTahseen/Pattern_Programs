n = int(input('Please Enter Number of Rows ---'))
print()
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(str(j)+' ',end='')
    print()
