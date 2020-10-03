import discord
from discord.ext import commands
import tsReq
import tankReq
import traceback
import sys
#test track
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Activation.')

@client.event
async def on_message(message):
    if message.content == 'help shame':
        await message.channel.send("```\n cherrypick [username] [plane] gives someones stats in specified aircraft \n shame/shamekb [username] [optional number to output] [optional min battles] gives someones worst planes sorted by KD/KB \n flex/flexkb [username] [optional number to output] [optional min battles] gives someones best planes sorted by KD/KB \n ```")
    if message.content == 'shame DEFYN' or message.content == 'shame doof':
        await message.channel.send("Defyn is a fat whore")
    if message.content.startswith('cherrypick'):
        commands = message.content.split(" ")
        try:
            await message.channel.send("```\nShame on " 
            + commands[1] 
            + "\n" 
            + tsReq.req_stat_plane(commands[1],commands[2])
            + "```")
            await message.channel.send("```\n Stats are not guaranteed correct (ssn's lightning for example)\n```")
            return
        except:
            traceback.print_exc()
            await message.channel.send("```\nBad Input\n```")
            return
    elif message.content.startswith('shame'):
        commands = message.content.split(" ")
        if len(commands[0]) > 5:
            mode = "KB"
        else:
            mode = "KD"
        try:
            if len(commands) == 3:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tsReq.req_worst(commands[1],50,int(commands[2]),mode) 
                + "```" )
            elif len(commands) == 2:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tsReq.req_worst(commands[1],50,3,mode) + "```" )
            elif len(commands) == 4:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tsReq.req_worst(commands[1],int(commands[3]),int(commands[2]),mode) 
                + "```" )
            await message.channel.send("```\n Stats are not guaranteed correct (ssn's lightning for example)\n```")
            return
        except:
            traceback.print_exc()
            await message.channel.send("```\n"+"BAD INPUT\n"+"```")
    elif message.content.startswith("flex"):
        commands = message.content.split(" ")
        if len(commands[0]) > 4:
            mode = "KB"
        else:
            mode = "KD"
        try:
            if len(commands) == 3:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tsReq.req_best(commands[1],50,int(commands[2]),mode) 
                + "```" )
            elif len(commands) == 2:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tsReq.req_best(commands[1],50,3,mode) 
                + "```" )
            elif len(commands) == 4:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tsReq.req_best(commands[1],int(commands[3]),int(commands[2]),mode) 
                + "```" )
            await message.channel.send("```\n Stats are not guaranteed correct (ssn's lightning for example)\n```")
            return
        except:
            traceback.print_exc()
            await message.channel.send("```\n"+"BAD INPUT\n"+"```")

    elif message.content.startswith('tcherrypick'):
        commands = message.content.split(" ")
        try:
            await message.channel.send("```\nShame on " 
            + commands[1] 
            + "\n" 
            + tankReq.req_stat_plane(commands[1],commands[2])
            + "```")
            await message.channel.send("```\n Stats are not guaranteed correct (ssn's lightning for example)\n```")
            return
        except:
            traceback.print_exc()
            await message.channel.send("```\nBad Input\n```")
            return
    elif message.content.startswith('tshame'):
        commands = message.content.split(" ")
        if len(commands[0]) > 6:
            mode = "KB"
        else:
            mode = "KD"
        try:
            if len(commands) == 3:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tankReq.req_worst(commands[1],50,int(commands[2]),mode) 
                + "```" )
            elif len(commands) == 2:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tankReq.req_worst(commands[1],50,3,mode) + "```" )
            elif len(commands) == 4:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tankReq.req_worst(commands[1],int(commands[3]),int(commands[2]),mode) 
                + "```" )
            await message.channel.send("```\n Stats are not guaranteed correct (ssn's lightning for example)\n```")
            return
        except:
            traceback.print_exc()
            await message.channel.send("```\n"+"BAD INPUT\n"+"```")
    elif message.content.startswith("tflex"):
        commands = message.content.split(" ")
        if len(commands[0]) > 5:
            mode = "KB"
        else:
            mode = "KD"
        try:
            if len(commands) == 3:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tankReq.req_best(commands[1],50,int(commands[2]),mode) 
                + "```" )
            elif len(commands) == 2:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tankReq.req_best(commands[1],50,3,mode) 
                + "```" )
            elif len(commands) == 4:
                await message.channel.send("```\n" 
                + commands[1] 
                + " is trash\n" 
                + tankReq.req_best(commands[1],int(commands[3]),int(commands[2]),mode) 
                + "```" )
            await message.channel.send("```\n Stats are not guaranteed correct (ssn's lightning for example)\n```")
            return
        except:
            traceback.print_exc()
            await message.channel.send("```\n"+"BAD INPUT\n"+"```")
    return

print(sys.argv[1])
while (True):
    client.run(sys.argv[1])
