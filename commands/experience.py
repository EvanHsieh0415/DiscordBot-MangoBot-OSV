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
        Exps = ExpMemberData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['exp']
        await ctx.send(f'{ctx.author.mention}\'s Exp is {Exps}')

    @exp.command()
    async def level(self, ctx):
        Levels = ExpMemberData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['level']
        await ctx.send(f'{ctx.author.mention}\'s Rank is {Levels}')

    @exp.command()
    async def rank(self, ctx):
        pass

    @commands.is_owner()
    @exp.command()
    async def setup(self, ctx):
        ExpMemberData = {'fileName': 'exp.json', 'index': {'guild': {str(ctx.guild.id): {'guildName': ctx.guild.name, 'exp':{}}}}}
        for i in ctx.guild.members:
            ExpMemberData['index']['guild'][str(ctx.guild.id)]['exp'][str(i.id)] = {'memberName': i.name, 'exps': 0, 'levels': 0}
        with open(r'.\data\exp.json', 'w', encoding='utf8') as ExpMemberFile:
            json.dump(ExpMemberData, ExpMemberFile, sort_keys=True, indent=4)
        print(f'{ctx.guild.name} setup complete')
        await ctx.send(f'{ctx.guild.name} 初始化完成')
    
    @commands.is_owner()
    @exp.command()
    async def clear(self, ctx, confirm):
        if confirm == True:
            ExpMemberData[str(ctx.guild.id)] = {'name': ctx.guild.name, 'index':{}}
            with open(r'.\data\exp.json', 'w', encoding='utf8') as ExpMemberFile:
                json.dump(ExpMemberData, ExpMemberFile, sort_keys=True, indent=4)
            print(f'Clear {ctx.guild.name}\'s data')
        else:
            print(f'Cancel clear {ctx.guild.name}\'s data')

def setup(bot):
    bot.add_cog(experience(bot))