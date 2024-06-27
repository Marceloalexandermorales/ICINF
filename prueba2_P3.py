capitales_paises = {}

print("ingrese 5 capitales y sus paises.")
for i in range(5):
    capital = input("ingrese la capital: ")
    pais = input("ingrese el pais de la capital: ")
    capitales_paises[capital] = pais

print("capitales y paises ingresados:")
print(capitales_paises)

nombre_turista = input("Ingrese el nombre del turista: ")
capital_turista = input("Ingrese la capital de procedencia del turista: ")

pais_turista = "desconocido"
if capital_turista in capitales_paises:
    pais_turista = capitales_paises[capital_turista]

print("El turista con el nombre " + nombre_turista + " viene de la capital " + capital_turista + " y su país es " + pais_turista + ".")
