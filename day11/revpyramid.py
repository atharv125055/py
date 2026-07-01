#This program prints a triangle of numbers
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(f"{i}", end="")
    print(f"")