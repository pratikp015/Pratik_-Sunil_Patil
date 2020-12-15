# Assignment Day 3
# Q.1 Use IF, ELSE and ELIF to write a program in python for your report cards
#CBSE Pattern Grading and Grade Pointer System

marks = float(input("Enter the marks:-"))
if  marks <= 100 and marks >= 91 :
    print("Your Grade is-> A1 and Grade Pointer is -> 10 ")
elif marks <= 90 and marks >= 81 :
    print("Your Grade is-> A2 and Grade Pointer is-> 9.0")
elif marks <= 80 and marks >= 71 :
    print("Your Grade is-> B1 and Grade Pointer is-> 8.0")
elif marks <= 70 and marks >= 61 :
    print("Your Grade is-> B2 and Grade Pointer is-> 7.0")
elif marks <= 60 and marks >= 51 :
    print("Your Grade is-> C1 and Grade Pointer is-> 6.0")
elif marks <= 50 and marks >= 41 :
    print("Your Grade is-> C2 and Grade Pointer is-> 5.0")
elif marks <= 40 and marks >= 33 :
    print("Your Grade is-> D  and Grade Pointer is-> 4.0")
elif marks <= 32 and marks >= 21 :
    print("Your Grade is-> E1 and Grade Pointer is-> Fail")
elif marks <= 20 and marks >= 00 :
    print("Your Grade is -> E2 and Grade Pointer is -> Fail")
else:
    print("Fail")
