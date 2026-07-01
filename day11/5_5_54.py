#This program prints a pattern of numbers using nested for loops
for i in range(5, 0, -1):
    for j in range(5, i-1, -1):
        print(f"{j}", end=" ")
    print(f"")