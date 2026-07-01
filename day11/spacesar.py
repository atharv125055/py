#This program is used to print the star in a space format.
for i in range(1,5):
    for j in range(5,i,-1):
        print(f"_ ",end="")
    print(f"* ",end="")
    for k in range(1,i+1):
        print(f"_ * ",end="")
    print(f"")