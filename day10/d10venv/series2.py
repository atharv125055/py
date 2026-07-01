#This program prints a series of numbers in the shape of a triangle.series : 1,23,456,78910
i=1
x=1
while i<=4:
    j=1
    while j<=i:
        print(f"{x}",end="")
        x=x+1
        j=j+1
    if i<4:
        print(f"")
    i=i+1