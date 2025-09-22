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