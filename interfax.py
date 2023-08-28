a = "candena"
b = "12"
c = "3.1415"
d = "true"
e = a + " " + b + " " + c + " " + d
print(e)
ej_int = 10 ** 1000  #el limite hasta donde la memoria lo permita
print (ej_int)
max_float = 1.8e308  #el valor maximo que un flotante puede representar al rededor (1.8e308)
print (max_float)

#respuesta 3.3
# k mod 2 == 0 => k es par
"""
Generar los n primeros pares.
"""
def generar_numeros_pares(n=50):
    pares = []
    
    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1

            numero += 1

    return pares        

n = int(input('Escriba la cantidad de n numeros pares a generar: '))

if n > 0:
    pares = generar_numeros_pares(n)

    print(pares)
    print('cantidad de pares:', len (pares))
else:
    print('El numero debe der par')    




    




