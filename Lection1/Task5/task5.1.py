import math

def complete_quadratic_equation(a, b, c):
    dis = b**2 - 4*a*c
    if dis > 0:
        root1 = (-b + dis**0.5) / (2*a)
        root2 = (-b - dis**0.5) / (2*a)
        return root1, root2
    elif dis == 0:
        root = -b / (2*a)
        return root,
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(dis)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

a = float(input("enter coefficient a: "))
b = float(input("enter coefficient b: "))
c = float(input("enter coefficient c: "))

roots = complete_quadratic_equation(a, b, c)
print("Roots:", roots)
