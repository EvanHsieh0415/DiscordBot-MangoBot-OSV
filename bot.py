import discord
import json
import os
from discord.ext import commands

with open('.\\settings\\channel.json', 'r', encoding='utf8') as ChannelFile:
    ChannelData = json.load(ChannelFile)
with open('.\\settings\\token.json', 'r', encoding='utf8') as TokenFile:
    TokenData = json.load(TokenFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix= 'mb> ', intents = intents)

@bot.event  
async def on_ready():
    print('>> Mango Bot OSV is online <<')
    channel = bot.get_channel(int(ChannelData['feedback']['channel']))
    await channel.send('>> Mango Bot OSV is online <<')

for Filename in os.listdir('.\\commands'):
    if Filename.endswith('.py'):
        bot.load_extension(f'commands.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(TokenData['token'])