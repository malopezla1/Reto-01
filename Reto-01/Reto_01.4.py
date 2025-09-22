def mayor_suma(lista):
    if len(lista) < 2:
        return None
    mayor = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        suma = lista[i] + lista[i + 1]
        if suma > mayor:
            mayor = suma
    return mayor

lista = [1, 2, 3, 10, 8, 5, 11, 2]
print("La mayor suma de dos números consecutivos es: ", mayor_suma(lista))
