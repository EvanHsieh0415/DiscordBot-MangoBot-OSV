import discord
import json, time, os
from discord.ext import commands
from core.classes import Cog_Extension

with open(r'.\settings\admin.json', mode='r', encoding='utf8') as AdminFile:
    AdminData = json.load(AdminFile)

#def deco(func): #出自Discord: 星曌#4316
#   return commands.has_guild_permissions(administrator=True)(commands.command()(func))

def repect_clean(t, wait_sec, deleted=None):
    if t == 0:
        msg = f'[Admin Command] 開始清除訊息\n[Admin Command] 將於{wait_sec}秒後開始清除'
    elif t == 1:
        msg = f'\n[Admin Command] 已刪除{len(deleted)-3}條訊息'
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
                await ctx.send(repect_clean(0, wait_sec))
                time.sleep(wait_sec)
                deleted =  await ctx.channel.purge(limit = count+3)
                await ctx.send(repect_clean(1, wait_sec, deleted))
    
    @commands.has_guild_permissions(administrator=True)
    @commands.group()
    async def json(self, ctx):
        pass
    
    @json.command()
    async def re_dump(self, ctx):
        await ctx.send('> json.dump Start')
        for Filename in os.listdir('.\\settings'):
            if Filename.endswith('.json'):
                with open(f'.\\settings\\{Filename}', mode='r', encoding='utf8') as File:
                    Data = json.load(File)
                with open(f'.\\settings\\{Filename}', mode='w', encoding='utf8') as File:
                    json.dump(Data, File, sort_keys=True, indent=4, ensure_ascii=False)
                await ctx.send(f'json.dump `{Filename}`')
                print(f'json.dump {Filename}')
        await ctx.send('> json.dump all complete')

def setup(bot):
    bot.add_cog(admin(bot))