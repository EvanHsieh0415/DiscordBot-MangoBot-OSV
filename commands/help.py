import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

class help(Cog_Extension):
    @commands.command()
    async def help_(self, ctx, page:int):
        maxpage = 2
        if page == 1:
            help_type = 'Game'
        embed=discord.Embed(title=f'page: {page}', description=help_type)
        embed.set_author(name='Help')
        embed.set_footer(text=f'Page {page}/{maxpage}')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
