def factors(x):
    for i in range(1,x+1):
        if x%i==0:
            print(f"{i} is a factor of {x}")
a=int(input("Enter a positive integer: "))
factors(a)