mesIngresado= input("Digite el mes del año : ")
mes= mesIngresado.lower()

if(mes == 'enero' or 'febrero' or 'marzo'):
    print(f'{mes}Esta en la estación del año INVIERNO')
elif(mes== 'abril' or 'mayo' or 'junio'):
    print(f'{mes}Esta en la estación del año PRIMAVERA')
elif(mes== 'julio' or 'agosto' or 'septiembre'):
    print(f'{mes}Esta en la estación del año VERANO')
elif(mes== 'octubre' or 'novimebre' or 'diciembre'):
    print(f'{mes}Esta en la estación del año OTOÑO')
else:
    print("El mes ingresado no es valido")