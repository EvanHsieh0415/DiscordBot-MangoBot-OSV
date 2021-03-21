import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\guild_info.json', mode='r', encoding='utf8') as GuildinfoFile:
    GuildinfoData = json.load(GuildinfoFile)

def member_status(member_status:str, guild):
    member_list = []
    for member in guild.members:
        if str(member.status) == member_status:
            member_list.append(member.name)
    return member_list

def role_len(role_name:str, guild):
    role_list = []
    for member in guild.members:
        if role_name in member.roles.name:
            role_list.append(member.name)
    return role_list

class info(Cog_Extension):
    @commands.command()
    async def role(self, ctx, role_name:str=None):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name=role_name)
        if role_name == None:
            role_count = len(guild.roles)
            
            embed=discord.Embed(description='Roles')
            embed.add_field(name='Count', value=role_count, inline=False)
            guild_roles = guild.roles
            for i in range(len(guild_roles)):
                roles = guild_roles[i]
                if roles.name != '@everyone':
                    embed.add_field(name=f'{guild_roles[i]}', value=len(roles.members), inline=True)
        else:
            role_member_count = len(role.members)
            embed=discord.Embed(description=f'{role.mention}')
            embed.add_field(name='Members', value=f'{role_member_count}', inline=True)
            embed.add_field(name='Position', value=f'{role.position}', inline=True)
            embed.add_field(name='Color', value=f'{role.color}', inline=True)
            embed.add_field(name='ID', value=f'{role.id}', inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def member(self, ctx, *, member_name:str=None):
        guild = ctx.guild
        member = discord.utils.get(guild.members, name=member_name)
        if member_name == None:
            member_count = len(guild.members)
            member_online = len(member_status(member_status='online', guild=guild))
            member_idle = len(member_status(member_status='idle', guild=guild))
            member_dnd = len(member_status(member_status='dnd', guild=guild))
            member_offline = len(member_status(member_status='offline', guild=guild))

            embed=discord.Embed(description='Members')
            embed.add_field(name='Count', value=f'{member_count}', inline=False)
            embed.add_field(name='Online', value=f'{member_online}', inline=True)
            embed.add_field(name='Idle', value=f'{member_idle}', inline=True)
            embed.add_field(name='Do Not Disturb', value=f'{member_dnd}', inline=True)
            embed.add_field(name='Offline', value=f'{member_offline}', inline=False)
        else:
            embed=discord.Embed(title='', description=f'{member.mention}')
            embed.set_thumbnail(url=f'{member.avatar_url}')
            embed.add_field(name='Nick', value=f'{member.name}', inline=True)
            embed.add_field(name='ID', value=f'{member.id}', inline=True)
            embed.add_field(name='Create at', value=f'{member.created_at}', inline=False)
            embed.add_field(name='Join at', value=f'{member.joined_at}', inline=False)
            embed.add_field(name='Status', value=f'{member.status}', inline=True)
            embed.add_field(name='Activity', value=f'{member.activity}', inline=True)
            embed.add_field(name='Bot', value=f'{member.bot}', inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))