# Reto-01

En el siguiente repositorio encontrara la resolución de los 5 retos de programación basica de la clase 4 de POO semestre 2025-2, con su breve descripción de como se llego a ese codigo.

# Reto 1.1: 

Cree una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función serán los dos operandos y el carácter usado para la operación. entrada: (1,2,"+") , salida (3).

# Codigo

``` Python 
def operaciones(num1: float, num2: float, operation: float):
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

num1: float = int(input("Ingresa tu primer número: "))
num2: float = int(input("Ingresa tu segundo número: "))
print("\nSuma seleccione: 1 ")
print("Resta seleccione: 2 ")
print("Multiplicacion seleccione: 3 ")
print("Division seleccione: 4 ")
operation = int(input("\nSelecciona el tipo de operación: "))

print(operaciones(num1, num2, operation))
```
# Explicación:

Es bastante basico, ya que es una calculadora de operaciones basicas, en la cual simplemente declaro la variable de los 2 números (```num1``` y ```num2```) que quiero operar y otra que almacena el resultado (```operation```) y el tipo de operación que se va a ejecutar, asi con esto solo queda hacer un pequeño menú de selección para el usuario, que primero ingresa sus 2 números y despues selecciona la operación que quiere realizar.

# Reto 1.2: 

Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

# Codigo:
``` Python
def palindromo (word):
    word = word.lower()
    inverted = ""
    for letter in word:
        inverted = letter + inverted
    return word == inverted

word = input("Ingrese una palabra: ")
if palindromo(word):
    print("Es un palíndromo")
else: 
    print("No es un palíndromo")
```
# Explicación:

La variable ```word``` almanecara la palabra que ingrese el usuario, a la cual se le aplica la función lower para que asi se trabajen todos los caracteres en minúsculas y no halla confución a la hora de comparar por letras en mayúscula o minúscula, en consiguiente, se crea la variable ```inverted``` que no almacena nada por el momento, al crear un ciclo ```for``` se vuelve a almacenar en esa variable la palabra pero escrita al reves, al final solo se compara si la palabra inicial (```word```) y la palabra invertidad (```inverted```) son iguales y se define como palíndromo o no.

# Reto 1.3:

Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

# Codigo:
``` Python
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
```
# Explicación:

Se sabe que cualquier número menor de 2 no sera primo, entonces se trabaja en un bucle ```if``` de 2 hasta el límite de la lista antes del número tomado a evualuar, en el cual se selecciona un número ```num``` al cual se le aplicara el "modulo": ```%```, y ademas de esto ```i``` recorrera los número hasta ```n-1``` y si con cualquier número el resultado es 0 quiere decir que aquel número no sera primo, si no existe tal número que de en el resultado igual a cero entonces es un número primo, ya por ultimo se crea otro ciclo ```for``` donde se usa la función creada y retorna solo los números primos. 

# Agregado: 

``` Python
entrada_usuario = input("Ingresa los números de la lista separados por comas: ")
lista_nums = [int(numero) for numero in entrada_usuario.split(',')]    
```
Con estas 2 líneas de codigo, se puede reemplaza la linea ```lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]```, para que el usuario pueda ingresar su propia lista a revisión, aunque el nombre de las variables es a gusto personal. 

# Reto 1.4:

Escribir una función que reciba una lista de números enteros y devolver la mayor suma entre dos elementos consecutivos.

# Codigo:
``` Python
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
```
# Explicación:

Se crea una función que recibe una lista de números, el primer ciclo ```if``` permite hacer un filtro en el que si una lista es menor a 2 entonces no se retornara nada. Para poder encontrar el número mayor de 2 números consecutivos se empieza a recorrer la lista desde el primer número (```lista_nums[0]```) y sumandole el siguiente (```lista_num[1]```), este resultado se almacena en la variable ```mayor```, despues de esto se termina de recorrer la lista elemento por elemento hasta llegar a la suma final, si alguna suma supera a la anterior entonces esta se almacena como la nueva suma ```mayor```, si ninguna otra suma pasa este valor, entonces se termina retornando este, puesto que es el resultado mayor.

# Reto 1.5:
Escribir una función que reciba una lista de cadenas y retorne únicamente aquellos elementos que tengan los mismos caracteres. por ejemplo entrada: ```["amor", "roma", "perro"]```, salida```["amor", "roma"].```

# Codigo:
``` Python
def same_letters(lista):
    result = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if sorted(lista[i]) == sorted(lista[j]):
                if lista[i] not in result:
                    result.append(lista[i])
                if lista[j] not in result:
                    result.append(lista[j])
    return result

entrance = input("Ingresa las palabras separadas por comas: ")
lista_words = [palabra.strip() for palabra in entrance.split(',')]

print(f"Palabras con los mismos caracteres: {same_letters(lista_words)}")
```
# Explicación: 

La variable ```result```, se encarga de almacenar las palabras que tengan los mismos caracteres en la función, luego simplemente se recorren los caracteres de la función en un ciclo ```for``` y se ordenan con ```sorted()```, por lo que si la palabra lista ```i``` es igual a la palabra en la lista ```j```, entonces se agregan a la variable ```result```, si no son iguales no se agregaran, lo mismo si ya hacen parte de la lista, evitando asi duplicados, dando como resultado que la función retorna solo aquellos elementos que son "anagramas".

# Conclusión:

Cada uno de los retos puestos en clase, permito recordar cosas claves, como el manejo de strings y funciones de estas importantes como ```sorted()``` o ```.lower()```, asi mismo como el desarrollo de la logica de programación en listas y aritmetica, desde lo mas sencillo como una pequeña calculadora de 2 números con operadores basicos, hasta algo mucho mas complejo como la comparación de caracteres de cada string de una lista para encontrar cuales son anagramas.
