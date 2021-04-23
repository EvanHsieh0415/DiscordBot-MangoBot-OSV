import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open(r'.\data\exp.json', 'r', encoding='utf8') as ExpMemberFile:
    ExpMemberData = json.load(ExpMemberFile)

def exp_function(ctx):
    pass

class experience(Cog_Extension):
    @commands.group()
    async def exp(self, ctx):
        Exps = ExpMemberData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['exps'] 
        await ctx.send(f'{ctx.author.mention}\'s Exp is {Exps}')

    @exp.command()
    async def level(self, ctx):
        Levels = ExpMemberData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['levels'] 
        await ctx.send(f'{ctx.author.mention}\'s Rank is {Levels}')

    @exp.command()
    async def rank(self, ctx):
        pass

def setup(bot):
    bot.add_cog(experience(bot))