'''7. Write a program which contains one function that accept one number from
user and returns true if number is divisible by 5 otherwise return false.
Input : 8 Output : False
Input : 25 Output : True'''

def main():
    n = int(input("Enter the number : "))
    if n%5==0:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
