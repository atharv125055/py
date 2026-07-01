#This is a simple program to print a right-angled triangle pattern of stars using nested while loops.
i=1
while i<=3:
    j=1
    while j<=i:
        print(f"*",end="")
        j=j+1
    print(f"")
    i=i+1