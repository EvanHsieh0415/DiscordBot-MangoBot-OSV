import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\channel.json', 'r', encoding='utf8') as ChannelFile:
    ChannelData = json.load(ChannelFile)

def feedback(feedback_type, ctx, extension):
    if ChannelData['feedback']['enable'] == True:
        channel = self.bot.get_channel(int(ChannelData['feedback']['channel']))
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
        print(f"load {extension}")
        self.bot.load_extension(f'commands.{extension}')
        await ctx.channel.send(feedback('load', ctx, extension))

    @commands.command()
    async def unload(self, ctx, extension):
        print(f"unload {extension}")
        self.bot.unload_extension(f'commands.{extension}')
        await ctx.channel.send(feedback('unload', ctx, extension))

    @commands.command()
    async def reload(self, ctx, extension):
        print(f"reload {extension}")
        self.bot.reload_extension(f'commands.{extension}')
        await ctx.channel.send(feedback('reload', ctx, extension))

def setup(bot):
    bot.add_cog(load(bot))