import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open(r'.\settings\guild_info.json', mode='r', encoding='utf8') as GuildinfoFile:
    GuildinfoData = json.load(GuildinfoFile)

class info(Cog_Extension):
    @commands.command()
    async def role(self, ctx, role_name:str=None):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name=role_name)
        if role_name == None:
            role_count = len(guild.roles)
            
            embed=discord.Embed(description='Roles')
            embed.add_field(name='Count', value=role_count, inline=False)
            for i in range(3):
                embed.add_field(name='===', value='-----', inline=True)
            for i in range(len(guild.roles)):
                if guild.roles[i].name != '@everyone':
                    embed.add_field(name=guild.roles[i], value=len(guild.roles[i].members), inline=True)
        else:
            role_member_count = len(role.members)
            embed=discord.Embed(description=role.mention)
            embed.add_field(name='Members', value=role_member_count, inline=True)
            embed.add_field(name='Position', value=role.position, inline=True)
            embed.add_field(name='Color', value=role.color, inline=True)
            embed.add_field(name='ID', value=role.id, inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def member(self, ctx, *, member_name:str=None):
        guild = ctx.guild
        member = discord.utils.get(guild.members, name=member_name)
        if member_name == None:
            member_count = len([i for i in guild.members if i.bot == False])
            member_bot_count = len([i for i in guild.members if i.bot])
            member_online = len([i for i in guild.members if i.status == discord.Status.online])
            member_idle = len([i for i in guild.members if i.status == discord.Status.idle])
            member_dnd = len([i for i in guild.members if i.status == discord.Status.dnd])
            member_offline = len([i for i in guild.members if i.status == discord.Status.offline])

            embed=discord.Embed(description='Members')
            embed.add_field(name='Member Count', value=member_count, inline=True)
            embed.add_field(name='Bot Count', value=member_bot_count, inline=True)
            embed.add_field(name='ﱞ', value='ﱞ', inline=True)
            embed.add_field(name='Online', value=member_online, inline=True)
            embed.add_field(name='Idle', value=member_idle, inline=True)
            embed.add_field(name='Do Not Disturb', value=member_dnd, inline=True)
            embed.add_field(name='Offline', value=member_offline, inline=True)
        else:
            embed=discord.Embed(title='', description=member.mention)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name='Nick', value=member.nick, inline=True)
            embed.add_field(name='ID', value=member.id, inline=True)
            embed.add_field(name='Create at', value=member.created_at.strftime(r'%Y/%m/%d %H:%M')
            , inline=False)
            embed.add_field(name='Join at', value=member.joined_at.strftime(r'%Y/%m/%d %H:%M'), inline=False)
            embed.add_field(name='Status', value=member.status, inline=True)
            embed.add_field(name='Activity', value=member.activity, inline=True)
            embed.add_field(name='Bot', value=member.bot, inline=True)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def channel(self, ctx, *, channel:int=None):
        if channel == None:
            embed=discord.Embed(description='channel')
            embed.add_field(name='Text', value=len(ctx.guild.text_channel), inline=True)
            embed.add_field(name='Voice', value=len(ctx.guild.voice_channel), inline=True)
        else:
            channel = discord.utils.get(ctx.guild.channels, id=channel)
            embed=discord.Embed(description=channel.name)
            embed.add_field(name='Name', value=channel.name, inline=True)
            embed.add_field(name='Channel Type', value=channel.type, inline=True)
            embed.add_field(name='ID', value=channel.id, inline=False)
            if channel.type == discord.ChannelType.text:
                embed.add_field(name='Topic', value=channel.type, inline=True)
                if channel.slowmode_delay == 0:
                    slow = 'disable'
                else:
                    slow = channel.slowmode_delay
                embed.add_field(name='Slowmode', value=slow, inline=True)
            elif channel.type == discord.ChannelType.voice:
                embed.add_field(name='Bitrate', value=channel.bitrate, inline=True)
                embed.add_field(name='Max user', value=channel.user_limit, inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))