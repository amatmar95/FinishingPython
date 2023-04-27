import json
from random import randint
import pymongo
import os
import platform

NombreCiudades = {"Madrid","Barcelona","Sevilla","Malaga","Cordoba","Toledo","Valencia","Bilbao","Salamanca","Palma","Caceres","Segovia","Saragoça ","Cuenca","Alicante","Las Palmas","Avila","Merida","Granada","Murcia"}

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a new database and collection
db = client["temperaturas"]
col = db["ciudades"]

def generar_diccionario():
    for i in NombreCiudades:
        media_temperaturas = sum(randint(-10, 40) for j in range(12))
        ciudades = {
            "ciudad": i,
            "temperatura": media_temperaturas / 12
        }
        col.insert_one(ciudades)

def guardar_diccionario(ciudades):
    with open('ciudades.json', 'w') as f:
        json.dump(ciudades, f)

def cargar_diccionario():
    diccionario = {}
    for ciudad in col.find():
        diccionario[ciudad["ciudad"]] = ciudad["temperatura"]
    if not diccionario:
        diccionario = generar_diccionario()
    return diccionario

def ciudades_mas_calurosas(diccionario):
    max_temperatura = max(diccionario.values())
    return [ciudad for ciudad, temperatura in diccionario.items() if temperatura == max_temperatura]

def ciudades_mas_frias(diccionario):
    min_temperatura = min(diccionario.values())
    return [ciudad for ciudad, temperatura in diccionario.items() if temperatura == min_temperatura]

def ciudades_ordenadas_por_temperatura(diccionario):
    return sorted(diccionario.items(), key=lambda x: x[1], reverse=True)

def guardar_resultados(resultados):
    with open('resultados.json', 'w') as f:
        json.dump(resultados, f)

def main():
    while True:
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin":
            os.system("clear")
        elif platform.system() == "Linux":
            os.system("clear")        
        opcion = input("Seleccione una opción:\n1. Generar diccionario aleatorio y guardar en disco.\n2. Cargar diccionario del disco.\n3. \n4. \n5. \n6. \n7.")
        if opcion == "1":
            diccionario = generar_diccionario()
            guardar_diccionario(diccionario)
        elif opcion == "2":
            diccionario = cargar_diccionario()
        elif opcion == "3":
            print(f"Las ciudades más calurosas son: {ciudades_mas_calurosas(diccionario)}")
        elif opcion == "4":
            print(f"Las ciudades más frías son: {ciudades_mas_frias(diccionario)}")
        elif opcion == "5":
            print("Ciudades ordenadas por temperatura:")
            for ciudad, temperatura in ciudades_ordenadas_por_temperatura(diccionario):
                print(f"{ciudad}: {temperatura}")
        elif opcion == "6":
            opcion = input("Desea guardar los resultados en un archivo json? (S/N): ")
            if opcion.upper() == "S":
                resultados = {
                    "ciudades_mas_calurosas": ciudades_mas_calurosas(diccionario),
                    "ciudades_mas_frias": ciudades_mas_frias(diccionario),
                    "ciudades_ordenadas_por_temperatura": ciudades_ordenadas_por_temperatura(diccionario)
                }   
                guardar_resultados(resultados)
        elif opcion == "7":
            break
        else:
            print("Opción inválida.")
            return
    if __name__ == '__main__':
        main()
