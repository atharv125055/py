#This program is used to print the sum of the numbers in a list.
numbers=[33,55,6,33,66,234,666]
s=0
for x in numbers:
    s+=x
    print(f"{x}")
print(f"Sum: {s}")