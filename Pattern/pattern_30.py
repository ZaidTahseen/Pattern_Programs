n = int(input("Enter Number of Rows -- "))

for i in range(n):
    print(('  '*(n-i-1))+("* "*(2*(i+1)-1)))
for i in range(1,n):
    print((("  ")*i)+("* ")*(2*n-(2*(i+1)-1)))
