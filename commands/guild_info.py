import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\guild_info.json', mode='r', encoding='utf8') as GuildinfoFile:
    GuildinfoData = json.load(GuildinfoFile)
        
class guild_info(Cog_Extension):
    @commands.command
    async def guild(self, ctx, arg):
        pass
        
    @commands.command()
    async def role(self, ctx, role_name:str=None):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        role_count = len(role.members)
        embed=discord.Embed(description=f'{role.mention}')
        embed.add_field(name='Members', value=f'{role_count}', inline=True)
        embed.add_field(name='Position', value=f'{role.position}', inline=True)
        embed.add_field(name='Color', value=f'{role.color}', inline=True)
        embed.add_field(name='ID', value=f'{role.id}', inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def member(self, ctx, member_name:str=None):
        member = discord.utils.get(ctx.guild.members, name=member_name)
        

def setup(bot):
    bot.add_cog(guild_info(bot))