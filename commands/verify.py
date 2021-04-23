import discord
import json, random
from discord.ext import commands
from core.classes import Cog_Extension

def verify_setting(ctx, setType:str, limit:int=''):
    if setType in ['longer', 'digit', 'set_all']:
        with open(r'.\settings\verification.json', mode='r', encoding='utf8') as verifySetFile:
            verifySetData = json.load(verifySetFile)
        if setType in ['longer', 'digit']:
            verifySetData[str(ctx.guild.id)]['index'][setType] = limit
        elif setType == 'set_all':
            verifySetData[str(ctx.guild.id)] = {'name':ctx.guild.name, 'index': {'longer': 4, 'digit': 4}}
        with open(r'.\settings\verification.json', mode='w', encoding='utf8') as verifySetFile:
            json.dump(verifySetData, verifySetFile, sort_keys=True, indent=4, ensure_ascii=False)
    elif setType in ['member_all', 'member_setup']:
        with open(r'.\data\verification.json', mode='r', encoding='utf8') as verifyFile:
            verifyData = json.load(verifyFile)
        if setType == 'member_all':
            verifyData[str(ctx.guild.id)] = {'name': ctx.guild.name, 'index': {}}
            for i in ctx.guild.members:
                verifyData[str(ctx.guild.id)]['index'][str(i.id)] = {'name': i.name, 'count': 0, 'verCode': None, 'pass': False}
        elif setType == 'member_setup':
            verifyData = {}
        with open(r'.\data\verification.json', mode='w', encoding='utf8') as verifyFile:
            json.dump(verifyData, verifyFile, sort_keys=True, indent=4, ensure_ascii=False)

    
    print(f'{ctx.author.name} - {ctx.author.id} Set {setType}: {limit}')
    fb = f'Set {setType}: {limit}'
    return fb

def get_verifyCode(ctx):
    with open(r'.\data\verification.json', mode='r', encoding='utf8') as verifyFile:
        verifyData = json.load(verifyFile)
    with open(r'.\settings\verification.json', mode='r', encoding='utf8') as verifySetFile:
        verifySetData = json.load(verifySetFile)
    if verifyData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['pass'] == False:
        longer = verifySetData[str(ctx.guild.id)]['index']['longer']
        digit = verifySetData[str(ctx.guild.id)]['index']['digit']

        ch_l = []
        digit_num = int('F'*digit, 16)
        for i in range(longer):
            ch_l.append(str(hex(random.randint(0, digit_num)).replace('0x', '')).zfill(digit))
        code = '-'.join(ch_l)
        verifyData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['count'] += 1
        verifyData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['verCode'] = code
        with open(r'.\data\verification.json', mode='w', encoding='utf8') as verifyFile:
            json.dump(verifyData, verifyFile, sort_keys=True, indent=4, ensure_ascii=False)

        print(f'{ctx.author.name} - {ctx.author.id} Get VerCode: {code}')
        fb = f'你的驗證碼為 `{code}`'
    else:
        fb = '你已驗證完成, 不得再次進行驗證'
    return fb

def enter_verifyCode(ctx, enterCode):
    with open(r'.\data\verification.json', mode='r', encoding='utf8') as verifyDataFile:
        verifyData = json.load(verifyDataFile)
    if verifyData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['pass'] == False:
        cc = verifyData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['verCode']
        if cc == enterCode:
            verifyData[str(ctx.guild.id)]['index'][str(ctx.author.id)]['pass'] = True
            with open(r'.\data\verification.json', mode='w', encoding='utf8') as verifyDataFile:
                json.dump(verifyData, verifyDataFile, sort_keys=True, indent=4, ensure_ascii=False)
            print(f'{ctx.author.name} - {ctx.author.id} successfully verified -\n>>> Verification code')
            fb ='驗證成功'
        else:
            print(f'{ctx.author.name} - {ctx.author.id} enter error -\n>> correct code: {cc}\n>> enter code: {enterCode}')
            code = get_verifyCode(ctx=ctx)
            fb = f'{ctx.author.name} 驗證失敗\n 已重新生成驗證碼\n新的驗證碼為 `{code}`'
    else:
        fb = '你已驗證完成, 不得再次進行驗證'
    return fb

class verify(Cog_Extension):
    @commands.group()
    async def verify(self, ctx):
        pass
    
    @verify.command()
    async def get(self, ctx):
        await ctx.author.send(get_verifyCode(ctx=ctx))
    
    @verify.command()
    async def enter(self, ctx, code:str):
        await ctx.author.send(enter_verifyCode(ctx=ctx, enterCode=code))
    
    @commands.is_owner()
    @verify.command()
    async def set(self, ctx, Type:str, Limit:int=None):
        await ctx.send(verify_setting(ctx=ctx, setType=Type, limit=Limit))

def setup(bot):
    bot.add_cog(verify(bot))