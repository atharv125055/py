#This program calculates the sum of digits of a given number.
def sum_of_digits(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s
num = int(input("Enter a number: "))
s = sum_of_digits(num)
print(f"The sum of digits of the given number is: {s}")
