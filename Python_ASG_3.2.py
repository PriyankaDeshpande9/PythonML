'''2.Write a program which accept N numbers from user and store it into List.
Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56'''


def max_of_list(l):
    l.sort()
    return l[-1]

def main():
    n = int(input("Enter number of elements : "))
    x = list(map(int, input("Input Elements : ").split()))

    max_no = max_of_list(x)
    
    print("The max element of list is : {}".format(max_no))

if __name__ == "__main__":
    main()
