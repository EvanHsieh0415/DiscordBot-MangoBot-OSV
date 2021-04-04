import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open(r'.\settings\search.json', 'r', encoding='utf8') as SearchFile:
    SearchData = json.load(SearchFile)

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
            embed=discord.Embed(title='Game 遊戲大廳', description='遊戲指令前綴 `g`')
            embed.add_field(name='丟硬幣', value='cf', inline=True)
            embed.add_field(name='骰子 (可自訂義面數 預設為6面骰)', value='`dice [side]`', inline=True)
            embed.add_field(name='向機器人丟東西', value='`drop [some thing]`', inline=True)
            embed.add_field(name='問問題', value='`r [question]`', inline=True)
            await ctx.send(embed=embed)
        elif page == 2:
            embed=discord.Embed(title=f'目前可搜尋之引擎有 `{len(SearchData["seartch_list"])}`', description='(若無輸入搜尋內容 將返回該搜尋引擎之主頁)')
            embed.set_author(name='Search 搜尋系統')
            embed.add_field(name='Google 搜尋', value='`google [index]`', inline=True)
            embed.add_field(name='Wikipedia 維基百科', value='`wiki [index]`', inline=True)
            await ctx.send(embed=embed)
        elif page == 3:
            embed=discord.Embed(title='可搜尋的資訊有: `channel頻道, role身分組, member成員`', description='(若無輸入查詢之目標 將返回伺服器之資訊)')
            embed.set_author(name='Information 搜尋系統')
            embed.add_field(name='Channel 頻道', value='`channel [ channel ID ]`', inline=True)
            embed.add_field(name='Role 身分組', value='`role [ role name ]`', inline=True)
            embed.add_field(name='Member 成員', value='`member [ member name ]`', inline=True)
            await ctx.send(embed=embed)
        elif page == 4:
            embed=discord.Embed(title='入群後請進行驗證 驗證完成後 將會能使用伺服器更多的功能', description='(若已經驗證完成 將無法再次進行驗證 每個伺服器之驗證將為分別計算)')
            embed.set_author(name='Verify 驗證系統')
            embed.add_field(name='Get 取得驗證碼 機器人會私訊你驗證碼', value='`get`', inline=True)
            embed.add_field(name='Enter 輸入驗證碼 若輸入錯誤將會重新生成驗證碼', value='`enter [ verify code ]`', inline=True)
            await ctx.send(embed=embed)
        elif page == 5:
            embed=discord.Embed(title='經濟系統 可以努力工作賺錢.w.')
            embed.set_author(name='Economy 經濟系統')
            embed.add_field(name='Work 工作！', value='`work`', inline=True)
            embed.add_field(name='My Wallet 我的錢包', value='`my_wallet`', inline=True)
            await ctx.send(embed=embed)
        elif page == 6:
            embed=discord.Embed(title='回饋 發生了什麼錯誤OAO 趕快回報我！', description='注意！ 若任意回報將通知該群之管理員 進行懲處')
            embed.set_author(name='Feedback 回饋')
            embed.add_field(name='Call 私訊機器人擁有者', value='`call_owner`', inline=True)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title='該頁數不存在！！！', description='請重新確認 是否輸入錯誤')
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
