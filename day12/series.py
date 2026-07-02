#This function prints a pattern of numbers
def pattern(n):
    for i in range(1, n + 1):
          for j in range(n, i-1, -1):
                print(f"{i}", end=" ")
          print()

pattern(5)
