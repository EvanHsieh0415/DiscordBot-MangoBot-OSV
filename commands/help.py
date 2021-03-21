import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

def help_menu(cmds, lang):
    if lang == 'en_us':
        if cmds == 'all':
            pass
        elif cmds == 'mail':
            text = '> `mail` - mb> mail [Channel ID] [Message]\n> send [Message] to [Channel ID]'
        elif cmds == 'pipe_mail':
            text = '> `pipe_mail` - mb> mail [Pipe Number] [Message]\n > Send [Message] through Pipe [Pipe Number]'
    elif lang == 'zh_tw':
        if cmds == 'all':
            pass
        elif cmds == 'mail':
            text = '> `mail` - mb> mail [Channel ID] [Message]\n> 傳送 [Message] 到 [Channel ID]'
        elif cmds == 'pipe_mail':
            text = '> `pipe_mail` - mb> mail [Pipe Number] [Message]\n > 透過管道[Pipe Number] 傳送訊息 [Message]'
    return text

class help(Cog_Extension):
    @commands.command()
    async def help(self, ctx, cmd, lang):
        await ctx.send(help_menu(cmds=cmd, lang=lang))

def setup(bot):
    bot.add_cog(help(bot))
