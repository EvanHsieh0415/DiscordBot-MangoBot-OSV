import discord
import json, time
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\admin.json', mode='r', encoding='utf8') as AdminFile:
    AdminData = json.load(AdminFile)

#def deco(func): #出自Discord: 星曌#4316
#   return commands.has_guild_permissions(administrator=True)(commands.command()(func))

def repect_clean(wait_sec):
    msg = f'[Admin Command] 開始清除訊息\n[Admin Command] 將於{wait_sec}後開始清除'
    return msg

class admin(Cog_Extension):
    @commands.has_guild_permissions(administrator=True)
    @commands.command()
    async def clean(self, ctx, count:int):
        max_clean = AdminData['clean']['max_clean']
        wait_sec = AdminData['clean']['wait_sec']
        if count <= 0:
            await ctx.send('[Error] 清除數量不得小於等於0')
        else:
            if count > max_clean:
                await ctx.send('[Error] 清除數量不得大於設定之最大值')
            else:
                await ctx.send(repect_clean(wait_sec=wait_sec))
                time.sleep(wait_sec)
                deleted =  await ctx.channel.purge(limit = count+3)
                await ctx.send(repect_clean(wait_sec=wait_sec))
                await ctx.send(f'[Admin Command] 已刪除{len(deleted)-3}條訊息')

def setup(bot):
    bot.add_cog(admin(bot))