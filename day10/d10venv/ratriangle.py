#This is a simple program to print a series of numbers in a right-angled triangle pattern using nested while loops.
i=1
while i<=5:
    j=1
    while j<=i:
        print(f"{i}",end="")
        j=j+1
    print(f"")
    i=i+1