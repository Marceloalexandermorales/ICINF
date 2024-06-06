lista_palabras = []

while True:
    palabra = input("Ingrese una palabra (o presione Enter para finalizar): ")

    if palabra == "":
        break

    lista_palabras.append(palabra)

max_longitud = 0

for palabra in lista_palabras:
    if len(palabra) > max_longitud:
        max_longitud = len(palabra)

print("La palabra con la mayor cantidad de caracteres tiene", max_longitud, "caracteres.")