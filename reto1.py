#ENTRADAS=VARIABLES=REFERENCIAS EN MEMORIA
#Solo mayuscula la primera, inicializar varible, se declara y asigna valor
#None: indica que no lleva nada... Quemar ..jarcorear

nivelAgua=int(input("Digite el nivel de agua: "))


#PROCESOS
#Definir rangos....elif
#Switch no analiza rangos si no estados, no existe en python
#Operadores logicos Negación - Y(Incluye)&& --and - O(excluye)

if(nivelAgua>=0 and nivelAgua<20):
    #SALIDAS
    print(f'El nivel de agua es {nivelAgua} y este es bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    #SALIDAS
    print(f'El nivel de agua es {nivelAgua} operando normalmente')
elif(nivelAgua>=400):
    #SALIDAS
    print(f'El nivel de agua es {nivelAgua} llamen a FICO Y LUPE')
else:
    #SALIDAS
    print("El nivel del agua no es valido")

#SALIDAS