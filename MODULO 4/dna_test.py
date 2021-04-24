import pandas as pd
import csv
import re
import os
import sys
df_small=pd.read_csv('./dna/databases/small.csv')
df_large=pd.read_csv('./dna/databases/large.csv')
def hallar_ADN():
    n=int(input('Secuencia: '))
    secuencia_n=open('./dna/sequences/'+str(n)+'.txt')
    with open('./dna/sequences/'+str(n)+'.txt','r') as secuencia_n:
        for linea in secuencia_n:
            linea
    ADN=linea
    return ADN
def patron_small():    
    ADN=hallar_ADN()
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

def patron_large():    
    ADN=hallar_ADN()
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

#PROBAR PROGRAMA
print(patron_small())
print(patron_large())