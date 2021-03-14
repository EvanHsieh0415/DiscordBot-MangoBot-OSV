import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\keyword.json', 'r', encoding='utf8') as KeywordFile:
    KeywordData = json.load(KeywordFile)

class key_word(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.lower() in KeywordData['press f']['keyword']:
            Picture = discord.File(KeywordData['press f']['image'])
            await msg.channel.send(file=Picture)

def setup(bot):
    bot.add_cog(key_word(bot))