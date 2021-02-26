'''7. Write a program which accept one number and display below pattern.
Input : 5
Output : 1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''


def pattern(n):
    for i in range(1, n+1):
        for j in range(1,n+1):
            print(j, end=" ")
        print()

def main():
    num_rows = int(input("Enter the number : "))
    pattern(num_rows)
        
if __name__ == '__main__':
    main()
