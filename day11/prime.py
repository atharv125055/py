#This program checks whether a number is prime or not
num=int(input("Enter a number: "))
i=2
while i<num:
    if num%i==0:
        break
    i+=1
if i<num:
    print(num,"is not a prime number")    
else:
    print(num,"is a prime number")