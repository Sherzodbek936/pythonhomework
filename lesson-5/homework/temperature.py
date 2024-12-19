def convert_cel_to_far(C):
    print(f"{C} degrees C = {C * 9/5 + 32:.2f} degrees F ")
a=float(input("Enter a temperature in degrees C: "))
convert_cel_to_far(a)

def convert_far_to_cel(F):
    print(f"{F} degrees F = {(F - 32) * 5/9:.2f} degrees C ")
b=float(input("Enter a temperature in degrees F: "))
convert_far_to_cel(b)