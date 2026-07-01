#This program is used to print the star pattern
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(f"*",end="")
    print(f"")
for i in range(1,6):
    for j in range(i,0,-1):
        print(f"*",end="")
    print(f"")