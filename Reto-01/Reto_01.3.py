def result(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primos = []

for numero in lista:
    if result(numero):
        primos.append(numero)

print(f"Estos son los numeros primos en la lista: {primos}")