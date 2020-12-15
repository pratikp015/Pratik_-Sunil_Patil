#Assignment Day 3
#Q.4 Use for loop to print prime numbers in between 1 to 1000
upper = 1
lower = 1000

for num in range(upper,lower+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
