import json
import os
import time

FILENAME = "estados.json"
DASHBOARD_FILE = "dashboard_info.json"

def cargar_datos():
    if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        return {}
    with open(FILENAME, "r") as f:
        return json.load(f)

def guardar_todos_los_datos(datos):
    with open(FILENAME, "w") as f:
        json.dump(datos, f, indent=4)

def formato_tiempo(segundos_inicio):
    segundos = int(time.time() - segundos_inicio)
    horas, rem = divmod(segundos, 3600)
    minutos, _ = divmod(rem, 60)
    return f"{horas}h {minutos}m"

# Añade aquí obtener_dashboard y guardar_dashboard...