#print("You are in the quadratic equation calculator.\nChoose which of your equations is:\n1. Complete \n2. Incomplete")
#ope = input("Select the equation: ")
#a = float(input("Zmina A: "))
#b = float(input("Zmina B: "))
#c = float(input("Zmina C: "))
#f = float(input("Result equation: "))
#def nyav(a,b,c):
    #is=b**2-4*a*c
    #if dis > 0:
        #print("HI")

import cmath

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
        imaginary_part = cmath.sqrt(abs(dis)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

roots = complete_quadratic_equation(a, b, c)
print("Roots:", roots)
