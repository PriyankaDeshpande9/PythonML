'''9. Write a program which accept number from user and return number of
digits in that number.
Input : 5187934 Output : 7'''

def count_of_digits(num):
    cnt=0
    if num>0:
        while num:
            num = num//10
            cnt+=1
        return cnt
            

def main():
    n= int(input("Enter the number : "))
    count = count_of_digits(n)
    print("count of digits in {} is : {}".format(n, count))

if __name__=='__main__':
    main()
