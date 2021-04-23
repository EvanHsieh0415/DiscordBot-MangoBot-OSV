import discord
import json, datetime, traceback
from discord.ext import commands
from core.classes import Cog_Extension

with open(r'.\settings\event.json', 'r', encoding='utf8') as EventFile:
    EventData = json.load(EventFile)

with open(r'.\data\exp.json', 'r', encoding='utf8') as ExpMemberFile:
    ExpMemberData = json.load(ExpMemberFile)

def channel_function(event_type:str, member, self):
    if event_type == 'join':
        channel = self.bot.get_channel(int(EventData[str(member.guild.id)]['feedback']['join']['channel']))
    elif event_type == 'leave':
        channel = self.bot.get_channel(int(EventData[str(member.guild.id)]['feedback']['leave']['channel']))
    return channel

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} join {member.guild.name}!')
        if EventData[str(member.guild.id)]['feedback']['enable'] == True:
            channel = channel_function(event_type='join', member=member, self=self)
            embed=discord.Embed(title=f"{member.name}跳進了伺服器！", description="0w0", color=0x5fff5c, timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_thumbnail(url=f"{member.avatar_url}")
            embed.add_field(name="本伺服器所有者是", value=f"{member.guild.owner}", inline=True)
            embed.add_field(name="伺服器人數：", value=f"{member.guild.member_count}", inline=True)
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} leave {member.guild.name}!!')
        if EventData[str(member.guild.id)]['feedback']['enable'] == True:
            channel = channel_function(event_type='leave', member=member, self=self)
            embed=discord.Embed(title=f"{member.name} 離開了伺服器...", color=0xff0000, timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_thumbnail(url=f"{member.avatar_url}")
            await channel.send(embed=embed)

    # @commands.Cog.listener()
    # async def on_message(self, msg:str):
    #     if msg.author.bot == False:
    #         expAdd = len(msg)
    #         ExpMemberData[str(msg.guild.id)]['index'][str(msg.author.id)]['exp'] += expAdd
    #         with open(r'.\data\exp.json', 'w', encoding='utf8') as ExpMemberFile:
    #             json.dump(ExpMemberData, ExpMemberFile, sort_keys=True, indent=4)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        print(''.join(traceback.format_exception(type(error), error, error.__traceback__)))

def setup(bot):
    bot.add_cog(event(bot))
