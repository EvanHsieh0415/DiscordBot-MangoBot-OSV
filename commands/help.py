import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio

def help_menu(cmds, lang):
    if lang == 'en_us':
        if cmds == 'all':
            pass
        elif cmds == 'mail':
            text = '> `mail` - mb> mail [Channel ID] [Message]\n> send [Message] to [Channel ID]'
        elif cmds == 'pipe_mail':
            text = '> `pipe_mail` - mb> mail [Pipe Number] [Message]\n > Send [Message] through Pipe [Pipe Number]'
    elif lang == 'zh_tw':
        if cmds == 'all':
            pass
        elif cmds == 'mail':
            text = '> `mail` - mb> mail [Channel ID] [Message]\n> 傳送 [Message] 到 [Channel ID]'
        elif cmds == 'pipe_mail':
            text = '> `pipe_mail` - mb> mail [Pipe Number] [Message]\n > 透過管道[Pipe Number] 傳送訊息 [Message]'
    return text

all_pages = 6
def help1():
    embed = discord.Embed(title="幫助─目錄")
    embed.add_field(name="```1:```", value="目錄", inline=True)
    embed.add_field(name="```2:```", value="小遊戲", inline=True)
    embed.add_field(name="```3:```", value="資料", inline=True)
    embed.add_field(name="```4:```", value="管理員", inline=True)
    embed.add_field(name="```5:```", value="其它指令", inline=True)
    embed.add_field(name="```6:```", value="機器人擁有者指令", inline=True)
    embed.set_image(url="https://media.discordapp.net/attachments/616315208251605005/616319462349602816/Tw.gif")
    embed.set_footer(text=f"Page:1/{all_pages}")
    return embed

def chack(a):
    if a==1:
        return help1()

class help(Cog_Extension):
    @commands.command()
    async def help_(self, ctx, cmd, lang):
        await ctx.send(help_menu(cmds=cmd, lang=lang))

    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        cur_page = 1
        msg = await ctx.send(embed=chack(cur_page))
        await msg.add_reaction("◀️")
        await msg.add_reaction("▶️")
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"] and msg.id == reaction.message.id
        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check)
                if str(reaction.emoji) == "▶️" and cur_page != all_pages:
                    cur_page += 1
                    await msg.edit(embed=chack(cur_page))
                    await msg.remove_reaction(reaction, user)
                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await msg.edit(embed=chack(cur_page))
                    await msg.remove_reaction(reaction, user)
                else:
                    await msg.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                await msg.delete()
                break

def setup(bot):
    bot.add_cog(help(bot))
