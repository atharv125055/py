#This is a simple program to print a right-angled triangle pattern of numbers using nested while loops.
i=1
while i<=5:
    j=1
    while j<=i:
        print(f"{j}",end="")
        j=j+1
    print(f"")
    i=i+1