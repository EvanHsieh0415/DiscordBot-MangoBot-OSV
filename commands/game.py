import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension

class game(Cog_Extension):
    @commands.group()
    async def g(self, ctx):
        if 'g ' not in ctx.message.content and 'g' in ctx.message.content:
            await ctx.send('請加上遊戲名稱')
    
    @g.command()
    async def dice(self, ctx, count:str=6):
        try:
            count = int(count)
        except:
            await ctx.send('數字輸入錯誤')
        else:
            num = random.randint(1, count)
            await ctx.send(f'骰出的數字為{num}')
    
    @g.command()
    async def cf(self, ctx):
        side_l = ['正', '反']
        side = random.choice(side_l)
        await ctx.send(f'硬幣為{side}面')

    @g.group()
    async def drop(self, ctx):
        if 'drop ' not in ctx.message.content and 'drop' in ctx.message.content:
            await ctx.send('請加上投擲物名稱')
    
    @drop.command()
    async def coin(self, ctx, member:str=None):
        await ctx.send('唉呦 好痛')
    
    @g.command()
    async def r(self, ctx, ques):
        pers = random.randint(0, 100)
        await ctx.send(f'{ques}的機率是 {pers}%')

def setup(bot):
    bot.add_cog(game(bot))