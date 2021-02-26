'''10. Write a program which accept number from user and return addition of
digits in that number.
Input : 5187934   Output : 37'''


def total_of_digits(num):
    Sum=0
    if num>0:
        while num:
            digit = num%10
            num = num//10
            Sum = Sum+digit
        return Sum
            

def main():
    n= int(input("Enter the number : "))
    Total = total_of_digits(n)
    print("Sum of digits in {} is : {}".format(n, Total))

if __name__=='__main__':
    main()
