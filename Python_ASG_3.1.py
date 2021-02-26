'''1.Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130'''


def sum_of_ele(list1):
    sum = 0
    for i in list1:
        sum+=i
    return sum

def main():
    n = int(input("Enter number of elements : "))
    x = list(map(int, input("Input Elements : ").split()))

    total = sum_of_ele(x)
    
    print("The sum of elements is : {}".format(total))

if __name__ == "__main__":
    main()
