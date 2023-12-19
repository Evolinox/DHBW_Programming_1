import discord
import mathlib.vollstInduktion
import mathlib.heron

from discord.ext import commands
from discord import app_commands

class Mathematics(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DEBUG: Mathematics cog loaded")

    # Slashbefehl um die eine vollständige Induktion durchzuführen
    @app_commands.command(name = "induktion", description = "Beweise, ob die vollständige Induktion funktioniert")
    async def vollstInduktioninduktion(self, interaction: discord.Interaction, func: str):
        await interaction.response.defer()
        res = mathlib.vollstInduktion.induktion(func)
        if res == 0 :
            await interaction.followup.send("die vollständige Induktion " + func + " funktioniert")
        else:
            await interaction.followup.send("die vollständige Induktion " + func + " funktioniert nicht")

    # Slashbefehl um die Wurzel einer Zahl zu finden
    @app_commands.command(name = "sqrt", description = "Gibt die Wurzel einer beliebigen Zahl wieder")
    async def sqrt(self, interaction: discord.Interaction, number: int):
        res = mathlib.heron.heronsMethod(number)
        await interaction.response.send_message(f"Die Wurzel aus {number} ist: {res}")

async def setup(bot):
    await bot.add_cog(Mathematics(bot), guilds = [discord.Object(id=1179106176915480686), discord.Object(id=635480321541931029)])