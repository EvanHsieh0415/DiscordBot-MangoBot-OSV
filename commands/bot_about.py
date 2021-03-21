import discord
import json, datetime
from discord.ext import commands
from core.classes import Cog_Extension

class bot_about(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        ping=abs(int(self.bot.latency*1000))
        embed=discord.Embed(title=f'{ping}(ms)', color=0x73ff00, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name='延遲') 
        embed.set_footer(text=f'由{ctx.author}請求的鏈接')
        await ctx.send(embed=embed)
        print(f'{ctx.author} take bot\'s ping')


def setup(bot):
    bot.add_cog(bot_about(bot))
