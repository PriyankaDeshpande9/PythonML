'''4.Write a program which accept one number form user and return addition of
its factors.
Input : 12 Output : 16 (1+2+3+4+6)'''


def Add_factors(n):
    Sum = 0
    for i in range(1,(n//2+1)):
        print(i)
        if n%i==0:
            Sum += i
    return Sum


def main():
    num = int(input("Enter the number : "))
    result = Add_factors(num)
    print("The sum of factors of {} is {}".format(num, result))


if __name__ == '__main__':
    main()
