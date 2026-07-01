#This program prints the reverse triangle number pattern
i=5
while i>=1:
    j=5
    while j>=i:
        print(f"{i}",end="")
        j=j-1
    print(f"")
    i=i-1