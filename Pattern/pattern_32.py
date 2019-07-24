n = int(input("Enter Number of Rows -- "))

for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(2*i-1,0,-1):
        print(j, end=" ")
    print()
