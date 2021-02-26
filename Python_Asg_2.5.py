'''5.Write a program which accept one number for user and check whether number
is prime or not.
Input : 5 Output : It is Prime Number'''


def ChkPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
            else:
                return True
    else:
        print("Enter the valid number")


def main():
    no = int(input("Enter the number : "))
    if ChkPrime(no)==False:
        print(f"{no} is not prime")
    else:
        print(f"{no} is prime")


if __name__=='__main__':
    main()
