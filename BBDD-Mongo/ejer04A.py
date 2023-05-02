import json
from random import randint
from pymongo.mongo_client import MongoClient
import os
import platform

NombreCiudades = {"Madrid","Barcelona","Sevilla","Malaga","Cordoba","Toledo","Valencia","Bilbao","Salamanca","Palma","Caceres","Segovia","Zaragoza","Cuenca","Alicante","Las Palmas","Avila","Merida","Granada","Murcia"}

# Create a new database and collection


def connectdb():
    clientDB = MongoClient('mongodb://localhost:27017/')
    db = clientDB.admin
    resultado = db.command('serverStatus')
    print('Host:',resultado['host'])
    print('Version:',resultado['version'])
    print('Process:',resultado['process'])
    print(clientDB.list_database_names())
    return clientDB

#Create a database
def CreateDB(name,clientDB):
    database_name=name
    db=clientDB[database_name]
    return db

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

#Retrieve all the documents
def retrieveAllDocuments(col):
    #asyncronia y multihilo
    result=col.find({}).limit(200)
    for i in result:
        print(i)

# def actualizarCiudades():
#     antiguaCiudad = input("Escriba el nombre de la ciudad que quiere cambiar: ")
#     nuevaCiudad = input("Escriba el nombre de la nueva ciudad: ")
#     for i in NombreCiudades:
#         if NombreCiudades[i] == antiguaCiudad:
#             NombreCiudades[i] = nuevaCiudad
#     return list(NombreCiudades)

# def borrarCiudad():
#     ciudad= set(input("Introduzca la ciudad que quiere borrar: "))
#     for i in NombreCiudades:
#         if NombreCiudades[i] == ciudad:
#             del NombreCiudades[i]
#     return NombreCiudades

def actualizarCiudades(NombreCiudades,antiguaCiudad,nuevaCiudad):
    NombreCiudades.remove(antiguaCiudad)
    NombreCiudades.add(nuevaCiudad)
    print (NombreCiudades)

def borrarCiudad(ciudad):
    NombreCiudades.remove(ciudad)         
    print (NombreCiudades)

def dropColection(col):  
    col.drop()

if __name__ == '__main__':

    clientDB = connectdb()
    db = CreateDB("ciudades_temperaturas", clientDB)
    col = db["ciudades"]

    while True:
        if platform.system() == "Darwin":
            os.system("clear")
        elif platform.system() == "Linux":
            os.system("clear")        
        

        print("\nEstas son las opciones: \n1. Conectar con MongoDB \n2. Crear base de datos \n3. Generar diccionario aleatorio y guardar en disco.\n4. Cargar diccionario del disco.\n5. La ciudad más calurosa \n6. La ciudad más fría \n7. Ciudades ordenadas por temperatura \n8. Crear y guardar un archivo JSON\n9. Actualizar el nombre de una ciudad \n10. Borrar una ciudad de la lista \n11. Recuperar toda la información \n12. Borrar la colección \n13. Salir")
        opcion = input("Seleccione una opción:")
        if opcion == "1":
            clientDB=connectdb()
        elif opcion == "2":
            db=CreateDB('ciudades_temperaturas',clientDB)
        elif opcion == "3":
            diccionario = generar_diccionario()
            guardar_diccionario(diccionario)
        elif opcion == "4":
            diccionario = cargar_diccionario()
        elif opcion == "5":
            print(f"La ciudad más calurosa es: {ciudades_mas_calurosas(diccionario)}")
        elif opcion == "6":
            print(f"La ciudad más fría es: {ciudades_mas_frias(diccionario)}")
        elif opcion == "7":
            print("Ciudades ordenadas por temperatura:")
            for ciudad, temperatura in ciudades_ordenadas_por_temperatura(diccionario):
                print(f"{ciudad}: {temperatura}")
        elif opcion == "8":
            opcion = input("Desea guardar los resultados en un archivo json? (S/N): ")
            if opcion.upper() == "S":
                resultados = {
                    "ciudades_mas_calurosas": ciudades_mas_calurosas(diccionario),
                    "ciudades_mas_frias": ciudades_mas_frias(diccionario),
                    "ciudades_ordenadas_por_temperatura": ciudades_ordenadas_por_temperatura(diccionario)
                }   
                guardar_resultados(resultados)
        elif opcion =="9":
            antiguaCiudad = input("Escriba el nombre de la ciudad que quiere cambiar: ")
            nuevaCiudad = input("Escriba el nombre de la nueva ciudad: ")          
            actualizarCiudades(NombreCiudades,antiguaCiudad,nuevaCiudad)
        elif opcion == "10":
            ciudad = input("Introduzca la ciudad que quiere borrar: ")
            borrarCiudad(ciudad)
        elif opcion == "11":        
            retrieveAllDocuments(col)
        elif opcion == "12":
            dropColection(col)
        elif opcion == "13":
            break
        else:
            print("Opción inválida.")
        follow=input("Press any key to continue...")
