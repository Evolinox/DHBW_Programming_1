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

def date2Friendly(timecode):
    ...
    return timecode

def path2Friendly(trainpath):
    ...
    return trainpath

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
        
        infraGoUrl = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{eva.value}/{date}/{time}"

        headers = {
            "DB-Client-Id": dbApiId,
            "DB-Api-Key": dbApiSecret,
            "accept": "application/xml"
        }
        
        await interaction.response.defer()
        await asyncio.sleep(1)

        response = requests.get(infraGoUrl, headers=headers)
        data = ET.fromstring(response.text)

        timetable = []

        timetable.append(data.get("station"))

        # Wait a second, who are you?!
        await asyncio.sleep(1)

        for s in data:
            for t in s:
                train = [
                    [
                        [s[0].attrib.get("c"), s[1].attrib.get("l")],
                        s[1].attrib.get("pp"),
                        date2Friendly(s[1].attrib.get("pt"))
                ],
            path2Friendly(s[1].attrib.get("ppth")),
            path2Friendly(s[2].attrib.get("ppth"))
        ]
        timetable.append(train)

async def setup(bot):
    await bot.add_cog(Infrago(bot))