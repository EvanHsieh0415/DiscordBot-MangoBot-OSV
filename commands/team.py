import discord
import json, random
from discord.ext import commands
from core.classes import Cog_Extension

with open(r'.\settings\team.json', mode='r', encoding='utf8') as TeamFile:
    TeamData = json.load(TeamFile)

class team(Cog_Extension):
    @commands.group()
    async def t(self, ctx):
        if 't ' not in ctx.message.content and 't' in ctx.message.content:
            await ctx.send('請輸入後綴')
    
    @t.command()
    async def random(self, ctx, count:int=4):
        members = ctx.guild.members
        TeamData['team_count'] = count
        for i in range(count):
            TeamData['teams'][i] = {'members': {}}
        
        dict_member = {}
        for i in members:
            if i.bot is False:
                dict_member[i.name] = i.id
        
        await ctx.send(json.dumps(dict_member, sort_keys=True, indent=4, ensure_ascii=False))

        for i0 in range(count):
            for i1 in range(len(dict_member)//count):
                member = random.choice(dict_member)
                TeamData['teams'][i0]['members'][i1] = {member['name']: member['id']}
                del dict_member[member]
            # if len(dict_member)%count > 0:
            #     TeamData['teams'][i0]['members'][i1+1] = {member['name']: member['id']}
            #     del dict_member[member]

            await ctx.send(json.dumps(TeamData, sort_keys=True, indent=4, ensure_ascii=False))
def setup(bot):
    bot.add_cog(team(bot))