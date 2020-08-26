import discord
from discord.ext import commands
import tsReq

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Activation.')

@client.event
async def on_message(message):
    if message.content == 'shame DEFYN' or message.content == 'shame doof':
        await message.channel.send("Defyn is a fat whore")
    if message.content.startswith('shame'):
        commands = message.content.split(" ")
        try:
            if len(commands) == 3: 
                await message.channel.send("```\nShame on " + commands[1] + "\n" + tsReq.req_stat_plane(commands[1],commands[2])+ "```")
            elif len(commands) == 2:
                await message.channel.send("```\n" + commands[1] + " is trash\n" + tsReq.req_worst(commands[1]) + "```" )
            return
        except:
            await message.channel.send("```\nBad Input\n```")
            return


client.run()
