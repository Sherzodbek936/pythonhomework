a=input("enter a password: ")
b='QWERTYUIOPASDFGHJKLZXCVBNM'
if len(a)<8:
    print("Password is too short.")
else:
    for i in a:
        if i in b:
            print("Password is strong")
            break
        else:
            print("Password must contain an uppercase letter.")
            break

