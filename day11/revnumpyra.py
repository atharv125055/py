#This program prints a pattern of numbers using nested for loops
for i in range(5, 0, -1):
    for j in range(1,i+1):
        print(f"{i}", end="")
    print(f"")