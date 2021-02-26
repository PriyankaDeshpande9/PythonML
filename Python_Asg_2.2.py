'''2. Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

def main():
    no1 = int(input("Enter first number : "))
    for i in range(no1):
        print("*"*5, end=" ")
        print()


if __name__ == '__main__':
    main()
