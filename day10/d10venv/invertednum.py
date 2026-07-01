#This is a simple program to print an inverted right-angled triangle pattern of numbers using nested while loops.
i=5
while i>=1:
    j=1
    while j<=i:
        print(f"{j}",end="")
        j=j+1
    print(f"")
    i=i-+1