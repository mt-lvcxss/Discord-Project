# Discord Bot — Pycord setup

Instrucciones para usar este proyecto con **py-cord**.

- Instalar dependencias:

```powershell
python -m pip install -U pip
python -m pip install -r requirements.txt
```

- Crear un archivo `.env` en la raíz con la línea:

```
TOKEN=TU_TOKEN_AQUI
```

- Si tu bot necesita leer contenido de mensajes o miembros, habilita los "Privileged Gateway Intents" en el Developer Portal:
  1. https://discord.com/developers/applications
  2. Selecciona tu aplicación → **Bot** → en "Privileged Gateway Intents" activa **Message Content Intent** y/o **Server Members Intent** según necesites.
  3. Guarda los cambios y reinicia el bot.

- Ejecutar el bot:

```powershell
python Bot.py
```

Archivos clave:
- [Bot.py](Bot.py) — código del bot.
- [requirements.txt](requirements.txt) — dependencias para py-cord.
