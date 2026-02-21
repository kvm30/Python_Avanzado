##Usamos funciones para organizar el código


#PARADIGMA PROCEDURAL


def registrar_entrada(lista, placa):
    #Agrega un vehículo a la lista
    lista.append(placa)

def registrar_salida(lista, placa):
    #Elimina vehículo si existe
    if placa in lista:
        lista.remove(placa)


vehículos = []

registrar_entrada(vehículos, "AAA111")
registrar_entrada(vehículos, "BBB222")

print("Vehículos:", vehículos)

registrar_salida(vehículos, "AAA111")

print("Después salida", vehículos)

#esto es un comentario 