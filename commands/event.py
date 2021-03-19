import discord
import json, datetime
from discord.ext import commands
from core.classes import Cog_Extension

with open('.\\settings\\event.json', 'r', encoding='utf8') as EventFile:
    EventData = json.load(EventFile)

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} join {member.guild.name}!')
        channel = self.bot.get_channel(int(EventData[str(member.guild.id)]['feedback']['join']['channel']))
        embed=discord.Embed(title=f"{member.name}跳進了伺服器！", description="0w0", color=0x5fff5c, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name="本伺服器所有者是", value=f"{member.guild.owner}", inline=True)
        embed.add_field(name="伺服器人數：", value=f"{member.guild.member_count}", inline=True)
        await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} leave {member.guild.name}!!')
        channel = self.bot.get_channel(int(EventData[str(member.guild.id)]['feedback']['leave']['channel']))
        embed=discord.Embed(title=f"{member.name} 離開了伺服器...", color=0xff0000, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_thumbnail(url=f"{member.avatar_url}")
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(event(bot))
