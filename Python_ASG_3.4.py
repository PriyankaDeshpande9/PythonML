'''4.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3 '''

def countX(l,x):
    count = 0
    for i in l:
        if i == x:
            count+=1
    return count

def main():
    n = int(input("Enter number of elements : "))
    x = list(map(int, input("Input Elements : ").split()))
    no = int(input("Element to search : "))

    cnt = countX(x, no)
    
    print(f"The {no} appeared {cnt} times")

if __name__ == "__main__":
    main()
