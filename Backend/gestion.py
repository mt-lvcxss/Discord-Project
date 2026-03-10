import discord
from discord.ext import commands
from Utils.helpers import *

class DashboardView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        # timeout=None es obligatorio para persistencia
        super().__init__(timeout=None) 

    @discord.ui.button(
        label="Entrar / Salir", 
        style=discord.ButtonStyle.primary, 
        emoji="🛠️", 
        custom_id="btn_trabajo_toggle" # ID ÚNICO Y FIJO
    )
    async def toggle_trabajo(self, button, interaction):
        user = interaction.user
        datos = cargar_datos()
        user_id = str(user.id)
        
        if user_id in datos:
            del datos[user_id]
            res = "Has terminado tu jornada."
            try: await user.edit(nick=user.display_name.replace("[🔨] ", ""))
            except: pass
        else:
            datos[user_id] = {"estado": "Trabajando", "descripcion": "Sin asignación", "inicio": time.time()}
            res = "Has entrado a trabajar."
            try: await user.edit(nick=f"[🔨] {user.display_name}"[:32])
            except: pass
            
        guardar_todos_los_datos(datos)
        await interaction.response.send_message(f"✅ {res}", ephemeral=True)
        await self.actualizar_dashboard_directo()

    @discord.ui.button(
        label="Actualizar Lista", 
        style=discord.ButtonStyle.secondary, 
        emoji="🔄", 
        custom_id="btn_trabajo_refresh" # ID ÚNICO Y FIJO
    )
    async def refresh_lista(self, button, interaction):
        await self.actualizar_dashboard_directo()
        await interaction.response.send_message("Panel actualizado.", ephemeral=True)

    async def actualizar_dashboard_directo(self):
        info = obtener_dashboard()
        if not info: return
        datos = cargar_datos()
        try:
            channel = self.bot.get_channel(info["channel_id"]) or await self.bot.fetch_channel(info["channel_id"])
            message = await channel.fetch_message(info["message_id"])
            
            embed = discord.Embed(title="📊 Panel de Gestión en Vivo", color=discord.Color.green())
            if not datos:
                embed.description = "Nadie está trabajando actualmente. ☕"
            else:
                for uid, info_u in datos.items():
                    tarea = info_u.get("descripcion", "Sin asignación")
                    tiempo = formato_tiempo(info_u.get("inicio", time.time()))
                    embed.add_field(name=f"👤 Trabajador", value=f"**Usuario:** <@{uid}>\n⏱️ **Tiempo:** {tiempo}\n📝 **Tarea:** {tarea}", inline=False)
            
            await message.edit(embed=embed, view=self)
        except: pass

class GestionTrabajo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="estados", description="Activa el panel interactivo")
    async def estados(self, ctx):
        await ctx.respond("Generando panel...", ephemeral=True)
        mensaje = await ctx.channel.send(content="Cargando...", view=DashboardView(self.bot))
        guardar_dashboard(ctx.channel_id, mensaje.id)
        # Llamar a la actualización
        cog = self.bot.get_cog("GestionTrabajo")
        view = DashboardView(self.bot)
        await view.actualizar_dashboard_directo()

    @discord.slash_command(name="asignacion", description="Cambia tu tarea actual")
    async def asignacion(self, ctx, descripcion: str):
        datos = cargar_datos()
        user_id = str(ctx.author.id)
        if user_id not in datos:
            return await ctx.respond("Primero debes entrar a trabajar.", ephemeral=True)
        
        datos[user_id]["descripcion"] = descripcion
        guardar_todos_los_datos(datos)
        await ctx.respond(f"Tarea actualizada: {descripcion}", ephemeral=True)
        view = DashboardView(self.bot)
        await view.actualizar_dashboard_directo()

def setup(bot):
    bot.add_cog(GestionTrabajo(bot))