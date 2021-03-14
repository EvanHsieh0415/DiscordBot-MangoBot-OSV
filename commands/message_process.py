import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\message_process.json', mode='r', encoding='utf8') as MessageFile:
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

def setup(bot):
    bot.add_cog(message_process(bot))