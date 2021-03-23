import discord
import json, time
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\admin.json', mode='r', encoding='utf8') as AdminFile:
    AdminData = json.load(AdminFile)

def is_not_bot(m):
    return m.author.bot != client.user.bot

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
                await ctx.send('[Admin Command] 開始清除訊息')
                await ctx.send(f'將於{wait_sec}後開始清除')
                time.sleep(wait_sec)
                deleted =  await ctx.channel.purge(limit = count, check=is_not_bot)
                deleted = len(deleted)
                await ctx.send(f'[Admin Command] 已刪除{deleted}條訊息')

def setup(bot):
    bot.add_cog(admin(bot))