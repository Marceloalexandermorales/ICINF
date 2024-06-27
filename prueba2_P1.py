notas = []

print("ingresar las notas, para terminar ingresar 0")

while True: 
   nota = float(input("ingresar nota: "))
   if nota == 0:
       break
   notas.append(nota)
   
   
cantidad_notas=len(notas)
if cantidad_notas > 0:
    promedio_notas = sum(notas) / cantidad_notas
else:
    promedio_notas = 0

notas_bajo_4 = len([nota for nota in notas if nota < 4.0])
notas_igual_o_mayor_4 = len([nota for nota in notas if nota >= 4.0])

print("1) Cantidad de notas: ")
print(cantidad_notas)
print("2) Promedio de notas: ")
print(promedio_notas)
print("3) Cantidad de notas bajo nota 4.0: ")
print(notas_bajo_4)
print("4) Cantidad de notas igual o mayor que nota 4.0: ")
print(notas_igual_o_mayor_4)