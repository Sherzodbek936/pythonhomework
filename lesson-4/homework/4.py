import random
while True:
    son=random.randint(1,100)
    b=10

    for i in range(b):
        a=int(input("son="))
        if a>son:
            print("Too high!")
        elif a<son:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
    c = input("Want to play again?: ")
    if c not in ('y', 'yes', 'ok','YES','Y'):
            break
