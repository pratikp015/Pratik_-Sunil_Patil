#Assignment Day 3
#Q.4 Write a program to print x prime numbers using while loop starting from 0, and take the input of x from the user
upper =int(input("Enter the upper interval"))
lower =int(input("Enter the lower interval"))

for num in range(upper,lower+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
