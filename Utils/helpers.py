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

def guardar_dashboard(channel_id, message_id):
    with open(DASHBOARD_FILE, "w") as f:
        json.dump({"channel_id": channel_id, "message_id": message_id}, f)

def obtener_dashboard():
    if os.path.exists(DASHBOARD_FILE):
        with open(DASHBOARD_FILE, "r") as f:
            return json.load(f)
    return None

def formato_tiempo(segundos_inicio):
    segundos = int(time.time() - segundos_inicio)
    horas, rem = divmod(segundos, 3600)
    minutos, _ = divmod(rem, 60)
    return f"{horas}h {minutos}m"