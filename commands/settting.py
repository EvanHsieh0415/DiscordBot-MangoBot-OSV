import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open(r'.\data\exp.json', mode='r', encoding='utf8') as expFile:
            expData = json.load(expFile)

class setting(Cog_Extension):
    @commands.has_guild_permissions(administrator=True)
    @commands.group()
    async def set(self, ctx):
        pass

    @set.group()
    async def exp(self, ctx):
        pass

    @commands.is_owner()
    @exp.command()
    async def setup(self, ctx):
        expData = {str(ctx.guild.id): {'index': {} } }
        for i in ctx.guild.members:
            expData[str(ctx.guild.id)]['index'][str(i.id)] = {'name': i.name,'exps': 0, 'levels': 0}
        print(f'{ctx.guild.name} exp system setup complete')
        with open(r'.\data\exp.json', mode='w', encoding='utf8') as expFile:
            json.dump(expData, expFile, sort_keys=True, indent=4, ensure_ascii=False)

    @commands.is_owner()
    @exp.command()
    async def clear(self, ctx, confirm):
        if confirm == True:
            expData[str(ctx.guild.id)] = {'name': ctx.guild.name, 'index':{}}
            with open(r'.\data\exp.json', 'w', encoding='utf8') as ExpMemberFile:
                json.dump(expData, ExpMemberFile, sort_keys=True, indent=4)
            print(f'Clear {ctx.guild.name}\'s data')
        else:
            print(f'Cancel clear {ctx.guild.name}\'s data')
        with open(r'.\data\exp.json', mode='w', encoding='utf8') as expFile:
            json.dump(expData, expFile, sort_keys=True, indent=4, ensure_ascii=False)

def setup(bot):
    bot.add_cog(setting(bot))