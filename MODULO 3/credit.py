def generar_tarjeta():
    tarjeta=[]
    numeros = input('Number: ')
    for numero in numeros:
        tarjeta.append(int(numero))
    return tarjeta

def identificar_tarjeta(tarjeta):
    if tarjeta[0:2]==[3,4] or tarjeta[0:2]==[3,7]:
        return 'AMEX\n'
    elif tarjeta[0:2]==[5,1] or tarjeta[0:2]==[5,2] or tarjeta[0:2]==[5,3] or tarjeta[0:2]==[5,4] or tarjeta[0:2]==[5,5]:
        return 'MasterCard'
    elif tarjeta[0]==4:
        return 'VISA\n'
    else:
        return 'INVALID\n'

def algoritmo_luhn(tarjeta):
    tarjeta=tarjeta[::-1]
    suma1=0
    suma2=0
    for index, valor in enumerate(tarjeta):
        if index%2==1:
            valor=valor*2
            if valor>=10:
                valor=valor%10
                suma1=suma1+valor-1
            suma1=suma1+valor
        elif index%2==0:
            if valor>=10:
                valor=valor%10
                suma2=suma2+valor-1
            suma2=suma2+valor

    return suma1+suma2
            
x=generar_tarjeta()
print(identificar_tarjeta(x))
print(algoritmo_luhn(x))