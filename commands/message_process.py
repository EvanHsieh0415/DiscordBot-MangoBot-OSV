from typing import ChainMap
import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

class message_process(Cog_Extension):
    @commands.command()
    async def mail(self, ctx, ChannelID, *, arg:str=None):
        try:
            channel = self.bot.get_channel(int(ChannelID))
            await channel.send(f'`{ctx.author}` 於伺服器 `{ctx.guild.name}` 說: \n> {arg}')
        except:
            await ctx.send(f'{arg} 無法發送')
        else:
            print(f'{ctx.author} (  ) 於伺服器 {ctx.guild.name} ( {ctx.guild.id} ) 說: \n> {arg}')

def setup(bot):
    bot.add_cog(message_process(bot))