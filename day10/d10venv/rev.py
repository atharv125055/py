#This is a simple program to print a series of numbers in a right-angled triangle pattern using nested while loops.series : 1,21,321,4321,54321
i=5
while i>=1:
    j=i
    while j>=1:
        print(f"{j}",end="")
        j-=1
    print(f"")
    i=i-1