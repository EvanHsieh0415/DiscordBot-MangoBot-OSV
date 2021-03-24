import discord
import json, os
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\event.json', mode='r', encoding='utf8') as EventFile:
    EventData = json.load(EventFile)

with open('.\\settings\\load.json', mode='r', encoding='utf8') as LoadFile:
    LoadData = json.load(LoadFile)

def channel_function(self, ctx):
    global channel
    channel = self.bot.get_channel(int(EventData[str(ctx.guild.id)]['feedback']['load']['channel']))
    return channel

def load_function(feedback_type, ctx, self, extension):
    if EventData[str(ctx.guild.id)]['feedback']['enable'] == True:
        if extension == 'load':
            feedback_str = f'{extension} 執行動作失敗, 該程式區塊為重要區塊 無法進行動作'
        elif feedback_type == 'load':
            zh_index = '載入'
            self.bot.load_extension(f'commands.{extension}')
        elif feedback_type == 'unload':
            zh_index = '卸載'
            self.bot.unload_extension(f'commands.{extension}')
        elif feedback_type == 'reload':
            zh_index = '重新載入'
            self.bot.reload_extension(f'commands.{extension}')
        print(f'【Bot】{zh_index} {extension}')
        feedback_str = f'【Bot】{zh_index} {extension} 完成'
        return feedback_str

def load_all_function(feedback_type, ctx, self):
    if EventData[str(ctx.guild.id)]['feedback']['enable'] == True:
        not_load = LoadData['not_load']
        if feedback_type == 'load':
            zh_index = '載入'
            for Filename in os.listdir('.\\commands'):
                if Filename.endswith('.py') and Filename not in not_load:
                    self.bot.load_extension(f'commands.{Filename[:-3]}')
        elif feedback_type == 'unload':
            zh_index = '卸載'
            for Filename in os.listdir('.\\commands'):
                if Filename.endswith('.py') and Filename not in not_load:
                    self.bot.unload_extension(f'commands.{Filename[:-3]}')
        elif feedback_type == 'reload':
            zh_index = '重新載入'
            for Filename in os.listdir('.\\commands'):
                if Filename.endswith('.py') and Filename not in not_load:
                    self.bot.reload_extension(f'commands.{Filename[:-3]}')
        print(f'【Bot】全部{zh_index} 完成')
        zh_index = (f'【Bot】全部{zh_index} 完成')
        return zh_index

class load(Cog_Extension):
    @commands.command()
    async def l(self, ctx, extension):
        channel = channel_function(self=self, ctx=ctx)
        await channel.send(load_function(feedback_type='load', ctx=ctx, self=self, extension=extension))

    @commands.command()
    async def u(self, ctx, extension):
        channel = channel_function(self=self, ctx=ctx)
        await channel.send(load_function(feedback_type='unload', ctx=ctx, self=self, extension=extension))

    @commands.command()
    async def r(self, ctx, extension):
        channel = channel_function(self=self, ctx=ctx)
        await channel.send(load_function(feedback_type='reload', ctx=ctx, self=self, extension=extension))

    @commands.command()
    async def la(self, ctx):
        channel = channel_function(self=self, ctx=ctx)
        await channel.send(load_all_function(feedback_type='load', ctx=ctx, self=self))

    @commands.command()
    async def ua(self, ctx):
        channel = channel_function(self=self, ctx=ctx)
        await channel.send(load_all_function(feedback_type='unload', ctx=ctx, self=self))

    @commands.command()
    async def ra(self, ctx):
        channel = channel_function(self=self, ctx=ctx)
        await channel.send(load_all_function(feedback_type='reload', ctx=ctx, self=self))

def setup(bot):
    bot.add_cog(load(bot))
