'''3. Write a program which contains one function named as Add() which accepts
two numbers
from user and return addition of that two numbers.
Input : 11 5 Output : 16'''


def Add(a,b):
    total = a+b
    return total


def main():
    n1 = int(input("Enter 1st number : "))
    n2 = int(input("Enter 2nd number : "))
    Sum = Add(n1,n2)
    print("The sum of {} & {} is {}".format(n1,n2,Sum))
    

if __name__=='__main__':
    main()
