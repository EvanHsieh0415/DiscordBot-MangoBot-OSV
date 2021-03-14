import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

def show(ctx, guild_member_status:str):
    member_list = []
    for member in ctx.guild.members:
        if str(member.status) == guild_member_status:
            member_list.append(f'{member.name}#{member.discriminator}')
    text = f'`{guild_member_status} Count: {len(member_list)}`\n'
    for i in member_list:
        text += f'> {i}\n'
    return text

class member_info(Cog_Extension):

    @commands.command()
    async def member(self, ctx, arg1, arg2:str):
        if arg1 == 'status':
            await ctx.send(show(ctx, arg2))

def setup(bot):
    bot.add_cog(member_info(bot))