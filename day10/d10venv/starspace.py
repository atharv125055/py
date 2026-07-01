#This program prints a pyramid pattern of numbers with spaces.
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(f"_ ",end="")
        j=j+1
    k=1    
    while k<=i:
        print(f"*",end="")
        if k<i:
          print(f"_ ",end="")
        k=k+1    
    print(f"")
    i=i+1