import discord
import requests
import json
import asyncio
import textwrap

from discord.ext import commands
from discord import app_commands

class Infrago(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DEBUG: Infrago cog loaded")

    # Slashbefehl um die Frage einzugeben und an Ollama lokal zu senden
    @app_commands.command(name = "timetable", description = "Get arrivals and departures from a Station")
    async def infra(self, interaction: discord.Interaction, eva: str, date: str, time: str):
        
        infraGoUrl = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{eva}/{date}/{time}"

        headers = {
            "DB-Client-Id": dbApiId,
            "DB-Api-Key": dbApiSecret,
            "accept": "application/xml"
        }
        
        await interaction.response.defer()
        await asyncio.sleep(1)

        response = requests.get(infraGoUrl, headers=headers)
        timetable = ET.fromstring(response.text)

        # Wait a second, who are you?!
        await asyncio.sleep(1)

        # Embed
        promptEmbed = discord.Embed(title=timetable.get("station"), description=f"EVA Nummer: {eva.value}", color=0xe91e63)
        promptEmbed.add_field(name="Datum", value=date2friendly, inline=True)
        promptEmbed.add_field(name="Stunde", value=f"{time} Uhr", inline=True)

        await interaction.followup.send(embed=promptEmbed)

async def setup(bot):
    await bot.add_cog(Infrago(bot))