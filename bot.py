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
        return
    if message.content.startswith('shame'):
        commands = message.content.split(" ")
        try:
            ret = tsReq.getStats(commands[1],commands[2])
        except:
            await message.channel.send("```Bad Input```")
            return
        print("-----"+str(message.author)+"-----")
        tsReq.stdoutStats(ret)
        await message.channel.send(tsReq.stroutStats(ret))
        return

client.run("hello world")
