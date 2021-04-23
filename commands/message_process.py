import discord
import json, base64
from discord.ext import commands
from core.classes import Cog_Extension

with open(r'.\settings\message_process.json', mode='r', encoding='utf8') as MessageFile:
    MessageData = json.load(MessageFile)

class message_process(Cog_Extension):
    @commands.command()
    async def mail(self, ctx, ChannelID, *, msg:str=None):
        try:
            channel = self.bot.get_channel(int(ChannelID))
            await channel.send(f'`{ctx.author}` 於伺服器 `{ctx.guild.name}` 說: \n> {msg}')
        except:
            await ctx.send(f'{msg} 無法發送')
        else:
            print(f'>>>{ctx.author} 於伺服器 {ctx.guild.name} ( {ctx.guild.id} ) 說: \n> {msg}')

    @commands.command()
    async def pipe_mail(self, ctx, pipe, *, msg):
        if pipe in MessageData['mail']['connect']['pipe']:
            if ctx.channel.id == MessageData['mail']['connect']['pipe'][pipe]['from']['id']:
                try:
                    ToChannel = self.bot.get_channel(MessageData['mail']['connect']['pipe'][pipe]['to']['id'])
                    await ToChannel.send(f'`{ctx.author}` 於通訊頻道 `{pipe}` 說: \n> {msg}')
                except:
                    await ctx.send(f'{msg} 無法發送')
                else:
                    await ctx.send(f'已成功於頻道`{pipe}`發送訊息 \n> {msg}')
                    print(f'>>> {ctx.author} 於通訊頻道 `{pipe}` 說: \n> {msg}')
            else:
                await ctx.send(f'{msg} 無法發送, 請確認輸入端位置是否正確')
        else:
            await ctx.send(f'{msg} 無法發送, 請確認通訊頻道是否正確')

    @commands.command()
    async def Mencode(self, ctx, encryptType:str=False, *, password:str=False):
        output = ''
        encryptTypeList = ['ASCII']
        if encryptType in MessageData['encrypt']['list']:
            if password:
                if encryptType == 'ASCII':
                    l = []
                    for i in password:
                        l.append(str(ord(i)))
                    output = '-'.join(l)
                elif encryptType == 'base64':
                    output = str(base64.b64encode(password.encode()), 'utf8')
                await ctx.author.send(f'> **Mango Bot加密系統**\n原文：`{password}`\n加密方式：`{encryptType}`\n密文`{output}`')
                print(f'{ctx.author} 使用了 Mango Bot加密系統\n原文：`{password}`\n加密方式：`{encryptType}`\n密文`{output}`')
            else:
                await ctx.author.send(f'> **Mango Bot加密系統**\n請輸入加密內容')
        else:
            if encryptTypeList:
                await ctx.author.send(f'> **Mango Bot加密系統**\n加密方式 {encryptType} 尚未收編進加密辭典中 請與機器人技術人員聯繫')
            else:
                await ctx.author.send(f'> **Mango Bot加密系統**\n請輸入加密方式')
        

def setup(bot):
    bot.add_cog(message_process(bot))