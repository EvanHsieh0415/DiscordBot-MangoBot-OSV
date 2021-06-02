import discord
import json
import datetime
from discord.ext import commands
from core.classes import Cog_Extension

class invite(Cog_Extension):
    @commands.is_owner()
    @commands.command()
    async def vc_invite(self, ctx, vc_id:int, max_age:int=0, max_use:int=0, reason:str=''):
        channel = self.bot.get_channel(vc_id)
        invite_vc = channel.create_invite(max_age=max_age, max_use=max_use, reason=reason)
        print(invite_vc)
        await ctx.send(f'{invite_vc.url}')

def setup(bot):
    bot.add_cog(invite(bot))