'''5.Write a program which accept N numbers from user and store it into List.
Return addition of all
prime numbers from that List. Main python file accepts N numbers from user
and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum.
Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 +2 + 5) '''

def ChkPrime(l):
    l_prime = []
    for num in l:
   
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               l_prime.append(num)
    return l_prime

def sum_of_ele(list1):
    sum = 0
    for i in list1:
        sum+=i
    return sum
    
    
def main():
    n = int(input("Enter number of elements : "))
    x = list(map(int, input("Input Elements : ").split()))
    l_prime = ChkPrime(x)
    print(l_prime)
    sum_of_primes = sum_of_ele(l_prime)
    
    
    print(f"The sum of primes is {sum_of_primes}")

if __name__ == "__main__":
    main()    
