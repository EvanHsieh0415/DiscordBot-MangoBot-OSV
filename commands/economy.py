import discord
import json, random
from discord.ext import commands
from core.classes import Cog_Extension

with open(r'.\data\economy.json', mode='r', encoding='utf8') as EcMemberFile:
    EcMemberData = json.load(EcMemberFile)
with open(r'.\settings\economy.json', mode='r', encoding='utf8') as EcSettingFile:
    EcSettingData = json.load(EcSettingFile)

class economy(Cog_Extension):
    @commands.group()
    async def ec(self, ctx):
        pass

    @commands.is_owner()
    @ec.command()
    async def setup(self, ctx):
        EcMemberData[str(ctx.guild.id)] = {'name': ctx.guild.name, 'index':{}}
        for i in ctx.guild.members:
            if i.bot == False:
                EcMemberData[str(ctx.guild.id)]['index'][str(i.id)] = {'name': i.name, 'money': 0}
                print(f'Add {i.name} into \'\\data\\economy.json\'')
        with open(r'.\data\economy.json', mode='w', encoding='utf8') as EcMemberFile:
            json.dump(EcMemberData, EcMemberFile, sort_keys=True, indent=4, ensure_ascii=False)
    
    @ec.command()
    async def work(self, ctx):
        Pay = random.choice(EcSettingData['work']['pay'])
        EcMemberData[str(ctx.guild.id)] ['index'][str(ctx.author.id)]['money'] += Pay
        await ctx.send(f'{ctx.author.name} 努力工作, 賺了{Pay}元')
        print(f'{ctx.author.name} - {ctx.author.id} work and get $ {Pay}')
        with open(r'.\data\economy.json', mode='w', encoding='utf8') as EcMemberFile:
            json.dump(EcMemberData, EcMemberFile, sort_keys=True, indent=4, ensure_ascii=False)

    @ec.command()
    async def my_wallet(self, ctx):
        money = EcMemberData[str(ctx.guild.id)] ['index'][str(ctx.author.id)]['money']
        await ctx.send(f'你的錢包目前有 {money} 元')

def setup(bot):
    bot.add_cog(economy(bot))