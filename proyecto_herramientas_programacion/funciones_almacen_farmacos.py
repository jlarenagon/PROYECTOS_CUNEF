import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def cargar_json(nombre):
    ruta = os.path.join(BASE_DIR, nombre)
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

DATA_ALMACEN = cargar_json("almacen-1.json")["almacen"]
DATA_FARMACOS = cargar_json("farmacos-1.json")


def nombre_farmaco(codigo):
    return print(DATA_FARMACOS.get(codigo, {}).get("nombre_comercial", f"(Desconocido: {codigo})"))


def tipo_farmaco(codigo):
    return print(DATA_FARMACOS.get(codigo, {}).get("tipo"))

def temperatura_farmaco(codigo):
    return print(DATA_FARMACOS.get(codigo, {}).get("temperatura_requerida"))

def stock_farmaco(codigo):
    encontrados = []
    for modulo, datos in DATA_ALMACEN.items():
        stock_modulo = datos.get("stock", {})
        if codigo in stock_modulo:
            cantidad = stock_modulo[codigo]
            encontrados.append(cantidad)
    return print(modulo) , print(encontrados[0])

def modulos():
    print("=== Módulos del almacén ===")
    for id in DATA_ALMACEN.keys():
        print(id) 

def estado_modulos():
    print("=== Módulos del almacén ===")
    for mod_id, info in DATA_ALMACEN.items():
        cap = info["capacidad_maxima"]
        temp = info["temperatura"]
        stock = info["stock"]
        ocupacion = sum(stock.values())
        print(f"- {mod_id}: Temp {temp}°C | Capacidad {cap} | Ocupación {ocupacion}/{cap}")

