'''3. Write a program which accept one number from user and return its
factorial.
Input : 5 Output : 120'''

def Fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

def main():
    num = int(input("Enter the number : "))
    result = Fact(num)
    print(f"Factorial of {num} is {result}.")


if __name__=='__main__':
    main()
        
