def validar_clave(clave):
    while True:
        if len(clave)==26:
            return clave
        else:         
            print('La clave es incorrecta')
            clave=input('Ingrese una nueva clave: ')


def salida(ciphertext):
    if plaintext==plaintext.lower():
        ciphertext=ciphertext.lower()
        return ciphertext
    if plaintext==plaintext.upper():
        ciphertext=ciphertext.upper()
        return ciphertext
    else: 
        return ciphertext

abecedario='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
clave= validar_clave(input('Key: '))
plaintext=input('Plaintext: ')
ciphertext=[]
new_p=plaintext.upper()
for caract in new_p:
    for index1,letra in enumerate(abecedario):
        if caract==letra:
            ciphertext.append(clave[index1])
    if caract==" ":
        ciphertext.append(" ")
    elif caract==",":
        ciphertext.append(",")        
ciphertext="".join(ciphertext)
print(f'Ciphertext: {salida(ciphertext)}')