def digitos(num):
    num_str = str(num)
    cantidad_digitos=len(num_str)
    return cantidad_digitos

numero_ingresado = input("ingresar un numero:")
print("la cantidad total de digitos es:",digitos(numero_ingresado))
