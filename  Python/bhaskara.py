a = b = c = xm = xn = d = r = dn = 0

a = float(input("Digite valor de a: "))
b = float(input("Digite valor de b: "))
c = float(input("Digite valor de c: "))

d = ((b*b)-(4*a*c))
print("Delta: ",d)

if  d<0:
    dn = -(d)
    r = d**(1/2)
    print("Raiz de Delta: ", r)
    xm = ((-b + (r)) / (2*a))
    print("O valor de X1 é: ", xm, "!")
    xn = ((b - (r)) / (2*a))
    print("O valor de X'' �: ", xn, "!")

else:
     r = d** (1/2)
     print("Raiz de Delta:",r)
     xm = ((-b + (r)) / (2*a))
     print("O valor de X' é: ", xm)
     xn = ((-b - (r) ) / (2*a))
     print("O valor de X'' é: ",xn)