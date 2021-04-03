import discord
from discord.ext import commands
from core.classes import Cog_Extension

class help(Cog_Extension):
    @commands.command()
    async def menu(self, ctx, page:int=0):
        if page == 0:
            embed=discord.Embed(title='Help Menu', description='幫助菜單(?)')
            embed.add_field(name='1. Game 遊戲大廳', value='Page: 1', inline=True)
            embed.add_field(name='2. Search 搜尋系統', value='Page: 2', inline=True)
            embed.add_field(name='3. Information 資訊查詢', value='Page: 3', inline=True)
            embed.add_field(name='4. Verify 驗證系統', value='Page: 4', inline=True)
            embed.add_field(name='5. Economy 經濟系統', value='Page: 5', inline=True)
            embed.add_field(name='6. Feedback 回饋', value='Page: 6', inline=True)
            await ctx.send(embed=embed)
        elif page == 1:
            pass
        elif page == 2:
            pass
        elif page == 3:
            pass
        elif page == 4:
            pass
        elif page == 5:
            pass
        elif page == 6:
            pass


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
