def operaciones(num1, num2, operation):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error!: No se puede dividir por 0."

num1: int = int(input("Ingresa tu primer número: "))
num2: int = int(input("Ingresa tu segundo número: "))
print("\nSuma seleccione: 1 ")
print("Resta seleccione: 2 ")
print("Multiplicacion seleccione: 3 ")
print("Division seleccione: 4 ")
operation = int(input("\nSelecciona el tipo de operación: "))

print(operaciones(num1, num2, operation))

