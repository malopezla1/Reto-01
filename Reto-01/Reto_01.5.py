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

entrance = ["roma", "amor", "perro"]
print(same_letters(entrance))