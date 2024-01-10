import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

createChannelID = 1114248615553155112
categoryID = 987701014159319100
devServerID = 635480321541931029

class Voicechannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        client = discord.Client(intents=intents)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, after, before):
        
        # Get current Guild
        guild = member.guild

        if guild.id != devServerID:
            print(f"Irgendwas stimmt net.")
        else:
            channel_exists = True
            channel_id = createChannelID
            channel_category = categoryID

            if channel_id and channel_exists == True:
                channel = discord.utils.get(guild.voice_channels, id = int(channel_id))

                for user in channel.members:
                    if user == member:
                        user_name = member.display_name
                        for channelTemp in guild.voice_channels:
                            if channelTemp.name == (user_name + "'s Channel"):
                                await channelTemp.delete()

                        category = discord.utils.get(guild.categories, id=int(channel_category))
                        await guild.create_voice_channel(user_name + "'s Channel", category = category)
                        for channelTemp2 in guild.voice_channels:
                            if channelTemp2.name == (user_name + "'s Channel"):
                                await member.edit(voice_channel = channelTemp2)

async def setup(bot):
    await bot.add_cog(Voicechannel(bot))