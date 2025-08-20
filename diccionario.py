# agenda = {
#     "Ana": "3011122330", 
#     "Bruno": "3022233440",
#     "Carla": "3003399881",
# }

# #mosatrar el numero de un contacto en especifico 
# """
# print("Telefono de bruno:", agenda["Bruno"])
# """



# nombre = input("Ingrese el nombre de la persona: ")
# #Numero de contacto especifico 


# if nombre in agenda:
#     print("si está", nombre, agenda[nombre])
# else:
#     print("No está")
#     telefono = input("ingrese el Telefono")
#     agenda[nombre] = telefono
#     print("agregado")
# # diccionario completo 
# print("Diccionario completo", agenda)

estudiantes = {
    "Lucia": [4.5, 3.8, 4.2],
    "Mateo": [3.0, 3.5, 4.0, 4.2],
    "Sofia": [5.0, 4.8, 4.9],
}
del estudiantes["Mateo"] # se elimina algo de el diccionario
promedios = {}
for nombre, notas in estudiantes.items(): #sirve para recorrer todo el diccionario, y el .items es solo para diccionarios y ocaciona que lo recorra
    prom = sum(notas) / len(notas) # suma y divide por cuantos items hay para sacar promedio
    print(f"Promedio de {nombre}: {prom:.2f}")
    promedios[nombre] = prom # agrega todos los valores al diccionario

print(promedios)

mejor_estudiante = max(promedios, key =promedios.get) # escoge el mayor numero 
print(mejor_estudiante)