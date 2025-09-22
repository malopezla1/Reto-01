def mayor_suma(lista_nums):
    if len(lista_nums) < 2:
        return None
    mayor = lista_nums[0] + lista_nums[1]
    for i in range(1, len(lista_nums) - 1):
        suma = lista_nums[i] + lista_nums[i + 1]
        if suma > mayor:
            mayor = suma
    return mayor

entrada_usuario = input("Ingresa los números de la lista separados por comas: ")
lista_nums = [int(numero) for numero in entrada_usuario.split(',')]   

print("La mayor suma de dos números consecutivos es: ", mayor_suma(lista_nums))
