n = int(input('Please Enter Number of Rows ---'))
print()

for i in range(1,n+1):
    print(" "*(n-i),(str(chr(64+i)+' ')*i))
