edad=int(input("ingrese su edad :"))

if(edad>= 0 and edad<14):
    print(f'Usted esta en el rango de edad NIÑO')
elif(edad>14 and edad<28):
    print(f'Usted esta en el rango de edad JOVEN')
elif(edad>28 and edad<60):
    print(f'Usted esta en el rango de edad ADULTO')
elif(edad>60):
    print(f'Usted esta en el rango de edad MAYOR')

else:
    print("La edad ingresada no es valida")