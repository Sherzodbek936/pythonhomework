def is_prime(n):
    if n<=1:
        print(False)
        return
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(False)
            break
    else:
        print(True)


a=int(input("Enter a positive interger: "))
is_prime(a)