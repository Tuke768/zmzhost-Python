import discord 
import json
from discord.ext import commands


with open('config.json') as e: 
  set_config = json.load(e)
  TOKEN = set_config['token']
  PREFIX = set_confog['prefix']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
    print('Pronto para uso!\n') 
    await bot.change_presence(activity=discord.Streaming(name="BOT HOSPEDADO NA ZMZHOST", url="https://www.twitch.tv/discord"))


@client.command()
async def teste(ctx):
     await canal.send('TESTE')
  
client.run(TOKEN)
