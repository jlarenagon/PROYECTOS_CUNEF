import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def cargar_json(nombre):
    ruta = os.path.join(BASE_DIR, nombre)
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_json(nombre, data):
    ruta = os.path.join(BASE_DIR, nombre)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

DATA_PEDIDOS = cargar_json("pedido.json")


def pedido_en_proceso():    
    print("Pedidios en proceso")
    print("-----------------------------------------------------------------")    
    for pedido in DATA_PEDIDOS:
        estado = pedido.get("estado_pedido", pedido.get("estado", ""))
        if estado == "en proceso":
            cliente = pedido["cliente"]["nombre"]
            print(f"- {pedido['pedido_id']} | Cliente: {cliente} | Fecha: {pedido['fecha']}")

def pedido_por_procesar():        
    print("Pedidios por procesar")
    print("-----------------------------------------------------------------")
    for pedido in DATA_PEDIDOS:
        estado = pedido.get("estado_pedido", pedido.get("estado", ""))
        if estado == "por procesar":
            cliente = pedido["cliente"]["nombre"]
            print(f"- {pedido['pedido_id']} | Cliente: {cliente} | Fecha: {pedido['fecha']}")

def procesar_pedido(archivo="pedido.json"):
    pedido_id= input("Introduce el id del pedido:")
    cambios = 0
    for pedido in DATA_PEDIDOS:
        if pedido.get("pedido_id") == pedido_id:
            if pedido.get("estado", pedido.get("estado")) == "por procesar":
                pedido["estado"] = "en proceso"
                cambios = 1
            break
    if cambios:
        guardar_json(archivo, DATA_PEDIDOS)
        print(f" Pedido {pedido_id} actualizado a 'en proceso'.")
    else:
        print(f" Pedido {pedido_id} no existe o no estaba 'por procesar'.")