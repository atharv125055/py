#
for i in range(1,6):
    for j in range(5,i,-1):
        print(f"_ ",end="")
    for j in range(1,i+1):
        print(f"{j}",end="")    
    for j in range(i-1,0,-1):
        print(f"{j}",end="")    
    print(f"")