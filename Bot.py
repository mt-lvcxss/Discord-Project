import discord
import os
from dotenv import load_dotenv

load_dotenv()

class MyBot(discord.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())

    async def on_ready(self):
        # Registrar la View para que sea persistente tras reinicios
        from cogs.gestion import DashboardView
        self.add_view(DashboardView(self))
        print(f"✅ {self.user} en línea y Cogs cargados.")

bot = MyBot()

# Cargar automáticamente todos los archivos en la carpeta /cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv('TOKEN'))