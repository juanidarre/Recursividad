#Ejercicio 1:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

limite = int(input("Ingrese un numero: "))
for i in range(1, limite + 1):
    print(f"Factorial de {i}: {factorial(i)}")

#Ejercicio 2:
def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    if posicion == 1:
        return 1
    return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

n = int(input("Ingrese la posicion final: "))
for i in range(n + 1):
    print(f"Posición {i}: {fibonacci_recursivo(i)}")

#Ejercicio 3:
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

print(potencia(2, 3))

#Ejercicio 4:
def decimal_a_binario(n):
    if n == 0:
        return "" 
    return decimal_a_binario(n // 2) + str(n % 2)

print(decimal_a_binario(10))

#Ejercicio 5:
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print(es_palindromo("radar"))

#Ejercicio 6:
def suma_digitos(n):
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1234))

#Ejercicio 7:
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(4))

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincide = 1 if (numero % 10) == digito else 0
    
    return coincide + contar_digito(numero // 10, digito)

print(contar_digito(12233421, 2))