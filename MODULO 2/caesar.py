#PROBLEMA 2
def validar_llave(clave):
    while True:
        if int(clave)>=0:
            return int(clave)
        else:
            print('Clave incorrecta')
            clave=input('Key: ')

clave= validar_llave(input('Key: '))
plaintext = input('Plaintext: ')

ciphertext=[]
for letra in plaintext:
    if letra == letra.upper():
        abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        abecedario = "abcdefghijklmnopqrstuvwxyz"
    if letra in abecedario:
        ciphertext.append(abecedario[(abecedario.index(letra)+clave) % len(abecedario)])
    if letra==" ":
        ciphertext.append(" ")
    if letra==",":
        ciphertext.append(",")

ciphertext="".join(ciphertext)

print(f'ciphertext: {ciphertext}')