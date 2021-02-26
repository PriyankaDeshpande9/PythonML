'''3.Write a program which accept N numbers from user and store it into List.
Return Minimum
number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5 '''


def min_of_list(l):
    l.sort()
    return l[0]

def main():
    n = int(input("Enter number of elements : "))
    x = list(map(int, input("Input Elements : ").split()))

    min_no = min_of_list(x)
    
    print("The max element of list is : {}".format(min_no))

if __name__ == "__main__":
    main()
