altura=input("Ingrese la altura: ")
while True:
    try:
        altura=int(altura)
        if altura>0 and altura<9: 
            for i in range(altura+1):
                espacios=altura-i
                print(" "*espacios+"#"*i)
            break
        else:
            altura=int(input("Ingrese la altura entre 1 y 8: "))     
    except:
        altura=input("Ingrese una altura correcta: ")