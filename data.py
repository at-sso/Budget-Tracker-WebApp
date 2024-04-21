import pymongo
from datetime  import datetime

myclient  = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb= myclient["presupuesto"]

collectionGastos = mydb["Gastos"]
collectionIngresos =  mydb["Ingresos"]

def registrar_ingresos():
    """Registrar un ingreso en la base de datos"""
    descripcion = input ("Descripción del Ingreso: ")
    monto = float(input("Monto del Ingreso: "))
    fecha = datetime.now().strftime("%d/%m/%Y")
    new_item = {"fecha":fecha,"descripcion":descripcion, "monto":monto}
    collectionIngresos.insert_one(new_item)
    print("Se ha agregado el ingreso correctamente.")

def mostrar_ingresos():
    """Imprimir todos los ingresos almacenados en la base de datos"""
    for ingreso in collectionIngresos.find():
        #print (f"Detalle del ingreso : {ingreso["Descripcion"]}, Monto del gasto : {ingreso["Monto"]} Fecha del gasto : {ingreso["Fecha"]}")
        print(ingreso)

def eliminar_ingresos():
    """Eliminar un ingreso de la base de datos"""
    # Buscar y mostrar todos los registros
    id_del = input ("Digite el ID del gasto a eliminar: ")
    collectionIngresos.delete_one( {'_id': id_del } )
    print("Se ha eliminado el ingreso correctamente.")

def modificar_ingresos():
    """Modificar un ingreso existente en la base de datos"""  
    id_del = int (input ("Digite el ID del ingreso a Modificar: "))
    descripcion = input ("Nueva Descripción del Ingreso: ")
    monto = float(input("Nuevo Monto del Ingreso: "))
    fechadelcambio = datetime.now().strftime("%d/%m/%Y")
    filtro = { '_id' : id_del }  
    collectionIngresos.update_one(filtro, { '$set': { 'descripcion': descripcion , 'monto': monto , 'fecha de cambio': fechadelcambio}})
    documetoactual = collectionIngresos.find_one(filtro)
    # Verificamos que se haya encontrado al menos un documento con ese ID
    if documetoactual is None:
        print("No se ha encontrado ningun ingreso con ese ID")
    else:
        # Creamos una copia del diccionario para no perder los valores originales
        dict_original = documetoactual.copy()
        # Actualizamos el diccionario con los nuevos valores
        dict_original ["descripcion"] = descripcion
        dict_original ["monto"] = monto
        dict_original ["fecha de cambio"]= fechadelcambio
        # Realizamos la actualización en la base de datos
        collectionIngresos.replace_one(filtro ,dict_original)
        print("Se han actualizado los datos del ingreso correctamente.")

def  registrar_gastos():
    nombre  = input('Ingrese el detalle del gasto :')
    monto   = float(input('Ingrese la cantidad a gastar :'))
    fecha   = datetime.now().strftime("%d/%m/%Y")
    gasto =      {"nombre":nombre,"monto":monto,"fecha":fecha}
    collectionGastos.insert_one(gasto)
    print("Se ha agregado el gasto a la base de datos.")

def  mostrar_gastos():
    for gasto in collectionGastos.find():
        print (f"id del gasto {gasto['_id']} Detalle del Gasto : {gasto['nombre']} Monto del gasto : {gasto['monto']} Fecha del gasto : {gasto [ 'fecha']}")
        

def  eliminar_gasto():
    idgasto = input ("Digite el ID del gasto que desea eliminar ")
    collectionGastos.delete_many({"_id ":idgasto})
    print("El gasto fue eliminado correctamente")

def actualizar_gasto():
    buscarID = input ('Busque por su ID para actualizar ')
    filtro = {'_id':buscarID }
    #recupero los datos del registro a editar
    datoActual = collectionGastos.find_one(filtro)
    if datoActual is None :
        print("No se encontro el registro con ese ID")
    else:
        #muestro los datos originales
        print(f'Detalle del Gasto Original:\n Nombre : {datoActual ["nombre"]}\n Monto : {datoActual ["monto"]}\n Fecha : {datoActual ["fecha"]}')

