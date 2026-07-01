#This program prints a triangle of numbers
for i in range(1,6):
    for j in range(5,i,-1):
        print(
            f"_ ", end="")
    print(f"*", end="")
    for k in range(1,i):
        print(f"_*", end="")
    print(f"")