import discord
import json
from discord.ext import commands
from discord.ext.commands.core import command
from discord.ext.commands.errors import CommandNotFound
from core.classes import Cog_Extension

def help_menu(cmds, lang):
    if lang == 'en_us':
        if cmds == 'all':
            pass
        elif cmds == 'mail':
            text = '> `mail` - mb> mail [Channel ID] [Message]\n> send [Message] to [Channel ID]'
        elif cmds == 'pipe_mail':
            text = '> `pipe_mail` - mb> mail [Pipe Number] [Message]\n > Send [Message] through Pipe [Pipe Number]'
        return text

class help(Cog_Extension):
    @commands.command()
    async def cmd_help(self, ctx, cmd, lang):
        await ctx.send(help_menu(cmds=cmd, lang=lang))

def setup(bot):
    bot.add_cog(help(bot))