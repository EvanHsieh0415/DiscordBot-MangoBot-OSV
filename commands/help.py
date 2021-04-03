import discord
from discord.ext import commands
from core.classes import Cog_Extension

class help(Cog_Extension):
    @commands.command()
    async def help_(self, ctx, page:int):
        maxpage = 2
        if page == 1:
            help_type = 'Game'
        embed=discord.Embed(title=f'page: {page}', description=help_type)
        embed.set_author(name='Help')
        embed.set_footer(text=f'Page {page}/{maxpage}')
        await ctx.send(embed=embed)

    @commands.command()
    async def call_owner(self, ctx, *, msg:str=None):
        if msg == None:
            await ctx.send('請輸入內容')
        else:
            print('='*50, f'\n{ctx.author.name} in {ctx.guild} call:\n{msg}\n', '='*50)
            owner = self.bot.get_user(self.bot.owner_id)
            await owner.send(f'`{ctx.author.name}` in `{ctx.guild}` call:\n> {msg}')
            await ctx.send(f'已傳送訊息給{owner.name}')

def setup(bot):
    bot.add_cog(help(bot))
