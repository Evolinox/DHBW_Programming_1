import discord
import requests
import json
import asyncio
import textwrap

from discord.ext import commands
from discord import app_commands
import xml.etree.ElementTree as ET

# Lies die API Daten aus der Textdatei
with open('token.txt') as file:
    textfile = file.readlines()
    dbApiId = ""
    dbApiSecret = ""

class Infrago(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DEBUG: Infrago cog loaded")

    # Slashbefehl um die Frage einzugeben und an Ollama lokal zu senden
    @app_commands.command(name = "timetable", description = "Get arrivals and departures from a Station")
    @app_commands.describe(eva = "Station Number")
    @app_commands.choices(eva = [
        discord.app_commands.Choice(name="Mosbach (Baden)", value="8004094"),
        discord.app_commands.Choice(name="Mosbach-Neckarelz", value="8000264"),
        discord.app_commands.Choice(name="Bad Friedrichshall", value="8000017"),
        discord.app_commands.Choice(name="Heilbronn Hauptbahnhof", value="8000157"),
        discord.app_commands.Choice(name="Osterburken", value="8000295"),
        discord.app_commands.Choice(name="Eberbach", value="8000369")
    ])
    async def infra(self, interaction: discord.Interaction, eva: discord.app_commands.Choice[str], date: str, time: str):
        date2friendly = f"{date[4]+date[5]}.{date[2]+date[3]}.{date[0]+date[1]}"
        
        infraGoUrl = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{eva.value}/{date}/{time}"

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

        for service in timetable:
            # Check if train terminates here
            for train in service:
                if not train.tag.find("dp") and train.tag.find("ar"):
                    print("hier")

                    departureTime = service[1].attrib.get("pt")
                    dT2friendly = f"{departureTime[6]+departureTime[7]}:{departureTime[8]+departureTime[9]} Uhr"
                    trainInfo = f"{service[0].attrib.get("c")} {service[1].attrib.get("l")} - Abfahrt: {dT2friendly} auf Gleis {service[1].attrib.get("pp")}"
                    trainPath = service[1].attrib.get("ppth").split("|")
                    nextStation = f"{trainPath[0]}"
                    endStation = f"{trainPath[len(trainPath)-1]}"

                    promptEmbed.add_field(name=trainInfo, value=f"Nächster Halt: {nextStation}\nEndstation: {endStation}", inline=False)

        await interaction.followup.send(embed=promptEmbed)

async def setup(bot):
    await bot.add_cog(Infrago(bot))