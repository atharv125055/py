#This program is used to print the numbers from 1 to 10 except 5 and 7.
i=1
while i<=10:
    if i==5 or i==7:
        i+=1
        continue
    print(f"{i}")
    i+=1