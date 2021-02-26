'''10. Write a program which accept name from user and display length of its
name.
Input : Marvellous Output : 10'''

def main():
    name = input("Enter the name : ")
    cnt = 0
    for i in name:
        cnt+=1
    print(cnt)



if __name__== '__main__':
    main()    
