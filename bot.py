import discord
import json, os
from discord.ext import commands

not_load = ['test.py']

with open('.\\settings\\event.json', mode='r', encoding='utf8') as EventFile:
    EventData = json.load(EventFile)
with open('.\\settings\\setting.json', mode='r', encoding='utf8') as SettingFile:
    SettingData = json.load(SettingFile)
with open('.\\settings\\token.json', mode='r', encoding='utf8') as TokenFile:
    TokenData = json.load(TokenFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix= 'mb>', intents = intents)

@bot.event  
async def on_ready():
    print('>> Mango Bot OSV is online <<')
    if EventData['on_ready']['feedback']['enable'] == True:
        for i in EventData['on_ready']['feedback']['channel']:
            channel = bot.get_channel(i)
            bot_name = SettingData['bot_name']
            await channel.send(f'【Bot】**{bot_name}** is online')

for Filename in os.listdir('.\\commands'):
    if Filename.endswith('.py') and Filename not in not_load:
        bot.load_extension(f'commands.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(TokenData['token'])