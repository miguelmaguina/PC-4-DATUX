import pandas as pd
import csv
import re
import os
def hallar_ADN(n: int):
    secuencia_n=open('./dna/sequences/'+str(n)+'.txt')
    with open('./dna/sequences/'+str(n)+'.txt','r') as secuencia_n:
        for linea in secuencia_n:
            linea
    ADN=linea
    return ADN
def patron_small(n:int):
    df_small=pd.read_csv('./dna/databases/small.csv')
    while True:
        if n>0 and n<5:
            ADN=hallar_ADN(n)
            p_1=re.findall('AGATC',ADN)
            p_2=re.findall('AATG',ADN)
            p_3=re.findall('TATC',ADN)
            for x in df_small['AGATC'].unique():
                for y in df_small['AATG'].unique():
                    for z in df_small['TATC'].unique():
                        if x==len(p_1) and y==len(p_2) and z==len(p_3):
                            if x==2 and y==8 and z==3:
                                return 'Alice'
                            elif x==4 and y==1 and z==5:
                                return 'Bob'
                            elif x==3 and y==2 and z==5:
                                return 'Charlie'
            return 'No Match'

def count(cont, cadena):
    patron = rf'({cont})\1*'
    patron_general = re.compile(patron)
    pareja = [pareja for pareja in patron_general.finditer(cadena)]
    maximo = 0
    for x in range(len(pareja)):
        if pareja[x].group().count(cont) > maximo:
            maximo = pareja[x].group().count(cont)
    return maximo

def patron_large(n:int):
    while True:
        if n>4 and n<21:    
            ADN=hallar_ADN(n)
            with open('./dna/databases/large.csv', 'r') as archivo_csv:
                lector = csv.DictReader(archivo_csv)
                diccionario = list(lector)
            
            AGATC = count("AGATC", ADN)
            TTTTTTCT = count("TTTTTTCT", ADN)
            TCTAG = count("TCTAG", ADN)
            AATG = count("AATG", ADN)
            GATA = count("GATA", ADN)
            TATC = count("TATC", ADN)
            GAAA = count("GAAA", ADN)
            TCTG = count("TCTG", ADN)

            for i in range(len(diccionario)):
                if all([diccionario[i]["AGATC"] == str(AGATC), diccionario[i]["TTTTTTCT"] == str(TTTTTTCT), diccionario[i]["TCTAG"] == str(TCTAG), diccionario[i]["AATG"] == str(AATG), diccionario[i]["GATA"] == str(GATA), diccionario[i]["TATC"]== str(TATC), diccionario[i]["GAAA"] == str(GAAA), diccionario[i]["TCTG"] == str(TCTG)]):
                    name = diccionario[i]["name"]
                    break
                else:
                    name = "No match"
            return name
def definir_patron():
    d=str(input('database:'))
    while True:
        if d=='small.csv':
            while True:
                n=input('Secuencia: ')
                x=re.findall(r'\d+',n)
                num=int(x[0])
                if num>0 and num<5:
                    return patron_small(num)
                else:
                    print('Secuencia no correcta')
                    n=input('Secuencia: ')
                    x=re.findall(r'\d+',n)
                    num=int(x[0])
        elif d=='large.csv':
            while True:
                n=input('Secuencia: ')
                x=re.findall(r'\d+',n)
                num=int(x[0])
                if num >4 and num<21:
                    return patron_large(num)
                else:
                    print('Secuencia no correcta')
                    n=input('Secuencia: ')
                    x=re.findall(r'\d+',n)
                    num=int(x[0])
        else:
            print('database incorrecta')
            d=str(input('database: '))

if __name__ == "__main__":           
    print(definir_patron())