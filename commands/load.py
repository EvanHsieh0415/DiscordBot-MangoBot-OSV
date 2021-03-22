import discord
import json, os
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\event.json', 'r', encoding='utf8') as EventFile:
    EventData = json.load(EventFile)

not_load = ['test.py']

def feedback(feedback_type, ctx, self, extension):
    if EventData[str(ctx.guild.id)]['feedback']['enable'] == True:
        channel = self.bot.get_channel(int(EventData[str(ctx.guild.id)]['feedback']['load']['channel']))
        if feedback_type == 'error':
            feedback_str = f'{extension} 執行動作失敗, 該程式區塊為重要區塊 無法進行動作'
        else:
            if feedback_type == 'load':
                zh_index = '載入'
            elif feedback_type == 'unload':
                zh_index = '卸載'
            elif feedback_type == 'reload':
                zh_index = '重新載入'
            feedback_str = f'{zh_index} {extension} 完成'
        return feedback_str

class load(Cog_Extension):
    @commands.command()
    async def load(self, ctx, extension):
        print(f'load {extension}')
        if extension == 'load':
            await ctx.channel.send(feedback('error', ctx, self, extension))
        else:
            self.bot.load_extension(f'commands.{extension}')
            await ctx.channel.send(feedback('load', ctx, self, extension))

    @commands.command()
    async def unload(self, ctx, extension):
        print(f'unload {extension}')
        if extension == 'load':
            await ctx.channel.send(feedback('error', ctx, self, extension))
        else:
            self.bot.unload_extension(f'commands.{extension}')
            await ctx.channel.send(feedback('unload', ctx, self, extension))

    @commands.command()
    async def reload(self, ctx, extension):
        print(f'reload {extension}')
        if extension == 'load':
            await ctx.channel.send(feedback('error', ctx, self, extension))
        else:
            self.bot.reload_extension(f'commands.{extension}')
            await ctx.channel.send(feedback('reload', ctx, self, extension))
    
    @commands.command()
    async def ra(self, ctx):
        print('reload all')
        for Filename in os.listdir('.\\commands'):
            if Filename.endswith('.py') and Filename not in not_load:
                self.bot.reload_extension(f'commands.{Filename[:-3]}')

def setup(bot):
    bot.add_cog(load(bot))
