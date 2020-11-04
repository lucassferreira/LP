from math import *

try:
    hipot = int(input("Hipotenusa: "))
    cat1= int(input("Cateto1: "))
    cat2 = int(input("Cateto2: "))
except:
    print("\nDigite apenas inteiros!")
    input()
if  hipot > cat1 + cat2:
    print("\nNão é um triangulo!")
elif (cat1 > 0 and cat2 > 0):
    print("\nÉ um triangulo")

    s = (hipot + cat1 + cat2) / 2

    area = sqrt(s * (s - hipot) * (s - cat1) * (s * cat2))

    print("Área do triângulo: {:.2f}.".format(area))
