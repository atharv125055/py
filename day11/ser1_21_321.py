#This program prints a triangle of numbers
for i in range(1,6):
    for j in range(1,i+1):
        print(f"{i-j+1}", end="")
    print(f"")