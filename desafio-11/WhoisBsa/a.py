limite = 1000
numero = 2
c = 1
p = 0
print ("Primos: ")
while numero < 10:
    i = numero -1
    while i > 1:
        if numero % i == 0: break
        i -= 1
        c += 1
    else:
        print (numero)
        p += 1
    numero += 1

print ("\n\nForam encontrados %d números primos." %p)
print ("Foram necessárias %d comparações." %c)