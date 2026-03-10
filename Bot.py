import discord
import os
from dotenv import load_dotenv

load_dotenv()

class MyBot(discord.Bot):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        # IMPORTANTE: Importar aquí para evitar importaciones circulares
        from Backend.gestion import DashboardView
        self.add_view(DashboardView(self))
        print(f"✅ {self.user} online. View persistente registrada.")

bot = MyBot()

# Cargar Backend
if __name__ == "__main__":
    for filename in os.listdir('./Backend'):
        if filename.endswith('.py'):
            bot.load_extension(f'Backend.{filename[:-3]}')

bot.run(os.getenv('TOKEN'))