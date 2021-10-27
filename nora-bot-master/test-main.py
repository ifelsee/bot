import discord
from discord.ext import commands 
from discord.ext import tasks

client = commands.Bot(command_prefix='nora ')

async def on_ready():
    print('Bot Giriş Yaptı {0.user}'.format(client))
    print("Giriş Saati:")
    print("Bot İd:")



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else: pass
    global sarkii
    thisMsg = message.content.lower()
    print(thisMsg)
    thisAutor = message.author
    
    print(message.author, " : ", str(thisMsg))



client.run(token)
