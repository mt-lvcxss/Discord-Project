import discord
from discord.ext import commands
from Utils.helpers import * # Importamos nuestras funciones

class DashboardView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @discord.ui.button(label="Entrar / Salir", style=discord.ButtonStyle.primary, emoji="🛠️")
    async def toggle_trabajo(self, button, interaction):
        # ... (Tu lógica de toggle aquí usando las funciones de helpers)
        await interaction.response.send_message("Estado actualizado", ephemeral=True)
        # Para llamar a la función de actualizar dentro del cog:
        cog = self.bot.get_cog("GestionTrabajo")
        await cog.actualizar_embed_activo()

class GestionTrabajo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def actualizar_embed_activo(self):
        # ... (Lógica de actualización del embed)
        pass

    @discord.slash_command(name="trabajo")
    async def trabajo(self, ctx):
        # ... (Lógica del comando)
        pass

def setup(bot):
    bot.add_cog(GestionTrabajo(bot))