'''6. Write a program which accept one number and display below pattern.
Input : 5
Output :
* * * * *
* * * *
* * *
* *
*
'''

def pattern(n):
    for i in range(1,n+1):
        #print(i)
        for j in range(n+1,i,-1):
            print("*", end=" ")
        print()

def main():
    n = int(input("Enter the number : "))
    pattern(n)


if __name__=='__main__':
    main()
