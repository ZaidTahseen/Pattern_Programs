n = int(input("Enter Number of Rows --"))
print()
for i in range(n):
    print((("  ")*i)+(str(n-i)+' ')*(n-i))
